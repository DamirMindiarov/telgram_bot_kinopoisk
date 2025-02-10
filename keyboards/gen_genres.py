from telebot.util import quick_markup

genres = ['боевик', 'ужасы', 'фэнтези', 'фантастика', 'комедия', 'драма', 'документальный']


def gen_genres():
    buttons = {genre: {'callback_data': f'genre {genre}'} for genre in genres}

    keyboard = quick_markup(buttons, row_width=3)
    return keyboard
