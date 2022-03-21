#  Copyright (C) Ermano Buikis - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ermano Buikis ermano.buikis.com, March 2022

import os
from datetime import datetime

from dotenv import load_dotenv
from termcolor import colored

from telethon.sync import TelegramClient, events

from params import *

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

    print('SCANNER',colored('[ACTIVE]','green')+"\nTelegram client connected with: ",colored(USERNAME_TELEGRAM,'yellow'))

##### freecrypto_signals ##################################################################################################################################
    @client.on(events.NewMessage(chats=CHANNEL_1))
    async def trader_CHANNEL_1(event):
        new_message = event.message.message
        TEXT_PATTERNS = ('Sell','Buy','StopLoss')
        for pattern in TEXT_PATTERNS:
            if pattern not in new_message:
                return False
    
        date = str(event.message.date)
        print('NEW SIGNAL from : ',colored(CHANNEL_1,'green'),'\t', date[:-6],new_message)

        # PARSER
        op_data={'side':'','symbol':'','buy':{},'sell':{},'stoploss':''}

        for row in text_message.split('\n'): # TEXT MESSAGE ROWS 
            if '#' in row:
                op_data['Symbol'] = row[1:].replace(' ','')

            if row.find('Buy') < row.find('Sell'):
                op_data['Side']='Sell'
            else:
                op_data['Side']='Buy'

            if 'Buy' in row:
                if '-' in row.split()[1]:
                    temp = row.split()[1].split('-')
                    for n in range(len(temp)):
                        op_data['Buy'][n] = temp[n]
                else:
                    op_data['Buy'] = row.split()[1]
            if 'Sell' in row:
                if '-' in row.split()[1]:
                    temp=row.split()[1].split('-')
                    for n in range(len(temp)):
                        op_data['Sell'][n] = temp[n]
                else:
                    op_data['Sell'] = row.split()[1]

            if 'StopLoss' in row or 'Stoploss' in row :
                op_data['Stoploss'] = row.split()[1]

            print(op_data)

        # TRADER
        #for operation in op_data  
           # traderFTX(operation)

##### cryptohopperofficial ##################################################################################################################################
#     @client.on(events.NewMessage(chats=GROUP_NAME_2))
#     async def scanner_Coin_Signals(event):
#         new_message = event.message.message         
#         TEXT_PATTERNS = ('Enrty','Target','Stoploss','Leverage')
#         for pattern in TEXT_PATTERNS:
#             if pattern not in new_message:   
#                 return False

#         date = str(event.message.date)
#         write_message(get_new_id(NAME_DB), date[:-6],GROUP_NAME_2,new_message,NAME_DB)            
#         print("NEW signal from : ",colored(GROUP_NAME_2,'green'),'\t', date[:-6],new_message)
# #___________________________________________________________________________________________________________
#     @client.on(events.NewMessage(chats=GROUP_NAME_3))
#     async def scanner_FatpigsSignals(event):
#         new_message = event.message.message         
#         TEXT_PATTERNS = ('Enrty','#','/','Stop Loss','Target','Leverage')
#         for pattern in TEXT_PATTERNS:
#             if pattern not in new_message:   
#                 return False

#         date = str(event.message.date)
#         write_message(get_new_id(NAME_DB), date[:-6],GROUP_NAME_2,new_message,NAME_DB)            
#         print("NEW signal from : ",colored(GROUP_NAME_2,'green'),'\t', date[:-6],new_message)

#     @client.on(events.NewMessage(chats=PUBLIC_TEST_CHANNEL))
#     async def scanner_PUBLIC_TEST_CHANNEL(event):
#         new_message = event.message.message         
#         TEXT_PATTERNS = ('Enrty','Target','Stop Loss')
#         for pattern in TEXT_PATTERNS:
#             if pattern not in new_message:   
#                 return False

#         date = str(event.message.date)
#         write_message(get_new_id(NAME_DB), date[:-6],GROUP_NAME_2,new_message,NAME_DB)            
#         print("NEW signal from : ",colored(GROUP_NAME_2,'green'),'\t', date[:-6],new_message)

    with client:
        client.run_until_disconnected()