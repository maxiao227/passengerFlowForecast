# -*- coding: utf-8 -*-
"""
机场巴士客流预测
"""
import os

from sklearn.externals import joblib
from sklearn.neural_network import MLPRegressor
import numpy as np
from hisense.util.Python2DataBase import Python2DataBase


class AirportBusTrain(object):
    def __init__(self, lastWeekAmount, lastDayAmount, lastHourAmount=None, actualAmount=None):
        # self.lastWeekAmount = lastWeekAmount
        # self.lastDayAmount = lastDayAmount
        # self.lastHourAmount = lastHourAmount
        self.actualAmount = actualAmount
        self.X_NextHour = np.hstack((lastWeekAmount, lastDayAmount, lastHourAmount))  # 下一小时的用此方法
        self.X = np.hstack((lastWeekAmount, lastDayAmount))  # 一小时后的用此方法
        self.X_NextWeek = lastWeekAmount  # 一天后的用此方法
        pass

    def train(self):
        clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10, random_state=1)  # 根据测试，中间层数选用10层
        clf.fit(self.X, self.actualAmount.ravel())  # 数据训练
        joblib.dump(clf, "../model/AirportBusTrain.m")

        clf.fit(self.X_NextHour, self.actualAmount.ravel())
        joblib.dump(clf, "../model/AirportBusTrain_NextHour.m")

        clf.fit(self.X_NextWeek, self.actualAmount.ravel())
        joblib.dump(clf, "../model/AirportBusTrain_NextWeek.m")
        pass

    def predict(self):
        python2DataBase = Python2DataBase()
        clf = joblib.load("../model/AirportBusTrain_NextHour.m")
        # todo:新数据导入到数据库中
        result_NextHour = clf.predict(self.X_NextHour)
        python2DataBase.set2DataBaseNextHour(result_NextHour, 18)
        # todo :从这里开始
        clf = joblib.load("../model/AirportBusTrain.m")
        result_currentDay = clf.predict(self.X)
        python2DataBase.set2DataBaseCurrentDay(result_currentDay, 18)

        clf = joblib.load("../model/AirportBusTrain_NextWeek.m")
        result_NextWeek = clf.predict(self.X_NextWeek)
        python2DataBase.set2DataBaseCurrentWeek(result_NextWeek, 18)
