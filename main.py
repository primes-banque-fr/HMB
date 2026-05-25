import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN
from database import init_db

from handlers.start import start_cmd
from handlers.menu import menu_handler
from handlers.capture import handle_capture
from handlers.admin import admin_callback

async def run_bot():

    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))
    app.add_handler(MessageHandler(filters.PHOTO, handle_capture))
    app.add_handler(CallbackQueryHandler(admin_callback))

    print("BOT ONLINE")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # garder le bot vivant
    await asyncio.Event().wait()

def main():
    asyncio.run(run_bot())

if __name__ == "__main__":
    main()
