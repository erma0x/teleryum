import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient, events

load_dotenv()
USERNAME_TELEGRAM = os.getenv('TELEGRAM_USERNAME')
API_ID_TELEGRAM = os.getenv('TELEGRAM_ID')
API_HASH_TELEGRAM = os.getenv('TELEGRAM_HASH')

client = TelegramClient(USERNAME_TELEGRAM, API_ID_TELEGRAM, API_HASH_TELEGRAM) 
client.start()

for dialog in client.iter_dialogs():
    print(f'{dialog.id}:{dialog.title}')