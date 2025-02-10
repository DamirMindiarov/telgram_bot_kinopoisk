import json

from loader import bot
from states.states_01 import MyStates
from api.api import find_films
from database.save_user_info import add_movie, add_history_message, add_user_history
from telebot.util import quick_markup
from datetime import datetime


@bot.callback_query_handler(state=MyStates.count, func=lambda callback_query: 'count ' in callback_query.data)
def for_count(callback_query):
    count, id_message = callback_query.data.split()[1:]

    with bot.retrieve_data(callback_query.from_user.id, callback_query.message.chat.id) as data:
        result = find_films(data['name'], int(count))

        # Проверка
        if type(result) is str:
            bot.send_message(callback_query.from_user.id, result)
            return

        user_id = callback_query.from_user.id
        command = 'find_film'
        body = f'name {data['name']}'
        date = datetime.now().strftime('%H:%M %A %d.%m.%Y')
        add_user_history(user_id, command, body, date)

        data = json.loads(result.text)
        add_movie(data)

        id_films = [str(elem['id']) for elem in data['docs']]

        if len(id_films) == 0:
            bot.send_message(callback_query.from_user.id, 'Ничего не нашел /find_film')
            return

    # добавляет в database_history_messages информацию о сообщении в котором показан результат запроса
    user_id = callback_query.from_user.id
    message_id = callback_query.message.message_id + 1
    list_id_movies = ' '.join(id_films)
    add_history_message(user_id, message_id, list_id_movies)

    keyboard = quick_markup({
        'Показать результаты': {'callback_data': f'show_results {callback_query.message.message_id + 1}'}
    })

    bot.delete_message(callback_query.message.chat.id, id_message)
    bot.send_message(callback_query.from_user.id, f'Нашел в кол-ве {len(id_films)}',
                     reply_markup=keyboard)
    bot.set_state(callback_query.from_user.id, MyStates.results, callback_query.message.chat.id)
