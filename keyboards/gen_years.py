from telebot.util import quick_markup


def gen_years():
    buttons_year = {f'{i}-{i + 10}': {'callback_data': f'years {f'{i}-{i + 10}'}'} for i in range(1980, 2020 + 1, 10)}
    buttons_year.update({'1980-2030': {'callback_data': 'years 1980-2030'}})

    keyboard = quick_markup(buttons_year, row_width=5)

    return keyboard
