import sys
import os
import time
import socket
import math

from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+2.0))

from pprint import pprint
from copy import deepcopy

from termcolor import colored
from dotenv import load_dotenv

import asyncio
from telethon import TelegramClient, events

import ccxt

from ftx.client import FtxClient
from ftx.ftx_perpetuals import ftx_perpetuals

from kucoin.utils import *
from kucoin.contracts import kucoinfutures_contract_size

from utils.channels import *
from utils_bot.params import *
from utils_bot.printer import *

from parsers.parser_wolfxsignals import *

def opposite(type_order):
    if type_order=='buy':
        return 'sell'
    return 'buy'

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


async def trader_kucoinfutures(order_data, exchange, maintenance_capital =0.05):
    '''
    get aviable balance
    get minimal order
    rebalance with a multiple of the minimal order
    '''

    order_data = string_to_float_prices(op_data_structure=order_data)
    order_data = sort_orders(op_data_structure=order_data)
    
    amount_usd_position = await get_amount_position_usdt_kucoinfutures()

    if print_op: print('position in usdt $ ',amount_usd_position,'leverage ',order_data['leverage'])

    n_entry_prices = len(order_data['entry_prices'])
    n_take_profits = len(order_data['take_profits'])
    n_stop_losses = len(order_data['stop_losses'])

    if get_free_balance(exchange) < (1+maintenance_capital) * amount_usd_position:
        return None

    for i in range(len(order_data['entry_prices'])): 
        
        entry_price = deepcopy(order_data['entry_prices'][i])

        # amount_token_position = round( amount_usd_position / n_entry_prices / entry_price , 8 )
        	
        	# TO FIX
        amount_token_position = 2 ############################################


        if print_op: print('amount_token_position ',amount_token_position)      
        
        # ENTRY LONG 
        entry_order = exchange.create_limit_order(symbol=order_data['symbol'],
                                                    side=order_data['side'],
                                                    amount=amount_token_position,
                                                    price=entry_price,
                                                    params={'leverage':order_data['leverage'], # TRIGGER PRICE #,'stop':'down','stopPriceType':'TP','stopPrice':entry_price,
                                                                'forceHold':False})
                                                                
        # TAKE PROFIT 
        take_profit_quantities = balance_kucoinfutures_contract_quantity(order_data['take_profits'], amount_token_position)        
        if print_op: print('take_profit_quantities ',take_profit_quantities)
        for j in range(len(order_data['take_profits'])):
            order = exchange.create_limit_order(symbol=order_data['symbol'],
                                                side=opposite(order_data['side']),
                                                amount=take_profit_quantities[j],
                                                price=order_data['take_profits'][j],
                                                params={'leverage':order_data['leverage'],'reduceOnly':True,
                                                'stop':kucoin_side(side=order_data['side'],trigger='TAKEPROFIT'),'stopPriceType':'TP','stopPrice':order_data['take_profits'][j]})


        # STOP LOSS
        stop_loss_quantities = balance_kucoinfutures_contract_quantity(order_data['stop_losses'], amount_token_position)
        if print_op: print('stop_loss_quantities ',stop_loss_quantities)
        for k in range(len(order_data['stop_losses'])):
            order = exchange.create_limit_order(symbol=order_data['symbol'],
                                                side=opposite(order_data['side']),
                                                amount=stop_loss_quantities[k],
                                                price=order_data['stop_losses'][k],
                                                params={'leverage':order_data['leverage'],'reduceOnly':True
                                                ,'stop':kucoin_side(side=order_data['side'],trigger='STOPLOSS'),'stopPriceType':'TP','stopPrice':order_data['stop_losses'][k],
                                                'forceHold':False})


