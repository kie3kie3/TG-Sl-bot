import config
import telebot
from telebot import types
from getter import get_info, update


bot = telebot.TeleBot(config.bot)


def mk_markup(message):
    markup = types.ReplyKeyboardMarkup()
    for i in config.wait_list:
        markup.add(i)
    bot.send_message(message.chat.id, 'Привет', parse_mode='html', reply_markup=markup)


def register(message):
    bd = get_info()
    try:
        del bd[str(message.chat.id)]
        print(456)
    except:
        print(123)
    bd[str(message.chat.id)] = {
        'name' : message.text,
        'wait' : {},
        'all_penalty': []
    }
    for i in config.wait_list:
        bd[str(message.chat.id)]['wait'][i] = False
    if str(message.chat.id) not in bd['ids']:
        bd['ids'].append(str(message.chat.id))
    update(bd)
    mk_markup(message)
