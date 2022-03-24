from telethon import TelegramClient, events, sync
import os
from dotenv import load_dotenv

load_dotenv()
MY_USERNAME = os.getenv('USERNAME')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
GROUP_NAME_1 = os.getenv('GROUP_NAME_1')
# GROUP_NAME_2 = os.getenv('GROUP_NAME_2')
# GROUP_NAME_3 = os.getenv('GROUP_NAME_3')
# GROUP_NAME_4 = os.getenv('GROUP_NAME_4')

client = TelegramClient('username', API_ID, API_HASH)
client.start()

for message in client.get_messages(GROUP_NAME_1, limit=1):
    print(message.message)