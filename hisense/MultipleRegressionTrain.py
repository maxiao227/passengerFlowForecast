# -*- coding: utf-8 -*-
import configparser

import jaydebeapi
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

'''
多元线性回归 用于预测日客流量
'''
# 读取数据库
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

# 调用线性回归模型
linreg = LinearRegression()
linreg.fit(X_test12, y_test12)
joblib.dump(linreg, "../model/MulRegression.m")

# #打印回归参数
# print(linreg.intercept_)
# print(linreg.coef_)
#
# # 模型拟合测试集
# y_pred = linreg.predict(X_test13)
#
#
# # 补全差值
# differvalue = np.array(y_pred[-2:].tolist())  # 12年预测值
# y_actualvalue = np.array(y_test12[-2:].tolist())  # 12年实际值
# y_predict = []
# ite = 0
#
# # 通过差值靠近真实值
# for i in range(114):
#     # 加4天变化数据预测
#     y_complement = y_actualvalue - differvalue
#     y_complement_average = reduce(lambda x, y: x + y, y_complement) / len(y_complement)
#     x_test = X_test13.iloc[i, 0:]
#     temp = linreg.predict([x_test])
#     predictactual = temp[0] + y_complement_average
#
#     # 更新近4天预测值
#     y_predict.append(predictactual)
#     differvalue = np.delete(differvalue, 0)
#     differvalue = np.append(differvalue, [predictactual])
#
#     # 更近近4天实际值
#     y_actualvalue = np.delete(y_actualvalue, 0)
#     y_true = y_test13.ix[290 + ite]
#     y_actualvalue = np.append(y_actualvalue, [y_true])
#     ite += 1
# # print(y_predict)
#
# # 绘制对比曲线
# plt.plot(date13, y_test13, "x-", label="真实")
# plt.plot(date13, y_predict, "+-", label="预测")
# plt.show()
#
# # 平均差值
# averageDiffer = sum(abs(y_test13 - y_predict)) / sum(y_test13) * 100
# print("average=%f\n" % averageDiffer)
#
# # 最大差值
# maxNum = max(abs(y_test13 - y_predict))
# print("the maxNum=%f" % maxNum)
# maxLocationy = y_test13[np.argmax(abs(y_test13 - y_predict))]
# maxDiffer = (maxNum / maxLocationy) * 100
# print("maxdiffer=%f\n" % maxDiffer)
#
# # 最小差值
# minNum = min(abs(y_test13 - y_predict))
# print("the minNum=%f" % minNum)
# minLocationy = y_test13[np.argmin(abs(y_test13 - y_predict))]
# minDiffer = (minNum / minLocationy) * 100
# print("mindiffer%f\n" % minDiffer)
#
# # 用scikit-learn计算MSE
# print("MSE:", metrics.mean_squared_error(y_test13, y_predict))
# # 用scikit-learn计算RMSE
# print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test13, y_predict)))
