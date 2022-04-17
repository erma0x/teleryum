import sys
import os
import time
import socket

from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+2.0))

from pprint import pprint
from copy import deepcopy

from termcolor import colored
from dotenv import load_dotenv

import asyncio
from telethon import TelegramClient, events

import ccxt

from ftx_api.client import FtxClient
from ftx_api.perpetuals import ftx_perpetuals
from channels import *
from params import *


def print_start():
    print(colored(LOGO,"cyan"))
    now = datetime.now(tzinfo)
    print(colored("\t SERVER ONLINE ","green"),now.strftime("%d/%m/%Y %H:%M:%S\n\n"))

def print_op_data(op_data):
    print(colored('OPERATION DATA','cyan'))
    print('symbol         \t',op_data['symbol'])
    print('trade side     \t',op_data['side'])
    print('entry prices   \t',' '.join(op_data['entry_prices']))
    print('take profits   \t',' '.join(op_data['take_profits']))
    print('stop losses    \t',' '.join(op_data['stop_losses']))
    print('leverage       \t',op_data['leverage'])

def print_message(message,channel):
    print('~'*70)
    print('\n',colored('NEW SIGNAL','green'),colored(channel,'cyan'),'\t', str(datetime.now(tzinfo))[:-13],'\n\n',message,'\n')



def parser_CHANNEL_1(new_message):

    op_data = deepcopy(base_operation_data_structure)

    if 'Binance Futures Signal' in new_message:
        TEXT_PATTERNS = ('Tp','Stoploss','Leverage','@')    
        for pattern in TEXT_PATTERNS:
                if pattern not in new_message:
                    return None

        for row in new_message.split('\n'): 
            if '#' in row:

                entry_prices = row.split('@')[-1].replace(' ','')
                op_data['entry_prices'].append(entry_prices)

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




def opposite(type_order):
    if type_order=='buy':
        return 'sell'
    return 'buy'

def get_free_balance_FTX():
    client = FtxClient(api_key=FTX_READONLY_C1,api_secret=FTX_READONLY_C1_HASH,subaccount_name='c1')
    free_balance = client.get_balances()[0]['free']
    #print('YOUR FREE BALANCE: '+str(round(free_balance,2)))
    return float(free_balance)

def get_total_balance_FTX( percentage_for_position=0.03 ):
    client = FtxClient(api_key=FTX_READONLY_C1,api_secret=FTX_READONLY_C1_HASH,subaccount_name='c1')
    total_balance = client.get_balances()[0]['total']
    return float(total_balance)

async def get_amount_position_usdt():
    total_balance = get_total_balance_FTX()

    if total_balance > 300:
        amount_position_usdt =  total_balance * 0.03   # get 3% of the position
    elif total_balance > 200:
        amount_usd_position =  total_balance * 0.1    # get 10% of the position
    else:
        amount_usd_position = 20

    return amount_usd_position

def balance_trigger_orders_quantity(trigger_prices, entry_quantity):
    trigger_quantities = []
    single_trigger_quantity = round( entry_quantity/len(trigger_prices) ,8)
    n_triggers = len(trigger_prices)

    if n_triggers > 1:
        if 0 != entry_quantity % ( single_trigger_quantity * (n_triggers-1) ):
            trigger_quantities = [single_trigger_quantity for i in trigger_prices][:-1]
            last_trigger_quantity = entry_quantity % ( single_trigger_quantity * (n_triggers-1) ) + single_trigger_quantity
            trigger_quantities.append(last_trigger_quantity)
        else:
            trigger_quantities = [single_trigger_quantity for i in trigger_prices]
            
    else:
        trigger_quantities.append(entry_quantity)

    return trigger_quantities

def sort_orders(op_data_structure):
    if op_data_structure['side'] == 'buy':
        op_data_structure['take_profits'] = sorted(op_data_structure['take_profits'])
        op_data_structure['stop_losses'] = sorted(op_data_structure['stop_losses'],reverse=True)
    else:
        op_data_structure['take_profits'] = sorted(op_data_structure['take_profits'],reverse=True)
        op_data_structure['stop_losses'] = sorted(op_data_structure['stop_losses'])
    return op_data_structure

