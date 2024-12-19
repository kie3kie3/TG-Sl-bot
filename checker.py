import time
import telebot
import config
from getter import get_info, update
from updateDay import day_update


bot = telebot.TeleBot(config.bot)


def ping(db, now):
    for i in config.wait_list:
        if db['checker']['ping_late'][i] and not db['day_late'][i][0] and now > db['checker']['shedule'][i] + 60:
            for a in config.admins:
                bot.send_message(a, f"{i} - опоздание")
            db['checker']['ping_late'][i] = False
            update(db)
            db = get_info()


def check_late(now):
    db = get_info()
    cur = time.localtime(now)
    if cur.tm_mon != db['checker']['update'][0] or cur.tm_mday != db['checker']['update'][1]:
        day_update(now, cur)
        print('ЫЫЫЫ')
    ping(db, now)



def main():
    while True:
        check_late(time.time())
        time.sleep(2)
