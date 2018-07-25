# -*- coding: utf-8 -*-
import pandas as pd
import jaydebeapi
import configparser


class DayPassengerDate(object):

    Config = configparser.ConfigParser()
    Config.read("../model/dbconfig.conf")
    dirver = Config.get('DATABASE', 'dirver')
    url = Config.get('DATABASE', 'url')
    user = Config.get('DATABASE', 'user')
    password = Config.get('DATABASE', 'password')
    jarFile = Config.get('DATABASE', 'jarFile')
    db = jaydebeapi.connect(dirver, [url, user, password], jarFile)

    try:
        curs = db.cursor()
        sql_X_test12 = 'SELECT "JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUG","SEP","OCT","NOV","DEC","MON","TUES","WED","THUR","FRI","SAT","SUN" FROM PASSENGER WHERE "CREATEDAY" < TO_DATE ( \'2013-01-01 00:00:00\', \'yyyy-mm-dd hh24:mi:ss\' ) ORDER BY "ID"'
        curs.execute(sql_X_test12)
        X_test12_get = curs.fetchall()

        sql_y_test12 = 'SELECT "PASSENGERF" FROM PASSENGER WHERE "CREATEDAY" < TO_DATE ( \'2013-01-01 00:00:00\', \'yyyy-mm-dd hh24:mi:ss\' ) ORDER BY "ID"'
        curs.execute(sql_y_test12)
        y_test12_get = curs.fetchall()

        sql_X_test13 = 'SELECT "JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUG","SEP","OCT","NOV","DEC","MON","TUES","WED","THUR","FRI","SAT","SUN" FROM PASSENGER WHERE "CREATEDAY" BETWEEN TO_DATE ( \'2013-01-01 00:00:00\', \'yyyy-mm-dd hh24:mi:ss\' ) and TO_DATE ( \'2014-01-01 00:00:00\', \'yyyy-mm-dd hh24:mi:ss\' ) ORDER BY "ID"'
        curs.execute(sql_X_test13)
        X_test13_get = curs.fetchall()

        sql_y_test13 = 'SELECT "PASSENGERF" FROM PASSENGER WHERE "CREATEDAY" BETWEEN TO_DATE ( \'2013-01-01 00:00:00\', \'yyyy-mm-dd hh24:mi:ss\' ) and TO_DATE ( \'2014-01-01 00:00:00\', \'yyyy-mm-dd hh24:mi:ss\' ) ORDER BY "ID"'
        curs.execute(sql_y_test13)
        y_test13_get = curs.fetchall()
    finally:
        db.close()

    # 数据集
    X_test12 = pd.DataFrame(list(X_test12_get))  # 12年测试集合 特征
    y_test12 = pd.DataFrame(list(y_test12_get))  # 12年测试集合 结果
    X_test13 = pd.DataFrame(list(X_test13_get))  # 13年测试集合 特征
    y_test13 = pd.DataFrame(list(y_test13_get))  # 13年测试集合 结果

    def getlastyearfeature(self):
        return self.X_test12

    def getlastyearresult(self):
        return self.y_test12

    def getpredictfeature(self):
        return self.X_test13

    def getpredictresult(self):
        return self.y_test13
