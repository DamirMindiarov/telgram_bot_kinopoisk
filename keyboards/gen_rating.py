from telebot.util import quick_markup


def gen_rating():
    keyboard = quick_markup({
        '1-3': {'callback_data': 'rating 1-3'},
        '3-6': {'callback_data': 'rating 3-6'},
        '6-10': {'callback_data': 'rating 6-10'},
        '1-10': {'callback_data': 'rating 1-10'}
    }, row_width=3)

    return keyboard
