# -*- coding: utf-8 -*-
from functools import reduce
import numpy as np
from sklearn.externals import joblib

"""
该文件用于对数据进行多元新型回归的预测
输入前一年的特征以及前一年的实际客流量，通过模型记性
"""


def predict(X_test12, y_test12, X_test13, y_test13):
    # 模型拟合测试集
    linreg = joblib.load("../model/MulRegression.m")
    y_pred = linreg.predict(X_test12)

    # 补全差值
    predict_List = np.array(y_pred[-2:])  # 12年预测值
    Actual_List = np.array(y_test12[-2:])  # 12年实际值
    y_predict = []
    ite = 0

    # 通过差值靠近真实值
    for i in range(10):
        # 加最近变化数据预测
        y_complement = Actual_List - predict_List
        y_complement_average = reduce(lambda x, y: x + y, y_complement) / len(y_complement)
        x_test = X_test13.iloc[i]
        temp = linreg.predict([x_test])  # 算法算出的预测值
        predictactual = temp[0] + y_complement_average  # 补全差值后的预测值

        # 更新近预测值
        y_predict.append(predictactual)
        predict_List = np.delete(predict_List, 0)
        predict_List = np.append(predict_List, [predictactual])

        # 更新最近实际值
        Actual_List = np.delete(Actual_List, 0)
        y_true = y_test13.ix[ite]
        Actual_List = np.append(Actual_List, [y_true])
        ite += 1
    return y_predict
