import sys
import os
import time
import socket
import math

from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+2.0))

from pprint import pprint
from copy import deepcopy

from termcolor import colored
from dotenv import load_dotenv

import asyncio
from telethon import TelegramClient, events

sys.path.append('../teleryum')
from utils.params import base_operation_data_structure as op_data
from utils.params import project_folder
from utils.params import PRIVATE_TEST_CHANNEL

def parser_wolfxsignals(text_message):

    TEXT_PATTERNS = ('/','TP','SL','️Leverage','x')

    for pattern in TEXT_PATTERNS:
        if pattern not in text_message:
            return False

    date = str(datetime.now())
    for row in text_message.split('\n'):
        if '/' in row:
            op_data['symbol'] = row[1:].split('/')[0]#.replace(' ','').replace('#','')

        if row.find('SELL'):
            op_data['side']='short'

        if row.find('BUY'):
            op_data['side']='buy'

        if op_data['side']:
            if 'TP' in row:
                temp = row.split()[1].split(' ')
                temp_list = []
                for n in range(len(temp)):
                    temp_list.append(temp[n])
                
                op_data['take_profits'] = temp_list

            if 'SL' in row:
                temp = row.split()[1].split(' ')
                temp_list = []
                for n in range(len(temp)):
                    temp_list.append(temp[n])

                op_data['stop_losses']= temp_list

            if 'Enter' in row:
                temp=''.join(row.split(' ')[2]).split('-')
                list_entry_prices = []
                for i in temp:
                    list_entry_prices.append(i)
                
                op_data['entry_prices'] = list_entry_prices

        if 'Leverage' in row:
            op_data['laverage']  = row.split()[1].replace('x','')

    return(op_data)


async def main():      
    load_dotenv(os.path.join(project_folder.replace('/tests',''), '.env'))

    TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME')
    TELEGRAM_ID = os.getenv('TELEGRAM_ID')
    TELEGRAM_HASH = os.getenv('TELEGRAM_HASH')
    print('\n\n',project_folder,TELEGRAM_ID)
    client = TelegramClient(TELEGRAM_USERNAME, TELEGRAM_ID, TELEGRAM_HASH) 

    while True:
        @client.on(events.NewMessage( chats = PRIVATE_TEST_CHANNEL ))
        async def trader_PRIVATE_TEST_CHANNEL( event ):
            NEW_MESSAGE = event.message.message
            signal = parser_wolfxsignals(NEW_MESSAGE)
            if signal:
                print(f'message = {NEW_MESSAGE} \n\n')

        async with client:        
            if client.is_connected():
                await client.run_until_disconnected() 
                #await client.loop.run_until_complete() 
            else:
                await client.start()   


if __name__ == "__main__":

    load_dotenv(os.path.join(project_folder, '.env'))
    asyncio.run(main())
