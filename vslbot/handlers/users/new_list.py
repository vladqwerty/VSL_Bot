from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from states.main import AllStates
from keyboards.inline.callback_datas import callback

@dp.callback_query_handler(callback.filter(what="new_list"))
async def new_list(call: CallbackQuery):
    await call.message.answer('Пожалуйста, введи продукты, которые ты хочешь добавить в свой список.\nПример:')
    await call.message.answer('Кефир\nМолоко\nСтейки\nВино')
    await AllStates.new_values.set()

@dp.message_handler(state=AllStates().new_values)
async def new_values(message: types.Message, state: FSMContext):
    text = message.text.split()
    await message.answer('Готово!')
    # db['user'].add()