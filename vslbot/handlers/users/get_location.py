from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

from keyboards.default import locations_buttons

@dp.message_handler(Command('show'))
async def show_on_map(message: types.Message):
    await message.answer(
        "Если хочешь узнать ближайшие магазины, просто отправь мне свое местоположение!",
        reply_markup=locations_buttons.keybord
)

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    lat = location.latitude
    long = location.longitude
    #do smt