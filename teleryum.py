import sys
import os
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from pprint import pprint
from termcolor import colored
from copy import deepcopy

from telethon.sync import TelegramClient, events
import ccxt
from FTXclient import FtxClient
from FTXperpetuals import perpetuals
from params import *

def opposite(type_order):
    if type_order=='buy':
        return 'sell'
    return 'buy'

def get_free_balance():
    client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)
    order = float(client.get_balances()[0]['free'])
    # print('your free balance: '+str(round(order,2)))
    return order


def trader(order_data):
    print('\n',colored('NEW OPERATION','red'),'\n',order_data)
    
    operation_position = 0.020 # 30 $ in ETH

    n_entry_prices = len(order_data['entry_prices'])
    n_take_profits = len(order_data['take_profits'])
    n_stop_losses = len(order_data['stop_losses'])

    operation_balance = round(get_free_balance()/(n_entry_prices+1),8)

    single_position = round( operation_position/n_entry_prices ,8)

    for entry_price in order_data['entry_prices']:
        entry_order = exchange.create_limit_order(symbol=order_data['symbol'],
                                                 side=order_data['side'],
                                                 amount=single_position,
                                                 price=float(entry_price))

        for take_profit in order_data['take_profits']:
            take_profit_order = exchange.create_order(symbol=order_data['symbol'],
                                                    type='takeProfit',
                                                    side=opposite(order_data['side']),
                                                    amount=round( single_position/n_take_profits ,8),
                                                    price=float(take_profit),
                                                    params={'triggerPrice':float(take_profit),'reduceOnly':True })

        for stop_loss in order_data['stop_losses']:
            stop_loss_order = exchange.create_order(symbol=order_data['symbol'],
                                                    type='stop',
                                                    side=opposite(order_data['side']),
                                                    amount=round( single_position/n_stop_losses ,8),
                                                    price=float(stop_loss),
                                                    params={'triggerPrice':float(stop_loss),'reduceOnly':True })


def message_parser_freecrypto_signals(new_message):

    op_data = deepcopy(base_operation_data_structure)

    TEXT_PATTERNS = ('Sell','Buy','StopLoss','#','(',')')    
    for pattern in TEXT_PATTERNS:
            if pattern not in new_message:
                return None

    for row in new_message.split('\n'): # text messages
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
    USERNAME_TELEGRAM = os.getenv('USERNAME_TELEGRAM')
    API_ID_TELEGRAM = os.getenv('API_ID_TELEGRAM')
    API_HASH_TELEGRAM = os.getenv('API_HASH_TELEGRAM')

    FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
    FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')
    RRFTID = os.getenv('RRFTID')
    RRFTSEC = os.getenv('RRFTSEC')

    exchange = ccxt.ftx({
                    'apiKey': RRFTID,
                    'secret': RRFTSEC,
                    'enableRateLimit': True,
                        })

    timezone_offset = +2.0  # Pacific Standard Time (UTC−08:00)
    tzinfo = timezone(timedelta(hours=timezone_offset))
    now = datetime.now(tzinfo)
    print("START:", colored(now.strftime("%d/%m/%Y %H:%M:%S"),'blue'))	

    client = TelegramClient(USERNAME_TELEGRAM, API_ID_TELEGRAM, API_HASH_TELEGRAM) 
    client.start()

    print('trading bot',colored('[ACTIVE]','green')+"\nTelegram client connected with: ",colored(USERNAME_TELEGRAM,'red'))    
    
    # PUBLIC_TEST_CHANNEL FAX SIMILE == freecrypto_signals 
    @client.on(events.NewMessage(chats=PUBLIC_TEST_CHANNEL))
    async def trader_PUBLIC_TEST_CHANNEL(event):
        NEW_MESSAGE = event.message.message
        date = str(datetime.now(tzinfo))
        print('\n',colored('NEW MESSAGE from : ','green'),CHANNEL_1,'\t', date[:-13],'\n\n',NEW_MESSAGE,'\n')
        op_data = message_parser_freecrypto_signals(new_message=NEW_MESSAGE)
        if op_data:
            if op_data['symbol'] in perpetuals:
                trader(order_data=op_data)
    
    with client:
        client.run_until_disconnected()