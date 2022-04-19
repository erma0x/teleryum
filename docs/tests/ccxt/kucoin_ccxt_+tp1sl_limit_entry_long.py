import sys
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


order = exchange.create_limit_buy_order('ETH-PERP', 0.01, 3360.00)
print(order)


SL_buy = exchange.create_order(symbol='ETH-PERP', type='stop', side='sell', amount=0.01, price=3280.00, params={'triggerPrice':3380.00,'reduceOnly':True,'leverage':1 })
print(SL_buy)

TP1_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True,'leverage':1 })
print(TP1_buy)

TP2_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3700.00, params={'triggerPrice':3500.00,'reduceOnly':True,'leverage':1 })
print(TP2_buy)

TP3_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3800.00, params={'triggerPrice':3500.00,'reduceOnly':True,'leverage':1 })
print(TP3_buy)

TP4_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3900.00, params={'triggerPrice':3500.00,'reduceOnly':True,'leverage':1 })
print(TP4_buy)