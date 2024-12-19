import telebot
import config
from getter import get_info, update

bot = telebot.TeleBot(config.bot)


def sendWeek():
    db = get_info()
    message = 'Опоздания на этой неделе:' + '\n'
    weekLate = db["week_late"].items()
    for key, value in weekLate:
        message += f'{db[key]['name']}: {value} \n'
    for i in config.admins:
        bot.send_message(i, message)
    update(db)


def clear():
    db = get_info()
    db['week_late'] = {}
    update(db)



