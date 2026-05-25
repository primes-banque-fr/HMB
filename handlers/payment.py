from config import MTN_NUMBER, ORANGE_NUMBER

async def payment(update, context):

    text = (
        "💳✨ 𝐏𝐀𝐈𝐄𝐌𝐄𝐍𝐓 𝐒𝐄́𝐂𝐔𝐑𝐈𝐒𝐄́\n"
        "━━━━━━━━━━━━━━━━\n"
        f"🟡 MTN MoMo : {MTN_NUMBER}\n"
        f"🟠 Orange Money : {ORANGE_NUMBER}\n"
        "━━━━━━━━━━━━━━━━\n"
        "📸 Envoyez votre capture après paiement"
    )

    await update.callback_query.message.edit_text(text)
