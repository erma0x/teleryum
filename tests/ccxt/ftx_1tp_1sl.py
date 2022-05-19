import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint

import ccxt


load_dotenv()
RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')

exchange = ccxt.ftx({
                'apiKey': RRFTID,
                'secret': RRFTSEC,
                'enableRateLimit': True,
                    })



exchange.verbose = True

securities = pd.DataFrame(exchange.load_markets()).transpose()

balance = exchange.fetch_balance()
pprint(balance)


order_response = exchange.create_order(symbol='ADA/USDT:USDT',type='limit',side='buy', amount=1, price=0.7)
pprint(order_response)


order = exchange.create_limit_buy_order(symbol='ADA/USDT:USDT',side='buy', amount=1, price=0.7,)
print(order)


SL_buy = exchange.create_order(symbol='ETH-PERP', type='stop', side='sell', amount=0.001, price=3280.00, params={'triggerPrice':3380.00,'reduceOnly':True })
print(SL_buy)

TP_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.001, price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True })
print(TP_buy)


