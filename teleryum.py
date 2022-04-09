import sys
import os
from datetime import datetime, timezone, timedelta
from pprint import pprint
from copy import deepcopy

from termcolor import colored
from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import ccxt

from FTXclient import FtxClient
from FTXperpetuals import ftx_perpetuals
from params import *
from channels import *

def print_start():
    now = datetime.now(tzinfo)
    print(colored(LOGO,'cyan'), colored("\tteleryum server ","cyan"),colored("online","green"),now.strftime("%d/%m/%Y %H:%M:%S"),'\n\n')

def print_op_data(op_data):
    print('symbol         \t',op_data['symbol'])
    print('trade side     \t',op_data['side'])
    print('entry prices   \t',' '.join(op_data['entry_prices']))
    print('take profits   \t',' '.join(op_data['take_profits']))
    print('stop losses    \t',' '.join(op_data['stop_losses']))
    print('leverage       \t',op_data['leverage'])

def print_message(message,channel):
    print('\n',colored(' NEW SIGNAL  ','green'),colored(channel,'cyan'),'\t', str(datetime.now(tzinfo))[:-13],'\n\n',message,'\n')

def opposite(type_order):
    if type_order=='buy':
        return 'sell'
    return 'buy'

def get_free_balance():
    client = FtxClient(api_key=FTX_READONLY,api_secret=FTX_READONLY_HASH)
    order = float(client.get_balances()[0]['free'])
    #print('YOUR FREE BALANCE: '+str(round(order,2)))
    return order

def balance_trigger_orders_quantity(trigger_prices, entry_quantity):
    trigger_quantities = []
    single_trigger_quantity = round(entry_quantity/len(trigger_prices))
    n_triggers = len(trigger_prices)
    trigger_quantities = [single_trigger_quantity for i in trigger_prices][:-1]
    last_trigger_quantity = entry_quantity % ( single_trigger_quantity * (n_triggers-1) )
    trigger_quantities.append(last_trigger_quantity)
    return(trigger_quantities)   


def trader(order_data):

    print(colored('OPERATION DATA','cyan'))
    print_op_data(order_data)
    
    operation_position = 0.020 # 30 $ in ETH # TO 3% of my balance! # initial_capital = 100

    
    columns = ['entry_prices','take_profits','stop_losses']

    for col in columns:
        for i in range(len(order_data[col])):
            order_data[col][i] = float(order_data[col][i])

    if order_data['side'] == 'buy':
        order_data['take_profits'] = sorted(order_data['take_profits'])
        order_data['stop_losses'] = sorted(order_data['stop_losses'],reverse=True)
    else:
        order_data['take_profits'] = sorted(order_data['take_profits'],reverse=True)
        order_data['stop_losses'] = sorted(order_data['stop_losses'])

    n_entry_prices = len(order_data['entry_prices'])
    n_take_profits = len(order_data['take_profits'])
    n_stop_losses = len(order_data['stop_losses'])

    operation_balance = round(get_free_balance()/(n_entry_prices + 1 ),8)

    single_position = round( operation_position/n_entry_prices ,8)
    
    single_trade_amount = single_position,single_position

    for entry_price in order_data['entry_prices']:
        entry_order = exchange.create_limit_order(symbol=order_data['symbol'],
                                                 side=order_data['side'],
                                                 amount=single_position,
                                                 price=entry_price)

        trigger_quantities_TP = balance_trigger_orders_quantity(order_data['take_profits'], single_position)
        for index in range(len(order_data['take_profits'])):
            take_profit_order = exchange.create_order(symbol=order_data['symbol'],
                                                    type='takeProfit',
                                                    side=opposite(order_data['side']),
                                                    amount=round( trigger_quantities_TP[index] ,8),
                                                    price=order_data['take_profits'][index],
                                                    params={'triggerPrice':order_data['take_profits'][index],'reduceOnly':True })

        trigger_quantities_SL = balance_trigger_orders_quantity(order_data['stop_losses'], single_position)
        for index in order_data['stop_losses']:
            stop_loss_order = exchange.create_order(symbol=order_data['symbol'],
                                                    type='stop',
                                                    side=opposite(order_data['side']),
                                                    amount=round( trigger_quantities_SL[index] ,8),
                                                    price=order_data['stop_losses'][index],
                                                    params={'triggerPrice':order_data['stop_losses'][index],'reduceOnly':True })

