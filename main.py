import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from config import BOT_TOKEN
from database import init_db

from handlers.start import start_cmd
from handlers.callbacks import callback_router
from handlers.capture import handle_capture

async def run():

    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CallbackQueryHandler(callback_router))
    app.add_handler(MessageHandler(filters.PHOTO, handle_capture))

    print("BOT ONLINE")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()
