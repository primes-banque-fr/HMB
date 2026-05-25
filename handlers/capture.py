from config import ADMIN_ID

async def handle_capture(update, context):

    photo = update.message.photo[-1].file_id
    user = update.message.from_user

    text = f"""
🚨 TRANSACTION

👤 @{user.username}
🆔 {user.id}

📸 Capture reçue
"""

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=text
    )

    await update.message.reply_text("📤 Envoyé pour validation admin")
