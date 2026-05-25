from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def mtn(update, context):

    text = (
        "🚀💎 𝐌𝐓𝐍 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐋𝐓𝐑𝐀 𝐑𝐀𝐏𝐈𝐃𝐄\n"
        "━━━━━━━━━━━━━━━━\n"
        "📦 5GB — 1000F\n"
        "📦 10GB — 1600F\n"
        "📦 30GB — 3600F"
    )

    keyboard = [
        [InlineKeyboardButton("5GB • 1000F", callback_data="pay_1000")],
        [InlineKeyboardButton("10GB • 1600F", callback_data="pay_1600")],
        [InlineKeyboardButton("30GB • 3600F", callback_data="pay_3600")],
        [InlineKeyboardButton("🔙 Retour", callback_data="catalog")]
    ]

    await update.callback_query.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
