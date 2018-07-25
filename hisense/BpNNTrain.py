# -*- coding: utf-8 -*-
import configparser
import jaydebeapi
from sklearn.externals import joblib
from sklearn.neural_network import MLPRegressor
import pandas as pd

'''
bpNN即 bp神经网络
'''
# 配置数据库
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
    sqlx = 'select "six","seven" from DATAPASSEGNER WHERE "id">7 ORDER BY "id" '
    curs.execute(sqlx)
    resultx = curs.fetchall()
    sqly = 'select "passengerf" from DATAPASSEGNER WHERE "id">7 ORDER BY "id" '
    curs.execute(sqly)
    resulty = curs.fetchall()

finally:
    db.close()

X = pd.DataFrame(list(resultx))  # 根据测试，选用之前2天的客流数据作为输入
print(X)
Y = pd.DataFrame(list(resulty))  # 当天的客流数据
print(Y)
# 数据集
clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=10, random_state=1)  # 根据测试，中间层数选用10层
clf.fit(X, Y)  # 数据训练
joblib.dump(clf, "../model/BpNN.m")

# result = clf.predict(X)  # 结果预测

# y = Y.values  # 预测结果

# # 求平均差值比
# differ = (sum(abs(y - result))) / (sum(y)) * 100  # 所有结果平局差值*100
# print("平均差值比=%f\n" % differ)
#
# # 求最大差值比
# ans = (y - result)
# absans = abs(ans)
# print("最大差值量=%f" % max(absans))  # 输出最大差值量
# differ = max(absans) / (y[np.argmax(absans)]) * 100  # 结果中最大的差值
# print("最大差值位置=%d" % np.argmax(absans))  # 输出最大差值位置
# print("最大差值比=%f\n" % differ)
#
# # 求最小差值比
# ans = (y - result)
# absans = abs(ans)
# print("最小差值量%f" % min(absans))  # 输出最小差值量
# differ = min(absans) / (y[np.argmin(absans)]) * 100  # 结果中最小的差值
# print("最小差值位置=%d" % np.argmin(absans))  # 输出最小差值位置
# print("最小差值比=%f\n" % differ)
#
# # 绘图
# plt.plot(np.arange(len(result)), y, 'go-', label='true value')  # 实际客流量，绿色
# plt.plot(np.arange(len(result)), result, 'ro-', label='predict value')  # 预测客流量，红色
# plt.show()
