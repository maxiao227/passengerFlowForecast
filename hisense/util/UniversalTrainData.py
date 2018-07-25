'''
获取训练集
'''
import configparser
import datetime
import jaydebeapi
import numpy as np


class UniversalTrainData(object):
    Config = configparser.ConfigParser()
    Config.read('../model/dbconfig.conf')
    dirver = Config.get('DATABASE', 'dirver')
    url = Config.get('DATABASE', 'url')
    user = Config.get('DATABASE', 'user')
    password = Config.get('DATABASE', 'password')
    jarFile = Config.get('DATABASE', 'jarFile')
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    y = []
    lastWeekAmount = []
    lastDayAmount = []
    lastHourAmount = []
    actualAmount = []
    dataEnter = {}
    dataLeave = {}
    sql = 'SELECT RS.PFDATA1, RS.PFDATA2, RS.ACTTIME FROM REC_SENSEAREAPFDATA RS WHERE RS.PFDATATYPE = \'1\' AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') >= TO_CHAR (SYSDATE - 90, \'yyyy-mm-dd\') AND TO_CHAR (RS.ACTTIME, \'yyyy-mm-dd\') < TO_CHAR (SYSDATE, \'yyyy-mm-dd\')'

    def getdate(self, n):
        date = str(datetime.datetime.now() + datetime.timedelta(days=n))[0:10]
        return date

    def getFromDB(self, model):
        try:
            db = jaydebeapi.connect(self.sql, [self.url, self.user, self.password], self.jarFile)
            curs = db.cursor()
            sqlx = self.sql + 'AND RS.SENSAREAID IN ( SELECT MH.AREACODE FROM MC_HUBSENSITIVEAREAINFO MH WHERE MH.UNITID = \'' + model + '\' )'
            curs.execute(sqlx)
            result = curs.fetchall()
        finally:
            db.close()

        for i in range(len(result) - 1):
            data = result[i][2][0:13]
            # print(data)
            self.dataEnter[data] = result[i][0]
            self.dataLeave[data] = result[i][1]
            pass

        self.x7.append(self.dataEnter.get(self.getdate(-31) + ' 21'))
        self.x7.append(self.dataEnter.get(self.getdate(-31) + ' 22'))
        self.x7.append(self.dataEnter.get(self.getdate(-31) + ' 23'))
        self.x8.append(self.dataEnter.get(self.getdate(-31) + ' 22'))
        self.x8.append(self.dataEnter.get(self.getdate(-31) + ' 23'))
        self.x9.append(self.dataEnter.get(self.getdate(-31) + ' 23'))
        for i1 in range(30):
            for i2 in range(24):
                self.x1.append(self.dataEnter.get(self.getdate(-51 + i1) + (" %02d" % i2)))
                self.x2.append(self.dataEnter.get(self.getdate(-44 + i1) + (" %02d" % i2)))
                self.x3.append(self.dataEnter.get(self.getdate(-37 + i1) + (" %02d" % i2)))
                self.x4.append(self.dataEnter.get(self.getdate(-33 + i1) + (" %02d" % i2)))
                self.x5.append(self.dataEnter.get(self.getdate(-32 + i1) + (" %02d" % i2)))
                self.x6.append(self.dataEnter.get(self.getdate(-31 + i1) + (" %02d" % i2)))
                self.x7.append(self.dataEnter.get(self.getdate(-30 + i1) + (" %02d" % i2)))
                self.x8.append(self.dataEnter.get(self.getdate(-30 + i1) + (" %02d" % i2)))
                self.x9.append(self.dataEnter.get(self.getdate(-30 + i1) + (" %02d" % i2)))
                self.y.append(self.dataEnter.get(self.getdate(-30 + i1) + (" %02d" % i2)))
        self.x7.pop()
        self.x7.pop()
        self.x7.pop()
        self.x8.pop()
        self.x8.pop()
        self.x9.pop()
        self.lastWeekAmount = np.vstack((self.x1, self.x2, self.x3))
        self.lastDayAmount = np.vstack((self.x4, self.x5, self.x6))
        self.lastHourAmount = np.vstack((self.x7, self.x8, self.x9))
        self.actualAmount = np.array(self.y).T

    def getlastWeekAmount(self):
        return self.lastWeekAmount

    def getlastDayAmount(self):
        return self.lastDayAmount

    def getlastHourAmount(self):
        return self.lastHourAmount

    def getactualAmount(self):
        return self.actualAmount

# X = np.vstack((x1, x2, x3, x4, x5, x6, x7, x8, x9)).T
# print(X[-1])
# print(len(X))
# Y = np.array(y).T
# print(Y[-1])
