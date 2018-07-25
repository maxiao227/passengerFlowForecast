# -*- coding: utf-8 -*-
"""
出租车客流预测
"""
from sklearn.externals import joblib
from sklearn.neural_network import MLPRegressor
import numpy as np

from hisense.util.Python2DataBase import Python2DataBase


class TaxiTrain(object):
    def __init__(self, lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount):
        # self.lastWeekAmount = lastWeekAmount
        # self.lastDayAmount = lastDayAmount
        # self.lastHourAmount = lastHourAmount
        self.actualAmount = actualAmount
        self.X_NextHour = np.hstack((lastWeekAmount, lastDayAmount, lastHourAmount))
        self.X = np.hstack((lastWeekAmount, lastDayAmount))
        self.X_NextWeek = lastWeekAmount
        pass

    def train(self):
        clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10, random_state=1)  # 根据测试，中间层数选用10层
        clf.fit(self.X, self.actualAmount.values.ravel())  # 数据训练
        joblib.dump(clf, "../model/TaxiTrain.m")

        clf.fit(self.X_NextHour, self.actualAmount.values.ravel())  # 数据训练
        joblib.dump(clf, "../model/TaxiTrain_NextHour.m")

        clf.fit(self.X_NextWeek, self.actualAmount.values.ravel())  # 数据训练
        joblib.dump(clf, "../model/TaxiTrain_NextWeek.m")
        pass

    def predict(self):
        python2DataBase = Python2DataBase()
        clf = joblib.load("../model/TaxiTrain_NextHour.m")
        result_NextHour = clf.predict(self.X_NextHour)
        python2DataBase.set2DataBaseNextHour(result_NextHour, 18)

        clf = joblib.load("../model/TaxiTrain.m")
        result_currentDay = clf.predict(self.X)
        python2DataBase.set2DataBaseCurrentDay(result_currentDay, 18)

        clf = joblib.load("../model/TaxiTrain_NextWeek.m")
        result_NextWeek = clf.predict(self.X_NextWeek)
        python2DataBase.set2DataBaseCurrentWeek(result_NextWeek, 18)
