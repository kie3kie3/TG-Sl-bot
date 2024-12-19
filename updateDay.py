import config
import time
from getter import get_info, update
import admin


def make_shedule(now, db, wday):
    h = 3600
    m = 60
    t = time.localtime(now)
    x = (t.tm_year, t.tm_mon, t.tm_mday, 0, 0, 0, t.tm_wday, t.tm_yday, t.tm_isdst)
    now = time.mktime(x)
    if wday == 6 or wday == 5:  
        wday = 1
    else:
        wday = 0
    for i in config.wait_list:
        j = now + h * (config.time_late[i][0]) + m * config.time_late[i][1]
        if i in config.wday:
            j += h * wday
        db['checker']['shedule'][i] = j
    db['checker']['update'] = [t.tm_mon, t.tm_mday]
    return db


def update_ping(db):
    for i in config.wait_list:
        db['checker']['ping_late'][i] = True
    return db


def day_update(now, cur):
    wday = cur.tm_wday 
    db = get_info()
    if wday == 6:
        admin.sendWeek()
        admin.clear()
    for i in config.wait_list:
        db['day_late'][i] = [False, 0, ""]
    db = make_shedule(now, db, wday)
    db = update_ping(db)
    update(db)
