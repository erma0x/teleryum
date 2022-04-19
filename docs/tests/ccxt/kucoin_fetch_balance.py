import sys

#print(sys.path[0])
#print(sys.path[0].replace('docs/tests/ccxt',''))
sys.path.insert(0,sys.path[0].replace('docs/tests/ccxt','') )

import os
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv
import ccxt

# import logging
# logging.basicConfig(level=logging.DEBUG)

print('python', sys.version)
print('CCXT Version:', ccxt.__version__)



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
exchange.verbose = True


securities = pd.DataFrame(exchange.load_markets()).transpose()

print('-'*80,'\n\t MY BALANCE')
balance = exchange.fetch_balance()
pprint(balance)


# order_response = exchange.create_order(symbol='ADA/USDT:USDT',type='limit',side='buy', amount=1, price=0.7, params={'leverage': 1})
# pprint(order_response)