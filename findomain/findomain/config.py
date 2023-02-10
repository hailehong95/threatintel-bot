import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

load_dotenv()

app = Flask(__name__)

# FINDOMAIN
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BINS_DIR = os.path.join(BASE_DIR, "bin")
DATA_DIR = os.path.join(BASE_DIR, "data")
FINDOMAIN_BIN = "findomain.exe" if os.name == "nt" else "findomain"
FINDOMAIN_LOG_FILE = os.path.join(DATA_DIR, "findomain.log")

# TELEGRAM
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# MYSQL
host = os.getenv("MYSQL_HOST")
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASS")
dbname = os.getenv("MYSQL_DATABASE")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{username}:{password}@{host}/{dbname}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
