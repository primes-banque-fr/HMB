import os

def get_file(product):

    path = f"files/{product}/"
    files = os.listdir(path)

    return os.path.join(path, files[0]) if files else None


async def deliver_file(bot, user_id, product):

    file_path = get_file(product)

    if not file_path:
        await bot.send_message(user_id, "❌ fichier indisponible")
        return

    await bot.send_document(
        chat_id=user_id,
        document=open(file_path, "rb"),
        caption="📦 Livraison réussie"
    )
