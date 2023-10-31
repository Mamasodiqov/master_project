import asyncio
import logging
import sys
from os import getenv

from db import DB
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

button1 = KeyboardButton(text ='share contact', request_contact=True)
button2 = KeyboardButton(text = 'share location', request_location=True)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[[button1],[button2]])

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "5964437215:AAEeQ0QARYTIDbJRXRPgx3K0qw7LG23hbBA"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
db = DB()

@dp.message(CommandStart())
async def welcome(message: types.Message) -> None:
    await message.reply(f"""Assalomu alaykum, {hbold(message.from_user.full_name)} botimizga xush kelibsiz!
    Men Client_bot, sizning yordamchingiz bo`laman.  """, reply_markup=keyboard1)

@dp.message()
async def register(message: types.Message):
    await message.answer(""""Ismingizni kiriting👇""")
    await Register.first_name.set()



######################################
async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
