from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def camtel(update, context):

    text = (
        "⚡💎 𝐂𝐀𝐌𝐓𝐄𝐋 𝐈𝐋𝐋𝐈𝐌𝐈𝐓𝐄́\n"
        "⚜️ Connexion stable & rapide\n"
        "━━━━━━━━━━━━━━━━\n"
        "💰 1S — 500F\n"
        "💰 2S — 750F\n"
        "💰 1M — 1500F"
    )

    keyboard = [
        [InlineKeyboardButton("500F • 1S", callback_data="pay_500")],
        [InlineKeyboardButton("750F • 2S", callback_data="pay_750")],
        [InlineKeyboardButton("1500F • 1M", callback_data="pay_1500")],
        [InlineKeyboardButton("🔙 Retour", callback_data="catalog")]
    ]

    await update.callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
