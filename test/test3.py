# -*- coding: utf-8 -*-
# 配置数据库
import configparser
import datetime
import jaydebeapi
import numpy as np


def getdate(n):
    date = str(datetime.datetime.now() + datetime.timedelta(days=n))[0:10]
    return date


Config = configparser.ConfigParser()
Config.read('../model/dbconfig.conf')
dirver = Config.get('DATABASE', 'dirver')
url = Config.get('DATABASE', 'url')
user = Config.get('DATABASE', 'user')
password = Config.get('DATABASE', 'password')
jarFile = Config.get('DATABASE', 'jarFile')
db = jaydebeapi.connect(dirver, [url, user, password], jarFile)
try:
    curs = db.cursor()
    sqlx = 'SELECT RS.* FROM REC_SENSEAREAPFDATA RS'
    curs.execute(sqlx)
    result = curs.fetchall()
finally:
    db.close()

print(type(result))
