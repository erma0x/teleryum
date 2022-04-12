import sys

sys.path.insert(0,sys.path[0].replace('ftx','') )

from client import FtxClient
import os
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')

client = FtxClient(api_key=RRFTID,api_secret=RRFTSEC)

order  = client.place_conditional_order( market='SOL-PERP', side='sell', size=0.1, type = 'stop',
        limit_price = 100.902, reduce_only = False, cancel = False,
        trigger_price =  105.902, trail_value = None)

pprint(order)