# TEST OF GETTING TELEGRAM MESSAGES IN REAL TIME
import os
from datetime import datetime
from pprint import pprint

from dotenv import load_dotenv
from termcolor import colored

from telethon.sync import TelegramClient, events

load_dotenv()
TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME')
TELEGRAM_ID = os.getenv('TELEGRAM_ID')
TELEGRAM_HASH = os.getenv('TELEGRAM_HASH')

# test channels
PRIVATE_TEST_CHANNEL = os.getenv('PRIVATE_TEST_CHANNEL')
PUBLIC_TEST_CHANNEL = os.getenv('PUBLIC_TEST_CHANNEL')
# channels names
CHANNEL_1 = os.getenv('CHANNEL_1')
# connect to telegram client with my.telegram.com API
client = TelegramClient(TELEGRAM_USERNAME, TELEGRAM_ID, TELEGRAM_HASH) 
client.start()

#########################################################
# return n_messages from the channel
n_messages = 1

channel_test = 'learn2tradectypto'
print(client.get_messages(channel_test, n_messages))