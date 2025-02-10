from loader import bot


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, '/start - стартовое сообщение\n'
                                           '/find_film - поиск фильмов по названию\n'
                                           '/deep_find - поиск фильмов по названию, жанру, году, рейтингу')
