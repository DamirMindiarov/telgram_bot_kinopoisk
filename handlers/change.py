from loader import bot
from database.models import Movie
from telebot.types import InputMediaPhoto
from keyboards.gen_keyboard import gen_keyboard
from config_data.config import URL_FOR_FILM
from database.get_user_info import get_list_id


@bot.callback_query_handler(func=lambda callback_query: 'to ' in callback_query.data)
def change(callback_query):
    i_new_id_film, id_message = callback_query.data.split()[1:]
    user_id = callback_query.from_user.id

    id_films = get_list_id(user_id, id_message)

    new_id_film = id_films[int(i_new_id_film)]

    film = Movie.get(Movie.movie_id == new_id_film)

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
        media = InputMediaPhoto(poster, caption=caption)
    else:
        poster = open('no_poster.jpg', 'rb')
        media = InputMediaPhoto(poster, caption=caption)

    bot.edit_message_media(
        media=media,
        chat_id=callback_query.message.chat.id,
        message_id=int(id_message) + 1,
        reply_markup=gen_keyboard(int(id_message), id_films, new_id_film))
