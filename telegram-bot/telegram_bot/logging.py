import sys
import logging

from telegram_bot.config import TELEGRAM_BOT_LOG_FILE

logger = logging.getLogger()
logFormatter = logging.Formatter('%(asctime)s - %(filename)s.%(funcName)s:%(lineno)d - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

fileHandler = logging.FileHandler(TELEGRAM_BOT_LOG_FILE)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.INFO)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
