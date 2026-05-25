from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def catalog(update, context):

    text = (
        "🛒💎 𝐂𝐀𝐓𝐀𝐋𝐎𝐆𝐔𝐄 𝐏𝐑𝐄𝐌𝐈𝐔𝐌\n"
        "━━━━━━━━━━━━━━━━\n"
        "⚡ CAMTEL Illimité\n"
        "🚀 MTN Premium Ultra Rapide"
    )

    keyboard = [
        [InlineKeyboardButton("⚡ CAMTEL", callback_data="camtel")],
        [InlineKeyboardButton("🚀 MTN", callback_data="mtn")],
        [InlineKeyboardButton("🔙 Retour", callback_data="start")]
    ]

    await update.callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
