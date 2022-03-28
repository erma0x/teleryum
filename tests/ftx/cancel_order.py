import sys

sys.path.insert(0,sys.path[0].replace('ftx','') )

import os
from datetime import datetime
from dotenv import load_dotenv
from client import FtxClient

load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)

print(client.cancel_order(order_id='21422222'))