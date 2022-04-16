import os
from datetime import datetime
from dotenv import load_dotenv
from termcolor import colored
from test_params import *

# freecrypto_signals

message1 = """
#FOR 
Buy 99-96
Sell 102-105-110-125
StopLoss 85
By (@SN_crypto)
"""
message2 = """
#DIA at (Binance, Kucoin)
Buy 2382-2310
Sell 2425-2470-2640-3050
StopLoss 2000
By (@SN_crypto)
"""
message3 = """
#CVX/BTC 
Buy 4367-4525
Sell  4616-4725-4955-5689-6889-9543
Stoploss 3799
By (@SN_crypto)

"""
messages = [message1,message2,message3]

op_data={'side':'','market':'','buy':{},'sell':{},'stoploss':{}}

op1 = {'market':'BTCBULL/USD',
            'side':'buy',
            'price':99999,
            'size':1.223,
            'type':'limit',
            'reduce_only':False
      }

def bot_freecrypto_signals(text_message):

    TEXT_PATTERNS = ('Sell','Buy','#')

    for pattern in TEXT_PATTERNS:
        if pattern not in text_message:
            return False

    date = str(datetime.now())
    #print('NEW SIGNAL from : ',colored(CHANNEL_1,'green'),'\t', date[:-6],text_message)

    for row in text_message.split('\n'): # TEXT MESSAGE ROWS 
        if '#' in row:
            op_data['market'] = row[1:].split(' ')[0]#.replace(' ','').replace('#','')

        if row.find('Buy') < row.find('Sell'):
            op_data['side']='short'
        else:
            op_data['side']='long'

        if 'Buy' in row:
            if '-' in row.split()[1]:
                temp = row.split()[1].split('-')
                for n in range(len(temp)):
                    op_data['buy'][n] = temp[n]
            else:
                op_data['buy'] = row.split()[1]
        if 'Sell' in row:
            if '-' in row.split()[1]:
                temp=row.split()[1].split('-')
                for n in range(len(temp)):
                    op_data['sell'][n] = temp[n]
            else:
                op_data['Sell'] = row.split()[1]

        if 'StopLoss' in row or 'Stoploss' in row :
            op_data['stoploss'] = row.split()[1]

    print('op ',op_data,'\n')

for message in messages:
    bot_freecrypto_signals(text_message=message)

    # TRADER
    # for operation in op_data  
        # traderFTX(operation)