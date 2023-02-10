import os

from dotenv import load_dotenv

load_dotenv()

# TELEGRAM
CHAT_ID = os.getenv("CHAT_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TELEGRAM_BOT_LOG_FILE = os.path.join(DATA_DIR, "telegram-bot.log")

# MYSQL
host = os.getenv("MYSQL_HOST")
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASS")
dbname = os.getenv("MYSQL_DATABASE")
SQLALCHEMY_DATABASE_URI = f"mysql://{username}:{password}@{host}/{dbname}"
