from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.inline.main import main_menu

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Привет, {message.from_user.full_name}!", 'Этот бот поможет тебе составить список покупок.'

    await message.answer('\n'.join(text), reply_markup=main_menu, reply=True)
