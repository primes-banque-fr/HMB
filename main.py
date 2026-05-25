from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN
from database import init_db

from handlers.start import start_cmd
from handlers.menu import menu_handler
from handlers.capture import handle_capture
from handlers.admin import admin_callback

def main():

    # créer base de données
    init_db()

    # connecter bot Telegram
    app = Application.builder().token(BOT_TOKEN).build()

    # commandes
    app.add_handler(CommandHandler("start", start_cmd))

    # messages texte
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))

    # images (captures)
    app.add_handler(MessageHandler(filters.PHOTO, handle_capture))

    # boutons admin
    app.add_handler(CallbackQueryHandler(admin_callback))

    print("BOT ONLINE")
    app.run_polling()

if __name__ == "__main__":
    main()
