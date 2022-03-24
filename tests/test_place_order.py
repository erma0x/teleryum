from client import FtxClient
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,
                    api_secret=FTX_API_HASH_READONLY,
                    subaccount_name='Test')

# order = client.get_subaccount_balances(nickname='Test')
# pprint(order)

# order = client.get_total_usd_balance()
# print(order)

############## ORDERS ###########################################

op1 = {'market':'BTCBULL/USD',
            'side':'buy',
            'price':99999,
            'size':1.223,
            'type':'limit',
            'reduce_only':False }

# op_data = {'market':'BTCBULL/USD',
#             'side':'sell',
#             'price':99999,
#             'size':1.223,
#             'type':'limit',
#             'reduce_only':True }

# operations_data=[op1,op2]

################## PLACE ORDERS #######################################

order = client.place_order(market=op_data['market'],
                            side=op_data['side'],
                            price=op_data['price'],
                            size=op_data['size'] ,
                            type=op_data['type'],
                            reduce_only=op_data['reduce_only'],
                            ioc = False,
                            post_only = False,
                            client_id = None,
                            reject_after_ts = None)

pprint(order)


# order  = client.place_conditional_order( market='BTCBULL/USD', side='buy', size=0.00001, type = 'stop',
#         limit_price = None, reduce_only = False, cancel = True,
#         trigger_price = None, trail_value = None)

# pprint(client.modify_order(existing_order_id = None,
#     existing_client_order_id = None,
#     price = None,
#     client_order_id = None, 
#     size = None))

# print(client.cancel_order(order_id='21422222'))

# pprint(client.get_trades(market='BTCBULL/USD',start_time = None, end_time = None))
