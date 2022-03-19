import os
from dotenv import load_dotenv
from termcolor import colored
from datetime import datetime

from telethon.sync import TelegramClient, events

from sqlite_helper import *
from params import NAME_DB

if __name__ == "__main__":

    now = datetime.now()
    print("START:", colored(now.strftime("%d/%m/%Y %H:%M:%S"),'yellow'))	

    create_db(NAME_DB)
    load_dotenv()
    MY_USERNAME = os.getenv('USERNAME')
    API_ID = os.getenv('API_ID')
    API_HASH = os.getenv('API_HASH')

    # channels names
    FATPIG_SIGNALS = os.getenv('FATPIG_SIGNALS')
    CRYPTO_HOPPER_OFFICAIL = os.getenv('CRYPTO_HOPPER_OFFICAIL')
    COIN_SIGNALS_1 = os.getenv('COIN_SIGNALS_1')
    COIN_SIGNALS_2 = os.getenv('COIN_SIGNALS_2')


    PRIVATE_TEST_CHANNEL = os.getenv('PRIVATE_TEST_CHANNEL')
    PUBLIC_TEST_CHANNEL = os.getenv('PUBLIC_TEST_CHANNEL')


    client = TelegramClient(MY_USERNAME, API_ID, API_HASH) # Telegram API 
    client.start()

    print(colored('LISTENER ACTIVE','green')+"\ntelegram client connected with: ",colored(MY_USERNAME,'yellow'),'\ndatabase:\t',colored(NAME_DB,'yellow'))
#___________________________________________________________________________________________________________
    @client.on(events.NewMessage(chats=CHANNEL_1)) # cryptohopperofficial
    async def trader_CHANNEL_1(event):
        new_message = event.message.message 
        TEXT_PATTERNS = ('Sell','Buy','StopLoss')
        for pattern in TEXT_PATTERNS:
            if pattern not in new_message:   
                return False

        op_data={'Side':'','Symbol':'','Buy':{},'Sell':{},'Stoploss':''}      # GENERATE BASE DATA
        print('id message ',id_message,' date ',date,' group ', sender_group)  # PRINT

        for row in text_message.split('\n'): # TEX MESSAGE ROWS 
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

        date = str(event.message.date)
        print('NEW signal from : ',colored(CHANNEL_1,'green'),'\t', date[:-6],new_message)
        #for operation in op_data  
           # traderFTX(operation)

#___________________________________________________________________________________________________________
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

# #___________________________________________________________________________________________________________
#     @client.on(events.NewMessage(chats=GROUP_NAME_4))
#     async def scanner_CoinSignalsgram(event):
#         new_message = event.message.message         
#         TEXT_PATTERNS = ('Enrty','Target','Stop Loss')
#         for pattern in TEXT_PATTERNS:
#             if pattern not in new_message:   
#                 return False

#         date = str(event.message.date)
#         write_message(get_new_id(NAME_DB), date[:-6],GROUP_NAME_2,new_message,NAME_DB)            
#         print("NEW signal from : ",colored(GROUP_NAME_2,'green'),'\t', date[:-6],new_message)
#___________________________________________________________________________________________________________
    with client:
        client.run_until_disconnected()

# @client.on(events.NewMessage(chats=GROUP_NAME_2))
# async def finderCryptoSignalsFree(event):
#     pass
