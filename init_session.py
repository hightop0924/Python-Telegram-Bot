from telethon import TelegramClient, connection
import logging
from telethon import sync, TelegramClient, events
import json

with open('config.json', 'r') as f:
	config = json.loads(f.read())

logging.basicConfig(level=logging.WARNING)

accounts = config['accounts']

folder_session = 'session/'

for account in accounts:
