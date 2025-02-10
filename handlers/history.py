from loader import bot
from database.get_user_info import get_user_history


@bot.message_handler(commands=['history'])
def show_history(message):
    user_id = message.from_user.id
    result = get_user_history(user_id)

    str_history = ''
    for elem in result[::-1]:
        str_history += elem + '\n'

    bot.send_message(message.from_user.id, str_history)
