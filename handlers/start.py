from telegram import ReplyKeyboardMarkup

async def start_cmd(update, context):

    keyboard = [
        ["🛒 Acheter", "💳 Paiement"],
        ["📦 Commandes"]
    ]

    await update.message.reply_text(
        "🚀 VPN PREMIUM BOT\nBienvenue 👑",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
