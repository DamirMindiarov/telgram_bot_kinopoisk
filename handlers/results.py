from loader import bot
from database.models import Movie
from keyboards.gen_keyboard import gen_keyboard
from config_data.config import URL_FOR_FILM
from database.get_user_info import get_list_id


@bot.callback_query_handler(func=lambda callback_query: 'show_results ' in callback_query.data)
def results(callback_query):
    id_message = int(callback_query.data.split()[1])
    bot.delete_message(callback_query.message.chat.id, id_message)
    user_id = callback_query.from_user.id

    id_films = get_list_id(user_id, id_message)

    current_id_film = id_films[0]
    description = Movie.get(Movie.movie_id == current_id_film).movie_description
    if description is None:
        description = 'Описания нет'

    film = Movie.get(Movie.movie_id == current_id_film)

    movie_short_description = film.movie_short_description if film.movie_short_description else ''
    caption = '{name}{alt_name} {year}\n{genre}\n{country}\n{short_desc}\n{link}'.format(
        name=film.movie_name,
        alt_name=f'({film.movie_alt_name})' if film.movie_alt_name else "",
        year=film.movie_year,
        genre=film.genre,
        country=film.countries,
        short_desc=movie_short_description,
        link=f'{URL_FOR_FILM}/{film.movie_id}/'
    )

    if film.poster:
        poster = film.poster
    else:
        poster = open('no_poster.jpg', 'rb')

    bot.send_photo(
        callback_query.from_user.id,
        photo=poster,
        caption=caption,
        reply_markup=gen_keyboard(id_message, id_films, current_id_film)
    )
    bot.send_message(callback_query.from_user.id, 'Чтобы начать поиск нажми/введи:\n/find_film\n/deep_find\nТакже '
                                                  'есть кнопка'
                                                  '"Меню" слева.')
