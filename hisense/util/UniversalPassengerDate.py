# -*- coding: utf-8 -*-
import pandas as pd
import configparser
import jaydebeapi
import numpy as np


class UniversalPassengerDate(object):
    Config = configparser.ConfigParser()
    Config.read('../model/dbconfig.conf')
    dirver = Config.get('DATABASE', 'dirver')
    url = Config.get('DATABASE', 'url')
    user = Config.get('DATABASE', 'user')
    password = Config.get('DATABASE', 'password')
    jarFile = Config.get('DATABASE', 'jarFile')
    sql = 'SELECT RS.PFDATA1 FROM REC_SENSEAREAPFDATA RS WHERE RS.PFDATATYPE = \'1\' AND RS.SENSAREAID IN ( SELECT MH.AREACODE FROM MC_HUBSENSITIVEAREAINFO MH WHERE MH.UNITID ='

    def getLastWeekAmount(self, model):
        try:
            db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            getLastWeekAmountsql = self.sql + '\'' + model + '\' ) AND ( TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') = TO_CHAR (SYSDATE - 7, \'yyyy-mm-dd\') OR TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') = TO_CHAR (SYSDATE - 14, \'yyyy-mm-dd\') OR TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') = TO_CHAR (SYSDATE - 21, \'yyyy-mm-dd\')) AND TO_CHAR (RS.ACTTIME, \'hh24\') = ( SELECT TO_CHAR (SYSDATE, \'hh24\') DDATE FROM DUAL )'
            curs.execute(getLastWeekAmountsql)
            lastWeekAmount = curs.fetchall()
        finally:
            db.close()
            return lastWeekAmount

    def getLastDayAmount(self, model):
        try:
            db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            getLastDayAmountsql = self.sql + '\'' + model + '\' ) AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') >= TO_CHAR (SYSDATE - 3, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') < TO_CHAR (SYSDATE, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'hh24\') = ( SELECT TO_CHAR (SYSDATE, \'hh24\') DDATE FROM DUAL )'
            curs.execute(getLastDayAmountsql)
            lastDayAmount = curs.fetchall()
        finally:
            db.close()
            return lastDayAmount

    def getLastHourAmount(self, model):
        try:
            db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            getLastHourAmountsql = self.sql + '\'' + model + '\' ) AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') = TO_CHAR (SYSDATE, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'hh24\') >= ( SELECT TO_CHAR (SYSDATE, \'hh24\') - 3 DDATE FROM DUAL ) AND TO_CHAR (RS.ACTTIME, \'hh24\') < ( SELECT TO_CHAR (SYSDATE, \'hh24\') DDATE FROM DUAL )'
            curs.execute(getLastHourAmountsql)
            lastHourAmount = curs.fetchall()
        finally:
            db.close()
            return lastHourAmount

    def getActualAmount(self, model):
        try:
            db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            getActualAmountsql = self.sql + '\'' + model + '\' ) AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') = TO_CHAR (SYSDATE, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'hh24\') = ( SELECT TO_CHAR (SYSDATE, \'hh24\') DDATE FROM DUAL )'
            curs.execute(getActualAmountsql)
            actualAmount = curs.fetchall()
        finally:
            db.close()
            return actualAmount

    def getLastWeeksList(self, model):
        try:
            db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            getActualAmountsql = self.sql + '\'' + model + '\' ) AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') >= TO_CHAR (SYSDATE - 7, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') < TO_CHAR (SYSDATE - 28, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'hh24\') = ( SELECT TO_CHAR (SYSDATE, \'hh24\') DDATE FROM DUAL )'
            curs.execute(getActualAmountsql)
            actualAmount = curs.fetchall()
            Week3List, Week2List, Week1List = [], [], []
            for i in range(168):
                Week1List.append(actualAmount[i])
                Week2List.append(actualAmount[i + 168])
                Week3List.append(actualAmount[i + 336])
            weeklist = np.hstack(Week3List, Week2List, Week1List)
        finally:
            db.close()
            return weeklist

    def getLastHoursList(self, model):
        try:
            db = jaydebeapi.connect(self.dirver, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            getActualAmountsql = self.sql + '\'' + model + '\' ) AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') >= TO_CHAR (SYSDATE - 1, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') < TO_CHAR (SYSDATE - 3, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'hh24\') = ( SELECT TO_CHAR (SYSDATE, \'hh24\') DDATE FROM DUAL )'
            curs.execute(getActualAmountsql)
            actualAmount = curs.fetchall()
            Hour3List, Hour2List, Hour1List = [], [], []
            for i in range(72):
                Hour3List.append(actualAmount[i])
                Hour2List.append(actualAmount[i + 24])
                Hour1List.append(actualAmount[i + 48])
            Hourlist = np.hstack(Hour3List, Hour2List, Hour1List)
        finally:
            db.close()
            return Hourlist
