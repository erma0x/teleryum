import sys
sys.path.insert(0,sys.path[0].replace('bot','') ) #  get tests/client.py

import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
import ccxt

load_dotenv()

OKEX_MAIN_READONLY_ID = os.getenv('OKEX_MAIN_READONLY_ID')
OKEX_MAIN_READONLY_HASH = os.getenv('OKEX_MAIN_READONLY_HASH')
OKEX_MAIN_ID = os.getenv('OKEX_MAIN_ID')
OKEX_MAIN_HASH = os.getenv('OKEX_MAIN_HASH')

exchange = ccxt.okex({
            'apiKey': OKEX_MAIN_ID,
            'secret': OKEX_MAIN_HASH,
            'enableRateLimit': True,
                })
                
#order = exchange.market(symbol='BTCUSD')

exchange.accounts()
print( order )

# order = exchange.create_limit_buy_order('ETH-PERP', 0.001, 2200.00)
# print(order)


# SL_buy = exchange.create_order(symbol='ETH-PERP', type='stop', side='sell', amount=0.001, price=3280.00, params={'triggerPrice':3380.00,'reduceOnly':True })
# print(SL_buy)

# TP_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.001, price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True })
# print(TP_buy)