async def trader_ftx(order_data, exchange,maintenance_capital =0.05):

    order_data = string_to_float_prices(op_data_structure=order_data)
    order_data = sort_orders(op_data_structure=order_data)
    
    amount_usd_position = await get_amount_position_usdt_ftx()

    if print_op: print('position in usdt $ ',amount_usd_position,'real LEVERAGE on FTX: 2 ')

    n_entry_prices = len(order_data['entry_prices'])
    n_take_profits = len(order_data['take_profits'])
    n_stop_losses = len(order_data['stop_losses'])

    if get_free_balance_ftx() < (1+maintenance_capital) * amount_usd_position:
        return None

    for i in range(len(order_data['entry_prices'])): 
        
        entry_price = deepcopy(order_data['entry_prices'][i])
        amount_token_position = round( amount_usd_position / n_entry_prices / entry_price , 8 )

        # ENTRY LONG
        if print_op: print('amount_token_position ',amount_token_position)      
        entry_order = exchange.create_limit_order(symbol = order_data['symbol'],
                                                side = order_data['side'],
                                                amount = amount_token_position,
                                                price = entry_price)

        # TAKE PROFIT 
        take_profit_quantities = balance_trigger_orders_quantity(order_data['take_profits'], amount_token_position)        
        if print_op: print('take_profit_quantities ',take_profit_quantities)
        for j in range(len(order_data['take_profits'])):
            take_profit_order = exchange.create_order(symbol = order_data['symbol'],
                                                    type = 'takeProfit',
                                                    side = opposite(order_data['side']),
                                                    amount = take_profit_quantities[j] ,
                                                    price = order_data['take_profits'][j],
                                                    params = {'triggerPrice':order_data['take_profits'][j],'reduceOnly':True })
        # STOP LOSS
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
    """
    ranking exchange from the hieghst leverage to the least
    and open operation if free balance avaiable    
    """

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


    KUCOIN_MAIN_KEY = os.getenv('KUCOIN_MAIN_KEY')
    KUCOIN_MAIN_SECRET = os.getenv('KUCOIN_MAIN_SECRET')
    KUCOIN_MAIN_PASS = os.getenv('KUCOIN_MAIN_PASS')

    kucoinfutures_main = ccxt.kucoinfutures({
        'adjustForTimeDifference': True,
        "apiKey": KUCOIN_MAIN_KEY,
        "secret": KUCOIN_MAIN_SECRET,
        'password': KUCOIN_MAIN_PASS,
    })

    await trader_kucoinfutures( order_data = op_data , exchange = kucoinfutures_main)

    # if channel in (1,'1'):
    #     if op_data['symbol'] in kucoin_perpetuals:
    #         await trader_kucoinfutures( order_data = op_data , exchange = kucoinfutures_main)

    #     # elif op_data['symbol'] in kraken_perpetuals:
    #     #     await trader_kraken( order_data = op_data , exchange = kraken_c1 )     

    #     elif op_data['symbol'] in ftx_perpetuals:
    #         await trader_ftx( order_data = op_data , exchange = ftx_c1 )     
    #     else:
    #         print('OPERATION UNSUCCESFUL: no ticker found    channel: ',channel)

    # if channel in (2,'2'):
    #     if op_data['symbol'] in kucoin_perpetuals:
    #         await trader_kucoinfutures( order_data = op_data , exchange = kucoinfutures_main)

    #     # elif op_data['symbol'] in kraken_perpetuals:
    #     #     await trader_kraken( order_data = op_data , exchange = kraken_c1 )     

    #     elif op_data['symbol'] in ftx_perpetuals:
    #         await trader_ftx( order_data = op_data , exchange = ftx_c1 )     
    #     else:
    #         print('OPERATION UNSUCCESFUL: no ticker found    channel: ',channel)


async def main():      
    load_dotenv()

    TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME')
    TELEGRAM_ID = os.getenv('TELEGRAM_ID')
    TELEGRAM_HASH = os.getenv('TELEGRAM_HASH')

    client = TelegramClient(TELEGRAM_USERNAME, TELEGRAM_ID, TELEGRAM_HASH) 

    if print_op: print_start()

    while True:
        # t.me/test_channel_pubblico_24991204  
        @client.on(events.NewMessage( chats =  ))
        async def trader_PUBLIC_TEST_CHANNEL( event ):
            NEW_MESSAGE = event.message.message
            signal = parser_c1( new_message = NEW_MESSAGE)
            if signal:
                print_message( message = NEW_MESSAGE, channel = wolfxsignals )
                await deamon_trader(op_data = signal, channel = 1)

        # # t.me/freecrypto_signals 
        # @client.on(events.NewMessage( chats = CHANNEL_1 ))
        # async def trader_CHANNEL_1( event ):
        #     NEW_MESSAGE = event.message.message
        #     signal = parser_CHANNEL_1( new_message = NEW_MESSAGE)
        #     if signal:
        #         print_message( message = NEW_MESSAGE, channel = CHANNEL_1 )
        #         # await global_trader()

        await asyncio.sleep(1)

        async with client:        
            if client.is_connected():
                await client.run_until_disconnected() 
                #await client.loop.run_until_complete() 
            else:
                await client.start()           


if __name__ == "__main__":

    load_dotenv()
    FTX_READONLY_C1 = os.getenv('FTX_READONLY_C1')
    FTX_READONLY_C1_HASH = os.getenv('FTX_READONLY_C1_HASH')

    asyncio.run(main())
