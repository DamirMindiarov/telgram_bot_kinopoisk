import json
from datetime import datetime

from loader import bot
from states import states_01
from api.for_deep_find import find_films_for_deep
from database.save_user_info import add_history_message, add_movie_for_deep_find, add_user_history
from telebot.util import quick_markup


@bot.callback_query_handler(
    state=states_01.DeepFind.rating,
    func=lambda callback_query: 'rating ' in callback_query.data)
def show_results(callback_query):
    rating = callback_query.data.split()[1]

    with bot.retrieve_data(callback_query.from_user.id, callback_query.message.chat.id) as data:
        data['rating'] = rating
        result = find_films_for_deep(
            genre=data['genre'],
            years=data['years'],
            rating=data['rating'])

        # Проверка
        if type(result) is str:
            bot.send_message(callback_query.from_user.id, result)
            return

        user_id = callback_query.from_user.id
        command = 'deep_find'
        body = f'{data['genre']}(rating {data['rating']}) {data['years']}'
        date = datetime.now().strftime('%H:%M %A %d.%m.%Y')
        add_user_history(user_id, command, body, date)

        data = json.loads(result.text)
        id_films = add_movie_for_deep_find(data)

        if len(id_films) == 0:
            bot.edit_message_text(
                'Ничего не нашел /find_film',
                callback_query.message.chat.id,
                callback_query.message.message_id
            )
            return

    # добавление в историческую БД
    user_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    list_id_movies = ' '.join(id_films)
    add_history_message(user_id, message_id, list_id_movies)

    keyboard = quick_markup({
        'Показать результаты': {'callback_data': f'show_results {callback_query.message.message_id}'}
    })

    bot.edit_message_text(
        f'Нашел в кол-ве {len(id_films)}',
        callback_query.message.chat.id,
        callback_query.message.message_id,
        reply_markup=keyboard
    )

    bot.set_state(callback_query.from_user.id, states_01.DeepFind.results, callback_query.message.chat.id)
