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

# ENTRY LONG 
order = exchange.create_limit_order(symbol='ADA/USDT:USDT',
                                        side='buy',
                                        amount=2,
                                        price=0.55,
                                        params={'leverage':1,'stop':'down','stopPriceType':'TP','stopPrice':0.6,
                                        'clientOid':'CCSJLINKKS','forceHold':False})
print(order,'\n\n')

# TAKE PROFIT
order = exchange.create_limit_order(symbol='ADA/USDT:USDT',
                                        side='sell',
                                        amount=1,
                                        price=1.4,
                                        params={'leverage':1,'stop':'up','stopPriceType':'TP','stopPrice':1.3,
                                        'clientOid':'CCSJLINKKS','forceHold':False,'reduceOnly':True})
print(order,'\n\n')

# TAKE PROFIT
order = exchange.create_limit_order(symbol='ADA/USDT:USDT',
                                        side='sell',
                                        amount=1,
                                        price=1.5,
                                        params={'leverage':1,'stop':'up','stopPriceType':'TP','stopPrice':1.4,
                                        'clientOid':'CCSJLINKKS','forceHold':False,'reduceOnly':True})
print(order,'\n\n')

# STOP LOSS
order = exchange.create_limit_order(symbol='ADA/USDT:USDT',
                                        side='sell',
                                        amount=1,
                                        price=0.49,
                                        params={'leverage':1,'stop':'down','stopPriceType':'TP','stopPrice':0.52,
                                        'clientOid':'CCSJLINKKS','forceHold':False,'reduceOnly':True})

print(order,'\n\n')


# STOP LOSS
order = exchange.create_limit_order(symbol='ADA/USDT:USDT',
                                        side='sell',
                                        amount=1,
                                        price=0.39,
                                        params={'leverage':1,'stop':'down','stopPriceType':'TP','stopPrice':0.42,
                                        'clientOid':'CCSJLINKKS','forceHold':False,'reduceOnly':True})


print(order,'\n\n')



