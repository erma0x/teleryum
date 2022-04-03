import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from termcolor import colored
from telethon.sync import TelegramClient, events
from channels import *

load_dotenv()
# RRFTID = os.getenv('RRFTID')
# RRFTSEC = os.getenv('RRFTSEC')
# import ccxt
# exchange = ccxt.ftx({
#                 'apiKey': RRFTID,
#                 'secret': RRFTSEC,
#                 'enableRateLimit': True,
#                     })

                    
if __name__ == "__main__":

    now = datetime.now()
    print("START:", colored(now.strftime("%d/%m/%Y %H:%M:%S"),'yellow'))	

    load_dotenv()
    USERNAME_TELEGRAM = os.getenv('USERNAME_TELEGRAM')
    API_ID_TELEGRAM = os.getenv('API_ID_TELEGRAM')
    API_HASH_TELEGRAM = os.getenv('API_HASH_TELEGRAM')

    # connect to telegram client with my.telegram.com API
    client = TelegramClient(USERNAME_TELEGRAM, API_ID_TELEGRAM, API_HASH_TELEGRAM) 
    client.start()
    print('trading-bot',colored('[ACTIVE]','green')+"\nTelegram client connected with: ",colored(USERNAME_TELEGRAM,'yellow'))

# freecrypto_signals FAX SIMILE == PUBLIC_TEST_CHANNEL
    @client.on(events.NewMessage(chats=PUBLIC_TEST_CHANNEL))
    async def trader_PUBLIC_TEST_CHANNEL(event):
        new_message = event.message.message
        TEXT_PATTERNS = ('Sell','Buy','StopLoss')
        for pattern in TEXT_PATTERNS:
            if pattern not in new_message:
                return False
    
        date = str(event.message.date)
        print('NEW SIGNAL from : ',colored(CHANNEL_1,'green'),'\t', date[:-6],new_message)

        # PARSER
        op_data={'side':'','symbol':'','buy':{},'sell':{},'stoploss':''}

        for row in new_message.split('\n'): # TEXT MESSAGE ROWS 
            if '#' in row:
                op_data['symbol'] = row[1:].replace(' ','')

            if row.find('Buy') < row.find('Sell'):
                op_data['side']='Sell'
            else:
                op_data['side']='Buy'

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
                    op_data['sell'] = row.split()[1]

            if 'StopLoss' in row or 'Stoploss' in row :
                op_data['stoploss'] = row.split()[1]

        print(op_data)
    
    with client:
        client.run_until_disconnected()