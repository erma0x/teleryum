import sys

sys.path.insert(0,sys.path[0].replace('ftx','') )

import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from client import FtxClient

load_dotenv()

RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')

client = FtxClient(api_key=RRFTID,api_secret=RRFTSEC)

order = client.place_order(market='SOL-PERP',side='sell', price=100.01, size=0.1 ,type='limit',
                            reduce_only=True,
                            ioc = False,
                            post_only = False,
                            client_id = 1,
                            reject_after_ts = None)
pprint(order)