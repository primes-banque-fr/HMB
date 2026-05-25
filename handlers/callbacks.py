from handlers.catalog import catalog
from handlers.camtel import camtel
from handlers.payment import payment
from handlers.start import start_cmd

async def callback_router(update, context):

    data = update.callback_query.data

    # 🛒 Catalogue
    if data == "catalog":
        return await catalog(update, context)

    # ⚡ CAMTEL
    if data == "camtel":
        return await camtel(update, context)

    # 💳 Paiement
    if data == "payment":
        return await payment(update, context)

    # 🏠 Retour START
    if data == "start":
        return await start_cmd(update, context)
