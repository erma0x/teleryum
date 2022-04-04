import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint

import ccxt
from client import FtxClient

load_dotenv()
RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

exchange = ccxt.ftx({
                'apiKey': RRFTID,
                'secret': RRFTSEC,
                'enableRateLimit': True,
                    })

ORDER_DATA = {'side': 'buy', 'symbol': 'ETH-PERP', 'take_profits': ['805', '820', '878', '1100'], 'entry_prices': ['2900', '3300'], 'stop_losses': ['670']}

def opposite(type_order):
    if type_order=='buy':
        return 'sell'
    return 'buy'


def calculate_amount_for_operation():
    client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)
    order = client.get_balances()[0]['free']
    pprint('your FREE balance: '+round(order,2))
    return order


def trader(order_data):
    operation_balance = calculate_amount_for_operation()
    for entry_price in order_data['entry_prices']:
        n_entry_prices = ORDER_DATA['entry_prices']
        entry_order = exchange.create_limit_order(symbol=order_data['symbol'],
                                                 side=order_data['side'],
                                                 amount=round(operation_balance/n_entry_prices,6),
                                                 price=float(entry_price))

    for take_profit in order_data['take_profits']:
        n_take_profits = ORDER_DATA['take_profits']
        take_profit_order = exchange.create_order(symbol=order_data['symbol'],
                                                side=opposite(order_data['side']),
                                                amount=round(operation_balance/n_take_profits,6),
                                                price=float(take_profit),
                                                params={'triggerPrice':float(take_profit),'reduceOnly':True })

    for stop_loss in ORDER_DATA['stop_losses']:
        n_stop_losses = ORDER_DATA['stop_losses']
        stop_loss_order = exchange.create_order(symbol=order_data['symbol'],
                                                side=opposite(order_data['side']),
                                                amount=round(operation_balance/n_stop_losses,6),
                                                price=float(stop_loss),
                                                params={'triggerPrice':float(stop_loss),'reduceOnly':True })

trader(order_data=ORDER_DATA)