def string_to_float_prices(op_data_structure):
    columns = ['entry_prices','take_profits','stop_losses']
    for col in columns:
        for i in range(len(op_data_structure[col])):
            op_data_structure[col][i] = float(op_data_structure[col][i])
    return op_data_structure

async def trader_ccxt(order_data, exchange):

    order_data = string_to_float_prices(op_data_structure=order_data)
    order_data = sort_orders(op_data_structure=order_data)

    n_entry_prices = len(order_data['entry_prices'])
    n_take_profits = len(order_data['take_profits'])
    n_stop_losses = len(order_data['stop_losses'])
    
    amount_usd_position = await get_amount_position_usdt()

    if print_op: print('position in usdt $ ',amount_usd_position,'real LEVERAGE on FTX: 2 ')
    
    maintenance_capital = 0.05
    if get_free_balance_FTX() < (1+maintenance_capital) * amount_usd_position:
        return None

    for i in range(len(order_data['entry_prices'])): 
        
        entry_price = deepcopy(order_data['entry_prices'][i])
        amount_token_position = round( amount_usd_position / n_entry_prices / entry_price , 8 )

        if print_op: print('amount_token_position ',amount_token_position)      
        entry_order = exchange.create_limit_order(symbol = order_data['symbol'],
                                                side = order_data['side'],
                                                amount = amount_token_position,
                                                price = entry_price  )

        take_profit_quantities = balance_trigger_orders_quantity(order_data['take_profits'], amount_token_position)        
        if print_op: print('take_profit_quantities ',take_profit_quantities)
        for j in range(len(order_data['take_profits'])):
            take_profit_order = exchange.create_order(symbol = order_data['symbol'],
                                                    type = 'takeProfit',
                                                    side = opposite(order_data['side']),
                                                    amount = take_profit_quantities[j] ,
                                                    price = order_data['take_profits'][j],
                                                    params = {'triggerPrice':order_data['take_profits'][j],'reduceOnly':True })

        stop_loss_quantities = balance_trigger_orders_quantity(order_data['stop_losses'], amount_token_position)
        if print_op: print('stop_loss_quantities ',stop_loss_quantities)
        for k in range(len(order_data['stop_losses'])):
            stop_loss_order = exchange.create_order(symbol = order_data['symbol'],
                                                    type = 'stop',
                                                    side = opposite(order_data['side']),
                                                    amount = stop_loss_quantities[k],
                                                    price = order_data['stop_losses'][k],
                                                    params = {'triggerPrice':order_data['stop_losses'][k],'reduceOnly':True })

