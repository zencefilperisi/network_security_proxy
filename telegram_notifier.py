# telegram_notifier.py
from telegram import Bot
import asyncio

# TOKEN ve CHAT_ID'yi kendi bilgilerinizle değiştirin
API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN" # BotFather'dan aldığın token 
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID" # Sana gelen mesajdaki chat ID

bot = Bot(token=API_TOKEN)

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def notify_telegram(message):
    asyncio.run(send_telegram_message(message))
