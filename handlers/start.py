from loader import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.from_user.id, 'Привет! Я бот, умею искать фильмы/сериалы по названию на www.kinopoisk.ru\n\n'
                              'Выбери одну из команд ниже, для более удобной навигации у тебя должна быть кнопка '
                              '"Меню" слева\n'
                              '- /find_film поиск по названию\n- /deep_find поиск по жанру, году, рейтингу'
    )
