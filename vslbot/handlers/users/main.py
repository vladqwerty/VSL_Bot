from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Привет, {message.from_user.full_name}!"

    await message.answer(text)
