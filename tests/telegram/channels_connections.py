# TEST OF GETTING TELEGRAM MESSAGES IN REAL TIME
import os
from datetime import datetime

from dotenv import load_dotenv
from termcolor import colored

from telethon.sync import TelegramClient, events

if __name__ == "__main__":

    now = datetime.now()
    print("START:", colored(now.strftime("%d/%m/%Y %H:%M:%S"),'yellow'))	

    load_dotenv()
    USERNAME_TELEGRAM = os.getenv('USERNAME_TELEGRAM')
    API_ID_TELEGRAM = os.getenv('API_ID_TELEGRAM')
    API_HASH_TELEGRAM = os.getenv('API_HASH_TELEGRAM')

    # test channels
    PRIVATE_TEST_CHANNEL = os.getenv('PRIVATE_TEST_CHANNEL')
    PUBLIC_TEST_CHANNEL = os.getenv('PUBLIC_TEST_CHANNEL')
    # channels names
    CHANNEL_1 = os.getenv('CHANNEL_1')
    # connect to telegram client with my.telegram.com API
    client = TelegramClient(USERNAME_TELEGRAM, API_ID_TELEGRAM, API_HASH_TELEGRAM) 
    client.start()

    # cryptohopperofficial 
    @client.on(events.NewMessage(chats=CHANNEL_1))  
    async def trader_CHANNEL_1(event):
        new_message = event.message.message 
        TEXT_PATTERNS = ('Sell','Buy','StopLoss')
        for pattern in TEXT_PATTERNS:
            if pattern not in new_message:   
                return False
        
                date = str(event.message.date)
        print('NEW SIGNAL from : ',colored(CHANNEL_1,'green'),'\t', date[:-6],new_message)


    with client:
        client.run_until_disconnected()