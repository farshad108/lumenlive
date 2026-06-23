import os
import sys
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from services.price_service import get_crypto_price

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to LumenLive 👋\n"
        "Use /price to check the live Bitcoin price."
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    btc_price = get_crypto_price("bitcoin", "usd")
    if btc_price:
        await update.message.reply_text(f"💰 Bitcoin price: ${btc_price:,.2f}")
    else:
        await update.message.reply_text("❌ Couldn't fetch the price right now. Please try again.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    print("✅ Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()