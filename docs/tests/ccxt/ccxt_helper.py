import ccxt


def init_exchanges(exchange_name='binance'):
    exchange = eval('ccxt.{}()'.format(exchange_name))
    return exchange

def update_exchange_settings(exchange):
    exchange = ccxt.binance ({
        'rateLimit': 10000,  # unified exchange property
        'headers': {
            'YOUR_CUSTOM_HTTP_HEADER': 'YOUR_CUSTOM_VALUE',
        },
        'options': {
            'adjustForTimeDifference': True,  # exchange-specific option
        }
    })
    exchange.options['adjustForTimeDifference'] = False

def enable_sandbox(config,exchange):
    # Python
    exchange = ccxt.binance(config)
    exchange.set_sandbox_mode(True)  # enable sandbox mode


def turn_on_rate_limit():
    # enable built-in rate limiting upon instantiation of the exchange
    exchange = ccxt.bitfinex({
        'enableRateLimit': True,
    })
    # or switch the built-in rate-limiter on or off later after instantiation
    exchange.enableRateLimit = True  # enable
    exchange.enableRateLimit = False  # disable


def format_amount(exchange):
    exchange.load_markets()
    symbol = 'BTC/USDT'
    amount = 1.2345678  # amount in base currency BTC
    price = 87654.321  # price in quote currency USDT
    formatted_amount = exchange.amount_to_precision(symbol, amount)
    formatted_price = exchange.price_to_precision(symbol, price)
    print(formatted_amount, formatted_price)
