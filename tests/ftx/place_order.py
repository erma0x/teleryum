import sys

sys.path.insert(0,sys.path[0].replace('ftx','') )

import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from client import FtxClient

load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)


pprint(client.place_order(market='BTCBULL/USD',side='buy',price=99999,size=1.223 ,type='limit',reduce_only=True,
 ioc = False, post_only = False, client_id = None, reject_after_ts = None))

