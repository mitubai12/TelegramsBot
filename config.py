from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from db.db import Database


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
db = Database("db.sqlite3")