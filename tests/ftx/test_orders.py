import sys
sys.path.insert(0,sys.path[0].replace('bot','') ) #  get tests/client.py
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from client import FtxClient

load_dotenv()

RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')

client = FtxClient(api_key=RRFTID,api_secret=RRFTSEC)


# order = client.place_order(market='XRP-PERP',
#                             side='buy',
#                             price = 0.79,
#                             size = 10,
#                             type = 'limit',
#                             reduce_only = False,
#                             ioc = False,
#                             post_only = False,
#                             client_id = None,
#                             reject_after_ts = None)


TP = client.place_conditional_order(market='XRP-PERP',
                            side='sell',
                            limit_price = 0.89,
                            size = 10,
                            type = 'take_profit',
                            reduce_only = True,
                            trigger_price = 0.801,
                            trail_value = None,
                            cancel = False
                            )

# SL = client.place_conditional_order(market='XRP-PERP',
#                             side='sell',
#                             limit_price = 0.72,
#                             size = 10,
#                             type = 'stop',
#                             reduce_only = True,
#                             trigger_price = 0.69,
#                             trail_value = None,
#                             cancel = False
#                             )

#pprint(order)
print('*'*60)
pprint(TP)
# print('*'*60)
# pprint(SL)

# assert type in ('stop', 'take_profit', 'trailing_stop')

# order = client.place_order(market='SOL-PERP',
#                             side='buy',
#                             price = 80,
#                             size = 0.01,
#                             type = 'limit',
#                             reduce_only = False,
#                             ioc = False,
#                             post_only = False,
#                             client_id = None,
#                             reject_after_ts = None)
