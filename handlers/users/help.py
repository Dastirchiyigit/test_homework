from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from datetime import datetime

# today = date.today()
# print("Today's date:", today)

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))

@dp.message_handler(commands='time')
async def bot_help(message: types.Message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    text=f"bizning vaqt ={dt_string}"

    await message.answer(text)


import requests
import json


@dp.message_handler(commands='usd')
async def bot_help(message: types.Message):
    r = requests.get("https://api.exchangerate.host/latest?base=UZS")
    json_object = json.loads(r.text)
    json_object=(json_object["rates"])
    xabar=''
    for x in json_object:
        xabar+=(f"{x} = {json_object[x]}\n")
    await message.answer(xabar)
