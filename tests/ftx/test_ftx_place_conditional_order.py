from client import FtxClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)


order  = client.place_conditional_order( market='BTCBULL/USD', side='buy', size=0.00001, type = 'stop',
        limit_price = None, reduce_only = False, cancel = True,
        trigger_price = None, trail_value = None)
   

print(order)