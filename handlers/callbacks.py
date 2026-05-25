from handlers.catalog import catalog
from handlers.camtel import camtel
from handlers.payment import payment

async def callback_router(update, context):

    data = update.callback_query.data

    if data == "catalog":
        return await catalog(update, context)

    if data == "camtel":
        return await camtel(update, context)

    if data == "payment":
        return await payment(update, context)
