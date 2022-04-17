import ccxt
import pandas as pd
import sys
from pprint import pprint
# import logging
# logging.basicConfig(level=logging.DEBUG)

print('python', sys.version)
print('CCXT Version:', ccxt.__version__)

exchange = ccxt.kucoinfutures({
    'adjustForTimeDifference': True,
    "apiKey": '...',
    "secret": '...',
    'password': 'This is you 6-7 digit trading password',
})
# exchange.verbose = True

securities = pd.DataFrame(exchange.load_markets()).transpose()
pprint(securities)

order_response = exchange.createOrder('ADA/USDT:USDT','limit','buy', 1, 1, {'leverage': 10})
pprint(order_response)
