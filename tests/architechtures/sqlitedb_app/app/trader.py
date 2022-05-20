import time
import sys
import pprint
from dotenv import load_dotenv
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import ccxt
import ccxt.async_support as ccxt  # noqa: E402

from utils.params import *
from sqlite_helper import *


class WatchDogTrader:
   
    watchDirectory = sys.path[0].replace('/app',"/"+NAME_DB) # Set the directory on watch

    print('\nTRADER ACTIVE\ndatabase: ',watchDirectory)
  
    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        trade_system = TradeSystem()
        self.observer.schedule(trade_system, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
  
  
class TradeSystem(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        if event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event\n % s. \n" % event.src_path)            
            cryptohopperofficial()
            

def cryptohopperofficial():
    """
    Parser + Trader
    when db changes connect to it and get last 
    operations not placed, and if the group is cryptosignalsfree
    use this function for place orders 
    for operation in get_all_messages(NAME_DB):
        if operation = 'not placed' and sender == 'cryptosignalsfree':
            parse and lunch operations
    Output
        Symbol:
        Laverage:
        Buy: float or  Buy: {1:float,2: ...}
        Sell: float or  Sell: {1:float,2: ...}
        StopLoss:

    """
    data = get_all_messages(NAME_DB)

    for index in range(len(data)):
    # GET DATA FROM DB 
        operation = data[index]
        id_message = operation[0]
        date = operation[1]
        sender_group = operation[2]
        text_message = operation[3]
        operation_placed = operation[4]
        
   # CONDITION 
   # IF the message sended from the is right sender and the operation is not placed   
        if sender_group == 'cryptohopperofficial' and operation_placed=='false':

            operation_data={'Side':'','Symbol':'','Buy':{},'Sell':{},'Stoploss':''}      # GENERATE BASE DATA
            
            print('id message ',id_message,' date ',date,' group ', sender_group)  # PRINT


  # PARSE DATA and EXTRACT TRADING OPERATION DATA            
            for info_op in text_message.split('\n'): # TEX MESSAGE ROWS 

                if '#' in info_op:
                    operation_data['Symbol'] = info_op[1:].replace(' ','')

                if info_op.find('Buy') < info_op.find('Sell'):
                    operation_data['Side']='Sell'
                else:
                    operation_data['Side']='Buy'

                if 'Buy' in info_op:
                    if '-' in info_op.split()[1]:
                        temp=info_op.split()[1].split('-')
                        for num in range(len(temp)):
                            operation_data['Buy'][num] = temp[num]

                    else:
                        operation_data['Buy'] = info_op.split()[1]
                
                if 'Sell' in info_op:
                    if '-' in info_op.split()[1]:
                        temp=info_op.split()[1].split('-')
                        for num in range(len(temp)):
                            operation_data['Sell'][num] = temp[num]

                    else:
                        operation_data['Sell'] = info_op.split()[1]

                if 'StopLoss' in info_op or 'Stoploss' in info_op :
                    operation_data['Stoploss'] = info_op.split()[1]

            print(operation_data)
            
            # exchange = ccxt.binance({'enableRateLimit': True})
            # exchange.set_sandbox_mode(True)



#############################################################################################
async def main(asyncio_loop):
    exchange = ccxt.binance({
        'asyncio_loop': asyncio_loop,
        'enableRateLimit': True,
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET',
        # 'verbose': True,  # for debug output
    })
    try:
        # change the values here
        symbol = 'BTC/USDT'
        price = 9000
        amount = 1
        type = 'limit'  # or market
        side = 'buy'
        order = await exchange.create_order(symbol, type, side, amount, price, {
            'type': 'margin',
        })
        pprint(order)

    except ccxt.InsufficientFunds as e:
        print('create_order() failed – not enough funds')
        print(e)
    except Exception as e:
        print('create_order() failed')
        print(e)
    await exchange.close()

if __name__ == '__main__':
    asyncio_loop = asyncio.get_event_loop()
    asyncio_loop.run_until_complete(main(asyncio_loop))
#############################################################################################


def enable_sandbox(exchange,config):
    # Python
    exchange = ccxt.binance(config)
    exchange.set_sandbox_mode(True)  # enable sandbox mode


def turn_on_rate_limit(exchange):
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


def order_balancer(operation_data):
	"""
	from json data information
	into multiple single operations
	that cover the same strategy
	Buy Sell
	1,1
	1,+
	+,1
	+,+

	side: both
	"""
	#  order_id = client.create_limit_order('XBTUSDM', 'buy', '1', '30', '8600')
	


# GET api keys
      #      load_dotenv()
        #    api_key = os.getenv('API_KEY')
         #   api_secret = os.getenv('API_SECRET')
          #  api_passphrase = os.getenv('API_PASSPHRASE')

# POST order
       #     from kucoin_futures.client import Trade
    #        client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=True, url=URL_SANDBOX)
          #  order_id = client.create_limit_order('XBTUSDM', 'buy', '1', '30', '8600')
          #  print('MY ORDER ID : ',order_id)

            #client = Client(api_key, api_secret, api_passphrase)
            #currencies = client.get_currencies()
            #order_id = client.create_limit_order('XBTUSDM', 'buy', '1', '30', '8600')

            # server_time = client.get_server_timestamp()
            # print('SERVER TIME ',server_time)
            
            # TRADING 
            # client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=True, url=URL_SANDBOX)
            # order_id = client.create_limit_order('XBTUSDM', 'buy', '1', '30', '8600')
            # client.cancel_order(order_id)
            
            # orders = client.get_active_orders('KCS-BTC')


if __name__ == '__main__':
    watch = WatchDogTrader()
    watch.run()
