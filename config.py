from os import getenv


API_ID = int(getenv("API_ID", "21705536"))
API_HASH = getenv("API_HASH", "c5bb241f6e3ecf33fe68a444e288de2d")
BOT_TOKEN = getenv("BOT_TOKEN", "7752183423:AAHwms4ySxoFaSCZU5nrv7lvqL_HosNra08")
OWNER_ID = int(getenv("OWNER_ID", "5957208798"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


