from aiogram.dispatcher.filters.state import StatesGroup, State 

class AllStates(StatesGroup):
    new_values = State()