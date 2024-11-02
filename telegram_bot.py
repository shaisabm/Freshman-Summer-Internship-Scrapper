from typing import Final
import os
import json
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_USERNAME: Final = '@freshman_internship_bot'
CHAT_IDS_FILE = "chat_ids.json"

# Load existing chat IDs from a file
def load_chat_ids():
    try:
        with open(CHAT_IDS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return set()

# Save chat IDs to a file
def save_chat_ids():
    with open(CHAT_IDS_FILE, "w") as f:
        json.dump(chat_ids, f)

# Load chat IDs at startup
chat_ids = load_chat_ids()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id not in chat_ids['chat_ids']:
        chat_ids['chat_ids'].append(update.message.chat_id)
    save_chat_ids()  # Save updated chat_ids
    await update.message.reply_text(f"Hello! I will send you updates about internships for freshmen.")

async def send_response(message: str, chat_ids_list: list):
    bot = Bot(token=TOKEN)
    for chat_id in chat_ids_list:
        await bot.send_message(chat_id=chat_id, text=message)  # Use await here

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    print("Bot is running!")
    app.run_polling(poll_interval=3)
