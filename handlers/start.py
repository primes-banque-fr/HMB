from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🚀✨ 🇭 🇲 🇧™ 𝐅𝐑𝐄𝐄𝐒𝐔𝐑𝐅 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 ✨🚀\n"
        "💎 𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐮𝐞 𝐝𝐚𝐧𝐬 𝐥𝐞 𝐬𝐞𝐫𝐯𝐢𝐜𝐞 𝐮𝐥𝐭𝐫𝐚 𝐩𝐫𝐞𝐦𝐢𝐮𝐦\n"
        "⚡ Fichiers VPN rapides & stables\n"
        "🔐 Système sécurisé & automatisé\n"
        "📦 Livraison instantanée après paiement\n"
        "━━━━━━━━━━━━━━━━\n"
        "📶 𝐑𝐞́𝐬𝐞𝐚𝐮𝐱 𝐝𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞𝐬\n"
        "⚡ CAMTEL Illimité\n"
        "🚀 MTN Premium Ultra Rapide"
    )

    keyboard = [
        [InlineKeyboardButton("🛒 Acheter fichier", callback_data="catalog")],
        [InlineKeyboardButton("💎 Forfaits", callback_data="plans")],
        [InlineKeyboardButton("📤 Paiement", callback_data="payment")],
        [InlineKeyboardButton("📦 Mes achats", callback_data="orders")],
        [InlineKeyboardButton("🧑‍💻 Support", callback_data="support")],
        [InlineKeyboardButton("📚 Tutoriel", callback_data="tutorial")]
    ]

    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