async def deamon_trader(op_data,channel):
    """ranking exchange from the hieghst leverage to the least"""

    FTX_C1 = os.getenv('FTX_C1')
    FTX_C1_HASH = os.getenv('FTX_C1_HASH')

    ftx_c1 = ccxt.ftx({
                    'headers': {
                    'FTX-SUBACCOUNT': 'c1',
                    },
                    'apiKey': FTX_C1,
                    'secret': FTX_C1_HASH,
                    'enableRateLimit': True,
                        })

    # kucoin_c1 = ccxt.kucoinfutures({
    #     'adjustForTimeDifference': True,
    #     "apiKey": '...',
    #     "secret": '...',
    #     'password': 'This is you 6-7 digit trading password',
    # })

    # kraken_c1 = ccxt.kraken({
    #     'adjustForTimeDifference': True,
    #     "apiKey": '...',
    #     "secret": '...',
    #     'password': 'This is you 6-7 digit trading password',
    # })


    FTX_C1 = os.getenv('FTX_C1')
    FTX_C1_HASH = os.getenv('FTX_C1_HASH')

    ftx_c1 = ccxt.ftx({
                    'headers': {
                    'FTX-SUBACCOUNT': 'c1',
                    },
                    'apiKey': FTX_C1,
                    'secret': FTX_C1_HASH,
                    'enableRateLimit': True,
                        })

    # kucoin_c1 = ccxt.kucoinfutures({
    #     'adjustForTimeDifference': True,
    #     "apiKey": '...',
    #     "secret": '...',
    #     'password': 'This is you 6-7 digit trading password',
    # })

    # kraken_c1 = ccxt.kraken({
    #     'adjustForTimeDifference': True,
    #     "apiKey": '...',
    #     "secret": '...',
    #     'password': 'This is you 6-7 digit trading password',
    # })

    # ftx_c2 = ccxt.ftx({
    #                 'headers': {
    #                 'FTX-SUBACCOUNT': 'c2',
    #                 },
    #                 'apiKey': FTX_C2,
    #                 'secret': FTX_C2_HASH,
    #                 'enableRateLimit': True,
    #                     })

    # kucoin_c2 = ccxt.kucoinfutures({
    #     'adjustForTimeDifference': True,
    #     "apiKey": '...',
    #     "secret": '...',
    #     'password': 'This is you 6-7 digit trading password',
    # })

    # kraken_c2 = ccxt.kraken({
    #     'adjustForTimeDifference': True,
    #     "apiKey": '...',
    #     "secret": '...',
    #     'password': 'This is you 6-7 digit trading password',
    # })

    if channel == 1 or channel == '1':
        if op_data['symbol'] in kucoin_perpetuals:
            await trader_ccxt( order_data = op_data , exchange = kucoin_c1)

        elif op_data['symbol'] in kraken_perpetuals:
            await trader_ccxt( order_data = op_data , exchange = kraken_c1 )     

        elif op_data['symbol'] in ftx_perpetuals:
            await trader_ccxt( order_data = op_data , exchange = ftx_c1 )     
        else:
            print('OPERATION UNSUCCESFUL: no ticker found    channel: ',channel)

    if channel == 2 or channel == '2':
        if op_data['symbol'] in kucoin_perpetuals:
            await trader_ccxt( order_data = op_data , exchange = kucoin_c2)

        elif op_data['symbol'] in kraken_perpetuals:
            await trader_ccxt( order_data = op_data , exchange = kraken_c2 )     

        elif op_data['symbol'] in ftx_perpetuals:
            await trader_ccxt( order_data = op_data , exchange = ftx_c2 )     
        else:
            print('OPERATION UNSUCCESFUL: no ticker found    channel: ',channel)

async def main():      
    load_dotenv()

    TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME')
    TELEGRAM_ID = os.getenv('TELEGRAM_ID')
    TELEGRAM_HASH = os.getenv('TELEGRAM_HASH')

    client = TelegramClient(TELEGRAM_USERNAME, TELEGRAM_ID, TELEGRAM_HASH) 

    if print_op: print_start()
    
    while True:

        # t.me/test_channel_pubblico_24991204  
        @client.on(events.NewMessage( chats = PUBLIC_TEST_CHANNEL ))
        async def trader_PUBLIC_TEST_CHANNEL( event ):
            NEW_MESSAGE = event.message.message
            signal = parser_CHANNEL_1( new_message = NEW_MESSAGE)
            if signal:
                print_message( message = NEW_MESSAGE, channel = PUBLIC_TEST_CHANNEL )
                # await deamon_trader_erma(op_data = signal, channel = 1)
                # await deamon_trader_lori(op_data = signal, channel = 1)


        # t.me/freecrypto_signals 
        @client.on(events.NewMessage( chats = CHANNEL_1 ))
        async def trader_CHANNEL_1( event ):
            NEW_MESSAGE = event.message.message
            signal = parser_CHANNEL_1( new_message = NEW_MESSAGE)
            if signal:
                print_message( message = NEW_MESSAGE, channel = CHANNEL_1 )
                # await global_trader()
            

        await asyncio.sleep(1)
        
        async with client:        
            if client.is_connected():
                #await client.loop.run_until_complete() 
                await client.run_until_disconnected() 

            else:
                await client.start()           

if __name__ == "__main__":

    load_dotenv()
    FTX_READONLY_C1 = os.getenv('FTX_READONLY_C1')
    FTX_READONLY_C1_HASH = os.getenv('FTX_READONLY_C1_HASH')

    asyncio.run(main())