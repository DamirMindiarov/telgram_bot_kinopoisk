from telebot.util import quick_markup


def gen_keyboard(id_message, id_films, cur_id_film, description=True):
    if len(id_films) == 0:
        return
    elif len(id_films) == 1:

        if description:
            keyboard = quick_markup({
                'Описание': {'callback_data': f'description {cur_id_film} {id_message}'}
            }, row_width=3)
        else:
            keyboard = quick_markup({
                'Основная информация': {'callback_data': f'main_info {cur_id_film} {id_message}'}
            }, row_width=3)
        return keyboard

    i_cur_id_film = id_films.index(cur_id_film)
    i_first = id_films.index(id_films[0])
    i_last = id_films.index(id_films[-1])

    back_film = i_cur_id_film - 1 if i_cur_id_film != i_first else i_last
    next_film = i_cur_id_film + 1 if i_cur_id_film != i_last else i_first

    if description:
        keyboard = quick_markup({
            '<-': {'callback_data': f'to {back_film} {id_message}'},
            f'{i_cur_id_film + 1}/{len(id_films)}': {'callback_data': 'none'},
            '->': {'callback_data': f'to {next_film} {id_message}'},
            'Описание': {'callback_data': f'description {cur_id_film} {id_message}'}
        }, row_width=3)
    else:
        keyboard = quick_markup({
            '<-': {'callback_data': f'to {back_film} {id_message}'},
            f'{i_cur_id_film + 1}/{len(id_films)}': {'callback_data': 'none'},
            '->': {'callback_data': f'to {next_film} {id_message}'},
            'Основная информация': {'callback_data': f'main_info {cur_id_film} {id_message}'}
        }, row_width=3)

    return keyboard
