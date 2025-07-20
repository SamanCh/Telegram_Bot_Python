from telegram import Bot

# Replace with your own token and chat ID
TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Your code has finished running!")
