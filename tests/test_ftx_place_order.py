from client import FtxClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

FTX_API_ID_READONLY = os.getenv('FTX_API_ID_READONLY')
FTX_API_HASH_READONLY = os.getenv('FTX_API_HASH_READONLY')

client = FtxClient(api_key=FTX_API_ID_READONLY,api_secret=FTX_API_HASH_READONLY)


print(client.place_order(market='BTCBULL/USD',side='buy',price=99999,size=1.223 ,type='limit',reduce_only=True,
 ioc = False, post_only = False, client_id = None, reject_after_ts = None))

