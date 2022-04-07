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

exchange = ccxt.ftx({
                'apiKey': RRFTID,
                'secret': RRFTSEC,
                'enableRateLimit': True,
                    })


order = exchange.create_limit_buy_order('ETH-PERP', 0.001, 3360.00)
print(order)


SL_buy = exchange.create_order(symbol='ETH-PERP', type='stop', side='sell', amount=0.001, price=3280.00, params={'triggerPrice':3380.00,'reduceOnly':True })
print(SL_buy)

TP_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.001, price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True })
print(TP_buy)

