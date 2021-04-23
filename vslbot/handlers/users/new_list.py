from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from states.main import AllStates
from keyboards.inline.callback_datas import callback
from keyboards.inline.main import main_menu
from utils.db_work import new_list

@dp.callback_query_handler(callback.filter(what="new_list"))
async def new_list_bot(call: CallbackQuery):
    await call.message.answer("Пожалуйста, введи название твоего списка")
    await AllStates.list_name.set()

@dp.message_handler(state=AllStates().list_name)
async def new_values(message: types.Message, state: FSMContext):
    list_name = message.text
    await state.update_data(list_name=list_name)
    await message.answer("Отлично! Пожалуйста, введи продукты, которые ты хочешь добавить в свой список.\nПример:")
    await message.answer('Кефир\nМолоко\nСтейки\nВино')
    await AllStates.new_values.set()

@dp.message_handler(state=AllStates().new_values)
async def get_list_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = str(message.from_user.id)
    new_values = message.text.split() 
    list_name = data.get("list_name")
    new_list(user_id, list_name, new_values)
    text = f"{message.from_user.full_name}, я сохранил твой список и готов дальше к работе "
    await message.answer(text, reply_markup=main_menu, reply=True)

    await state.finish()
