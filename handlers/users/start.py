import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp,db,bot


@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    telegram_id=message.from_user.id
    username=message.from_user.username
    full_name=message.from_user.full_name

    try:
        user=await db.add_user(full_name=full_name,username=username,telegram_id=telegram_id,)
    except asyncpg.exceptions.UniqueViolationError:
        user=await db.select_user(telegram_id=telegram_id)

    await message.answer(f"qalle butalogm!")

    # adminga xabar

    msg=f"yangi odam qushildi botga \n"

    await bot.send_message(ADMINS[0],msg)




