# -*- coding: utf-8 -*-
from sklearn.externals import joblib


class UniversalPredict(object):
    def __init__(self, model, X_nextHour, X):
        self.model = model  # 要预测的模型
        self.X_nextHour = X_nextHour
        self.X = X

    def predict(self):
        clf1 = joblib.load("../model/" + self.model + "_NextHour.m")
        resultNextHour = clf1.predict(self.X_nextHour)
        clf2 = joblib.load("../model/" + self.model + ".m")
        resultOther = clf2.predict(self.X)
        result = clf1 + clf2
        return result
