import sys

sys.path.insert(0,sys.path[0].replace('ftx','') )

from client import FtxClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)


print(client.get_conditional_order_history(market='XRPBULL/USDT',side='buy',order_type='limit',
start_time= None, end_time= None))
