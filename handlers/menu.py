from telegram import ReplyKeyboardMarkup
from database import cursor, conn
import random

async def menu_handler(update, context):

    text = update.message.text
    user = update.message.from_user

    # acheter
    if text == "🛒 Acheter":

        keyboard = [["CAMTEL", "MTN"]]

        await update.message.reply_text(
            "Choisissez un produit",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # produit sélectionné
    elif text in ["CAMTEL", "MTN"]:

        ref = f"HMB-{random.randint(10000,99999)}"

        cursor.execute("""
        INSERT INTO orders (user_id, username, product, plan, amount, status, ref)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            user.id,
            user.username,
            text,
            "1 mois",
            1000,
            "pending",
            ref
        ))

        conn.commit()

        await update.message.reply_text(
f"""
💳 Paiement requis

📦 Produit : {text}
🔖 Référence : {ref}

📲 MTN / Orange Money

Envoyez la capture après paiement.
"""
      )
