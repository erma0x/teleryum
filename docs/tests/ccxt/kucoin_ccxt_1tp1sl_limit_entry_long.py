import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
import ccxt

load_dotenv()

KUCOIN_MAIN_KEY = os.getenv('KUCOIN_MAIN_KEY')
KUCOIN_MAIN_SECRET = os.getenv('KUCOIN_MAIN_SECRET')
KUCOIN_MAIN_PASS = os.getenv('KUCOIN_MAIN_PASS')

exchange = ccxt.kucoinfutures({
    'adjustForTimeDifference': True,
    "apiKey": KUCOIN_MAIN_KEY,
    "secret": KUCOIN_MAIN_SECRET,
    'password': KUCOIN_MAIN_PASS,
})

#exchange.verbose = True


def setTp(exchange_, symbol: str, side: str, size: int, tp: float):
    params = dict(reduceOnly=True)
    side = 'sell' if side=='buy' else 'buy'
    try:
        res = exchange_.create_order(symbol, 'limit', side, size, price=tp, params=params)
        return res
    except Exception as e:
        print(e)


# order = exchange.create_limit_order(symbol='ADA/USDT:USDT',side='buy', amount=1, price=0.7,params={'leverage':1})
# print(order)

# print('*'*80)

order = exchange.create_limit_order(symbol='ADA/USDT:USDT',side='buy', amount=1, price=0.7,params={'leverage':1})
print(order)

# TP_buy = exchange.create_order(symbol='ADA/USDT:USDT',type='limit',side='sell', amount=1, price=1.3, params={'reduceOnly':True})
# print(TP_buy)

# TP_buy = setTp(exchange_=exchange, symbol = 'ADA/USDT:USDT', side = 'sell', size = 1 , tp = 1.3)
# # print(TP_buy)


# SL_buy = exchange.create_limit_order(symbol='ADA/USDT:USDT',side='sell', amount=1, price=0.6, params={'reduceOnly':True,'leverage':1 })
# print(SL_buy)


