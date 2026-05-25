from services.delivery import deliver_file
from config import ADMIN_ID

async def admin_callback(update, context):

    query = update.callback_query
    await query.answer()

    if update.effective_user.id != ADMIN_ID:
        return

    user_id = query.message.chat_id
    data = query.data

    if data == "ok":

        await query.message.edit_text("✅ Paiement validé")

        await deliver_file(context.bot, user_id, "camtel")

    elif data == "no":
        await query.message.edit_text("❌ Paiement refusé")
