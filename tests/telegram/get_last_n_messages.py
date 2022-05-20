# TEST OF GETTING TELEGRAM MESSAGES IN REAL TIME
import os
from dotenv import load_dotenv
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon import utils
from telethon.sync import TelegramClient, events
import sys
sys.path.append('../teleryum')
from utils.params import base_operation_data_structure as op_data
from utils.params import project_folder

load_dotenv(os.path.join(project_folder.replace('/tests/telegram',''), '.env'))

TELEGRAM_USERNAME = os.getenv('TELEGRAM_USERNAME')
TELEGRAM_ID = os.getenv('TELEGRAM_ID')
TELEGRAM_HASH = os.getenv('TELEGRAM_HASH')

client = TelegramClient(TELEGRAM_USERNAME, TELEGRAM_ID, TELEGRAM_HASH) 
client.start()

# return n_messages from the channel
n_messages = 10
ID_CHANNEL = 1338521686 # ID = wolfxsignals
print(client.get_messages(PeerChannel(channel_id=ID_CHANNEL), n_messages))
