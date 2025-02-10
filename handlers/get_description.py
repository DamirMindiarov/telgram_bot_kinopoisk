from database.models import Movie
from keyboards.gen_keyboard import gen_keyboard
from loader import bot
from database.get_user_info import get_list_id


@bot.callback_query_handler(func=lambda callback_query: 'description ' in callback_query.data)
def get_description(callback_query):
    cur_id_film, id_message = callback_query.data.split()[1:]
    description = Movie.get(Movie.movie_id == cur_id_film).movie_description
    user_id = callback_query.from_user.id

    id_films = get_list_id(user_id, id_message)

    if not description:
        caption = 'Описания нет'
    elif len(description) > 1024:
        caption = description[: 1021] + '...'
    else:
        caption = description

    bot.edit_message_caption(
        caption=caption,
        chat_id=callback_query.message.chat.id,
        message_id=int(id_message) + 1,
        reply_markup=gen_keyboard(id_message, id_films, cur_id_film, description=False)
    )
