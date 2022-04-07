import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from termcolor import colored
from telethon.sync import TelegramClient, events
import ccxt

from trader_teleryum import *
from params import *
from perpetuals_ftx import perpetuals

                   
if __name__ == "__main__":
    load_dotenv()
    RRFTID = os.getenv('RRFTID')
    RRFTSEC = os.getenv('RRFTSEC')
    exchange = ccxt.ftx({
                    'apiKey': RRFTID,
                    'secret': RRFTSEC,
                    'enableRateLimit': True,
                        })
                        
    now = datetime.now()
    print("START:", colored(now.strftime("%d/%m/%Y %H:%M:%S"),'blue'))	

    load_dotenv()
    USERNAME_TELEGRAM = os.getenv('USERNAME_TELEGRAM')
    API_ID_TELEGRAM = os.getenv('API_ID_TELEGRAM')
    API_HASH_TELEGRAM = os.getenv('API_HASH_TELEGRAM')

    # connect to telegram client with my.telegram.com API
    client = TelegramClient(USERNAME_TELEGRAM, API_ID_TELEGRAM, API_HASH_TELEGRAM) 
    client.start()
    print('trading-bot',colored('[ACTIVE]','green')+"\nTelegram client connected with: ",colored(USERNAME_TELEGRAM,'red'))
    
    # PUBLIC_TEST_CHANNEL FAX SIMILE == freecrypto_signals 
    @client.on(events.NewMessage(chats=PUBLIC_TEST_CHANNEL))
    async def trader_PUBLIC_TEST_CHANNEL(event):
        NEW_MESSAGE = event.message.message
        date = str(event.message.date)
        print(colored('NEW MESSAGE from : ','green'),CHANNEL_1,'\t', date[:-6],'\n\n',NEW_MESSAGE)
        print('_'*40)
        op_data = message_parser_freecrypto_signals(new_message=NEW_MESSAGE)
        if op_data:
            if op_data['symbol'] in perpetuals:
                trader(order_data=op_data)
    
    with client:
        client.run_until_disconnected()