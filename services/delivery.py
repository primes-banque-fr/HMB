import os

def get_file(product):

    path = f"files/{product}/"

    # ❌ sécurité: dossier existe ?
    if not os.path.exists(path):
        return None

    files = os.listdir(path)

    # ❌ sécurité: dossier vide ?
    if not files:
        return None

    # ✔ on trie pour stabilité
    files.sort()

    return os.path.join(path, files[0])


async def deliver_file(bot, user_id, product):

    file_path = get_file(product)

    if not file_path:
        await bot.send_message(
            chat_id=user_id,
            text="❌ 𝐅𝐢𝐜𝐡𝐢𝐞𝐫 𝐢𝐧𝐝𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞"
        )
        return

    try:
        with open(file_path, "rb") as file:

            await bot.send_document(
                chat_id=user_id,
                document=file,
                caption=(
                    "📦✨ 𝐋𝐈𝐕𝐑𝐀𝐈𝐒𝐎𝐍 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋\n"
                    "🔐 Merci pour votre confiance\n"
                    "⚡ HMB Premium System"
                )
            )

    except Exception as e:
        await bot.send_message(
            chat_id=user_id,
            text="⚠️ 𝐄𝐫𝐫𝐞𝐮𝐫 𝐥𝐢𝐯𝐫𝐚𝐢𝐬𝐨𝐧"
        )
        print("Delivery error:", e)
