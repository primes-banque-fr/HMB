import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

MTN_NUMBER = os.getenv("MTN_NUMBER")
ORANGE_NUMBER = os.getenv("ORANGE_NUMBER")
