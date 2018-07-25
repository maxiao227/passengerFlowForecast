# -*- coding: utf-8 -*-
import pandas as pd
import configparser
import jaydebeapi


class BpNNPassengerDate(object):
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
        sql = 'select "six","seven" from DATAPASSEGNER WHERE ROWNUM<2 ORDER BY "id" DESC'  # 根据测试，选用之前2天的客流数据作为输入
        curs.execute(sql)
        result = curs.fetchall()
    finally:
        db.close()

    data = pd.DataFrame(list(result))

    def getHistorical(self):
        return self.data
