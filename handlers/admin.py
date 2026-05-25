from config import ADMIN_ID
from services.delivery import deliver_file
from database import cursor, conn

async def admin_callback(update, context):

    query = update.callback_query
    await query.answer()

    user = update.effective_user

    if user.id != ADMIN_ID:
        await query.message.edit_text(
            "⛔ Accès refusé"
        )
        return

    data = query.data

    user_id = context.user_data.get("user_id")
    product = context.user_data.get("product")
    plan = context.user_data.get("plan")
    amount = context.user_data.get("amount")

    if data == "ok":

        cursor.execute(
            "UPDATE orders SET status='paid' WHERE user_id=?",
            (user_id,)
        )
        conn.commit()

        await query.message.edit_text(
            "✅ 𝐏𝐀𝐈𝐄𝐌𝐄𝐍𝐓 𝐕𝐀𝐋𝐈𝐃𝐄́\n"
            "📦 Livraison en cours..."
        )

        await deliver_file(
            context.bot,
            user_id,
            product
        )

    if data == "no":

        cursor.execute(
            "UPDATE orders SET status='rejected' WHERE user_id=?",
            (user_id,)
        )
        conn.commit()

        await query.message.edit_text(
            "❌ 𝐏𝐀𝐈𝐄𝐌𝐄𝐍𝐓 𝐑𝐄𝐅𝐔𝐒𝐄́\n"
            "⚠️ Transaction invalide"
        )

    if data == "fraud":

        cursor.execute(
            "UPDATE orders SET status='fraud' WHERE user_id=?",
            (user_id,)
        )
        conn.commit()

        await query.message.edit_text(
            "🚨 𝐅𝐑𝐀𝐔𝐃𝐄 𝐃𝐄𝐓𝐄𝐂𝐓𝐄́𝐄\n"
            "⛔ Transaction bloquée"
        )
