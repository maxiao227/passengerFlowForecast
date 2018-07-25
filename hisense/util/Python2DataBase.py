# -*- coding: utf-8 -*-
import configparser
import uuid
import datetime


class Python2DataBase(object):
    Config = configparser.ConfigParser()
    Config.read('../model/dbconfig.conf')
    dirver = Config.get('DATABASE', 'dirver')
    url = Config.get('DATABASE', 'url')
    user = Config.get('DATABASE', 'user')
    password = Config.get('DATABASE', 'password')
    jarFile = Config.get('DATABASE', 'jarFile')
    sql = 'INSERT INTO REC_SENSEAREAFORCECASTDATA ( ID, PFDATATYPE, ACTTIME, RECTIME, PFDATA2 ) VALUES '

    def set2DataBaseNextHour(self, result, model):
        uuidValue = uuid.uuid1()
        predictTime = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y/%m/%d %H:%M:%S")
        executeSql = self.sql + '( \'' + uuidValue + '\', \'' + str(model) + '\', ' + predictTime + ', SYSDATE,\'' + str(
            result) + '\')'

    def set2DataBaseCurrentDay(self, result, model):
        uuidValue = uuid.uuid1()
        for i in range(22):
            predictResult = result[i]
            predictTime = (datetime.datetime.now() + datetime.timedelta(hours=(2 + i))).strftime("%Y/%m/%d %H:%M:%S")
            executeSql = self.sql + '( \'' + uuidValue + '\', \'' + str(model) + '\', ' + predictTime + ', SYSDATE,\'' + str(
                predictResult) + '\')'

    def set2DataBaseCurrentWeek(self, result, model):
        uuidValue = uuid.uuid1()
        for i in range(144):
            predictResult = result[24 + i]
            predictTime = (datetime.datetime.now() + datetime.timedelta(hours=(25 + i))).strftime("%Y/%m/%d %H:%M:%S")
            executeSql = self.sql + '( \'' + uuidValue + '\', \'' + str(model) + '\', ' + predictTime + ', SYSDATE,\'' + str(
                predictResult) + '\')'
        for iter1 in range(3):
            for iter2 in range(168):
                predictResult = result[iter2]
                weekHour = (iter1 + 1) * 7 * 24
                predictTime = (datetime.datetime.now() + datetime.timedelta(hours=(weekHour + iter2))).strftime(
                    "%Y/%m/%d %H:%M:%S")
                executeSql = self.sql + '( \'' + uuidValue + '\', \'' + str(
                    model) + '\', ' + predictTime + ', SYSDATE,\'' + str(
                    predictResult) + '\')'
