import os
from datetime import datetime
from dotenv import load_dotenv
import sys

sys.path.insert(0,sys.path[0].replace('ftx','') )

from client import FtxClient
load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)

order = client.get_trigger_order_history(market = None)
print(order)


