import sys
sys.path.insert(0,sys.path[0].replace('bot','') ) #  get tests/client.py

import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()
RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')
import ccxt

OKEX_READONLY = os.getenv('FTX_READONLY')
OKEX_READONLY_HASH = os.getenv('FTX_READONLY_HASH')
OKEX_API_MAIN = os.getenv('FTX_API_MAIN')
OKEX_API_MAIN_HASH = os.getenv('FTX_API_MAIN_HASH')

exchange = ccxt.okex({
            'apiKey': OKEX_API_MAIN,
            'secret': OKEX_API_MAIN_HASH,
            'enableRateLimit': True,
                })


order = exchange.create_limit_buy_order('ETH-PERP', 0.001, 3360.00)
print(order)


# SL_buy = exchange.create_order(symbol='ETH-PERP', type='stop', side='sell', amount=0.001, price=3280.00, params={'triggerPrice':3380.00,'reduceOnly':True })
# print(SL_buy)

# TP_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.001, price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True })
# print(TP_buy)


