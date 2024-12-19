import config
import telebot
import admin
from telebot import types
import time
from getter import get_info, update
from register import register
from lateMaster import checkLate


bot = telebot.TeleBot(config.bot)


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "Как звать, тебя человек?")
    bot.register_next_step_handler(msg, register)


def inside(situation, id, db, date):
    db['day_late'][situation] = [True, date, db[id]['name']]
    db[id]['wait'][situation] = False
    return db


def cancel(message):
    db = get_info()
    for i in config.wait_list:
        if db[message.chat.id]['wait'][i]:
            db[message.chat.id]['wait'][i] = False
    update(db)


def photo(message):
    if not message.photo:
        bot.send_message(message.chat.id, 'Я умею принимать только фотки, напиши мне еще раз и пришли таки фотку')
        cancel(message)
        return  1
    db = get_info()
    for i in config.admins:
        bot.send_photo(i, message.photo[0].file_id, caption=db[str(message.chat.id)]['name'])
    for i in config.wait_list:
        if db[str(message.chat.id)]['wait'][i]:
            db = inside(i, str(message.chat.id), db, message.date)
            db = checkLate(db, float(message.date), i, str(message.chat.id))
    update(db)


@bot.message_handler()
def markup_txt(message):
    if message.text in config.wait_list:
        db = get_info()
        db[str(message.chat.id)]['wait'][message.text] = True
        update(db)
        msg = bot.send_message(message.chat.id, config.text)
        bot.register_next_step_handler(msg, photo)
    elif message.text == 'id':
        bot.send_message(message.chat.id, message.chat.id)
    elif message.chat.id in config.admins:
        if message.text == 'Опоздания':
            admin.sendWeek()
    else:
        bot.send_message(message.chat.id, 'Чаво?')


def main():
    time.sleep(6)
    print('Старт')
    bot.infinity_polling()
