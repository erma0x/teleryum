import sys
sys.path.insert(0,sys.path[0].replace('bot','') ) #  get tests/client.py
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from client import FtxClient
load_dotenv()

RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')

import ccxt

def format_amount(exchange):
    exchange.load_markets()
    symbol = 'BTC/USDT'
    amount = 1.2345678  # amount in base currency BTC
    price = 87654.321  # price in quote currency USDT
    formatted_amount = exchange.amount_to_precision(symbol, amount)
    formatted_price = exchange.price_to_precision(symbol, price)
    print(formatted_amount, formatted_price)

exchange = ccxt.ftx({
                'apiKey': RRFTID,
                'secret': RRFTSEC,
                'enableRateLimit': True,
                    })

ticker = 'BTC/USDT'

print(exchange.fetchTicker(ticker)['last'])   # LAST PRICE

# excange.createMarketBuyOrder(ticker, quanto)
# excange.createLimitSellOrder(ticker, quanto, prezo)


# def quanto_in_dollari(ticker, quanto):
#    return quanto/excange.createMarketBuyOrder(ticker)['last']
    
    
# excange.createMarketBuyOrder(ticker, quanto_in_dollari(quanto))