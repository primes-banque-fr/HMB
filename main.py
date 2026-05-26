import asyncio
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN

from bot.start import start
from bot.buy import buy
from bot.payment import handle_payment
from bot.voice_handler import handle_text_message, handle_voice_message
from admin.admin_panel import approve, reject


def main():

    print("=== HMB SUPPORT AI STARTING ===")

    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN missing")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))

    app.add_handler(CommandHandler("approve", approve))
    app.add_handler(CommandHandler("reject", reject))

    # BUTTONS (IMPORTANT FIX)
    app.add_handler(MessageHandler(filters.Regex("^🛒 Acheter$"), buy))
    app.add_handler(MessageHandler(filters.Regex("^💳 Paiement$"), buy))
    app.add_handler(MessageHandler(filters.Regex("^📦 Commandes$"), buy))
    app.add_handler(MessageHandler(filters.Regex("^📞 Support$"), buy))

    # PAYMENT IMAGE
    app.add_handler(MessageHandler(filters.PHOTO, handle_payment))

    # TEXT + VOICE AI
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice_message))

    print("=== BOT RUNNING (HMB SUPPORT AI ACTIVE) ===")

    app.run_polling()


if __name__ == "__main__":
    main()
