from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=2)

new_list = InlineKeyboardButton(text="Создать новый список", callback_data='go:new_list')
my_lists = InlineKeyboardButton(text="Мои списки", callback_data='go:my_lists')

main_menu.insert(new_list)
main_menu.insert(my_lists)