def parser_CHANNEL_1(new_message):
    op_data = deepcopy(base_operation_data_structure)

    if 'Binance Futures Signal' in new_message:
        TEXT_PATTERNS = ('Tp','Stoploss','Leverage','@')    
        for pattern in TEXT_PATTERNS:
                if pattern not in new_message:
                    return None

        for row in new_message.split('\n'): 
            if '#' in row:
                op_data['entry_prices'].append(row.split('@')[-1].replace(' ',''))
                op_data['symbol'] = row.split(' ')[2].replace('#','').replace('/USDT','-PERP')

                if 'Buy' in row:
                    op_data['side']='buy'
                else:
                    op_data['side']='sell'

            if 'Tp' in row:
                op_data['take_profits'].append(row.split(':')[-1].replace(' ',''))

            if 'Stoploss' in row:
                op_data['stop_losses'].append(row.split(':')[-1].replace(' ',''))

            if 'Leverage' in row:
                op_data['leverage'] = row.split(' ')[-1].replace('x','')

    else:
        
        TEXT_PATTERNS = ('Sell','Buy','Stop','#','(',')')    
        for pattern in TEXT_PATTERNS:
            if pattern not in new_message:
                return None

        for row in new_message.split('\n'):
            if '#' in row:
                op_data['symbol'] = row[1:].replace(' ','')+'-PERP'

            if row.find('Buy') < row.find('Sell'):
                op_data['side']='sell'
            else:
                op_data['side']='buy'

            if 'Buy' in row:
                if '-' in row.split()[1]:
                    temp = row.split()[1].split('-')
                    for n in range(len(temp)):
                        op_data['entry_prices'].append(temp[n])
                else:
                    op_data['entry_prices'].append(row.split()[1])
            if 'Sell' in row:
                if '-' in row.split()[1]:
                    temp=row.split()[1].split('-')
                    for n in range(len(temp)):
                        op_data['take_profits'].append(temp[n])
                else:
                    op_data['take_profits'].append(row.split()[1])

            if 'StopLoss' in row or 'Stoploss' in row :
                if '-' in row.split()[1]:
                    temp = row.split()[1].split('-')
                    for n in range(len(temp)):
                        op_data['stop_losses'].append(temp[n])
                else:
                    op_data['stop_losses'].append(row.split()[1])

    return op_data



if __name__ == "__main__":

    load_dotenv()
    TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME')
    TELEGRAM_ID = os.getenv('TELEGRAM_ID')
    TELEGRAM_HASH = os.getenv('TELEGRAM_HASH')

    FTX_READONLY = os.getenv('FTX_READONLY')
    FTX_READONLY_HASH = os.getenv('FTX_READONLY_HASH')
    FTX_API_MAIN = os.getenv('FTX_API_MAIN')
    FTX_API_MAIN_HASH = os.getenv('FTX_API_MAIN_HASH')

    exchange = ccxt.ftx({
                    'apiKey': FTX_API_MAIN,
                    'secret': FTX_API_MAIN_HASH,
                    'enableRateLimit': True,
                        })

    client = TelegramClient(TELEGRAM_USERNAME, TELEGRAM_ID, TELEGRAM_HASH) 
    client.start()

    print_start()

    # PUBLIC_TEST_CHANNEL FAX SIMILE == freecrypto_signals 
    @client.on(events.NewMessage(chats=PUBLIC_TEST_CHANNEL))
    async def trader_PUBLIC_TEST_CHANNEL(event):
        NEW_MESSAGE = event.message.message
        op_data = parser_CHANNEL_1(new_message=NEW_MESSAGE)
        if op_data:
            if op_data['symbol'] in ftx_perpetuals:
                print_message(message=NEW_MESSAGE, channel=PUBLIC_TEST_CHANNEL)
                trader(order_data=op_data)

    # @client.on(events.NewMessage(chats=CHANNEL_1))
    # async def trader_PUBLIC_TEST_CHANNEL(event):
    #     NEW_MESSAGE = event.message.message
        
    #     print('\n',colored('NEW MESSAGE from : ','green'),CHANNEL_1,'\t', str(datetime.now(tzinfo))[:-13],'\n\n',NEW_MESSAGE,'\n')
    #     op_data = parser_CHANNEL_1(new_message=NEW_MESSAGE)
    #     if op_data:
    #         if op_data['symbol'] in ftx_perpetuals: # FTX EXCHANGE
    #             trader(order_data=op_data)
    
    
    with client:
        client.run_until_disconnected()