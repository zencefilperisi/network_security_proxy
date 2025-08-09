import asyncio
from telegram import Bot

# Bot Token ve chat ID (bunları kendi botundan alman gerek)
API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

async def send_telegram_message():
    bot = Bot(token=API_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="🔔 Telegram bildirimi başarıyla çalışıyor!")

if __name__ == "__main__":
    asyncio.run(send_telegram_message())
    print("Mesaj gönderildi.")