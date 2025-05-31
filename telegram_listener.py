from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

from config import TELEGRAM_BOT_TOKEN

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'crypto' in update.message.text.lower():
        await update.message.reply_text("📡 Fetching today's crypto insights... please wait.")
        from analyzer import run_analysis
        result = run_analysis(return_output=True)
        await update.message.reply_text(result[:4000])

def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("✅ Telegram Bot is listening...")
    app.run_polling()
