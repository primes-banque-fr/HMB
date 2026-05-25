from telegram import ReplyKeyboardMarkup
from database import cursor, conn
import random

async def menu_handler(update, context):

    text = update.message.text
    user = update.message.from_user

    # 🛒 MENU ACHAT
    if text == "🛒 Acheter":

        keyboard = [
            ["⚡ CAMTEL", "🚀 MTN"]
        ]

        await update.message.reply_text(
            "🛒💎 𝐂𝐇𝐎𝐈𝐒𝐈𝐒𝐒𝐄𝐙 𝐔𝐍 𝐏𝐑𝐎𝐃𝐔𝐈𝐓\n"
            "━━━━━━━━━━━━━━━━",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # ⚡ PRODUIT CAMTEL / MTN
    elif text in ["⚡ CAMTEL", "🚀 MTN"]:

        ref = f"HMB-{random.randint(10000, 99999)}"

        cursor.execute("""
        INSERT INTO orders (user_id, username, product, plan, amount, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user.id,
            user.username,
            text,
            "1 mois",
            "1000F",
            "pending"
        ))

        conn.commit()

        await update.message.reply_text(
            "💳✨ 𝐏𝐀𝐈𝐄𝐌𝐄𝐍𝐓 𝐑𝐄𝐐𝐔𝐈𝐒\n"
            "━━━━━━━━━━━━━━━━\n"
            f"📦 Produit : {text}\n"
            f"🔖 Référence : {ref}\n"
            "━━━━━━━━━━━━━━━━\n"
            "📲 MTN / Orange Money\n"
            "📸 Envoyez la capture après paiement"
        )
