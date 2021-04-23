from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import callback_list, callback
from keyboards.inline.main import main_menu, new_list
from utils.db_work import get_user_list_values, get_lists_names
from loader import dp

@dp.callback_query_handler(callback.filter(what="my_lists"))
async def get_my_lists(call: CallbackQuery):
    user_id = str(call.from_user.id)    
    callback_data = call.data

    keyboard_list = InlineKeyboardMarkup(row_width=2)
    if get_lists(user_id) == "У тебя еще нет списков":
        await call.message.answer(get_lists_names(user_id), reply_markup=new_list)
    else:
        for i in get_lists(user_id):
            new_button = InlineKeyboardButton(text=f"{i}", callback_data=f'get:{i}:list')
            keyboard_list.insert(new_button)
        await call.message.answer("Все твои списки ниже", reply_markup=keyboard_list)

@dp.callback_query_handler(callback_list.filter(list='list'))
async def view_list(call: CallbackQuery, callback_data: dict):
    user_id = str(call.from_user.id)
    list_name = callback_data.get('list_name')
    some = 'Название списка - {list_name}\nСодержание списка: \n{values}'.format(list_name=list_name, values='\n'.join(get_user_list_values(user_id, list_name)))

    await call.message.answer(some)
    text = f"{call.from_user.full_name}, я готов на работу с твоими списками!"

    await call.message.answer(text, reply_markup=main_menu, reply=True)
