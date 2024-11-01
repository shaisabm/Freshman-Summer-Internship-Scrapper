import asyncio
from telegram import Bot
from dotenv import load_dotenv
from typing import Final
import os
import json

load_dotenv()


def send_update(message:str):
    TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")

    with open("chat_ids.json", "r") as f:
        chat_ids = json.load(f)['chat_ids']
    bot = Bot(token=TOKEN)

    for chat_id in chat_ids:
        asyncio.run(bot.send_message(chat_id=chat_id, text=message))