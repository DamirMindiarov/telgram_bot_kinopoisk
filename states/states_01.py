from telebot.handler_backends import State, StatesGroup


class MyStates(StatesGroup):
    name = State()
    count = State()
    results = State()


class DeepFind(StatesGroup):
    genre = State()
    years = State()
    rating = State()
    results = State()