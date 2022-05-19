import sys
import os
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()
import ccxt

def format_amount(exchange):
    exchange.load_markets()
    symbol = 'BTC/USDT'
    amount = 1.2345678  # amount in base currency BTC
    price = 87654.321  # price in quote currency USDT
    formatted_amount = exchange.amount_to_precision(symbol, amount)
    formatted_price = exchange.price_to_precision(symbol, price)
    print(formatted_amount, formatted_price)

def get_price(ticker = 'ETH-PERP'):
    return exchange.fetchTicker(ticker)['last']   # LAST PRICE

def set_leverage(exchange,leverage_= 0.1, symbol_='ETH-PERP'):
    return exchange.setLeverage(leverage=leverage_, symbol = symbol_, params = {})

def connect_FTX():
    return ccxt.ftx({
                    'enableRateLimit': True,
                        })

price_eth_perp = get_price(ticker='ETH-PERP')
print(price_eth_perp)