# -*- coding: utf-8 -*-
import socket
import traceback
import json
from hisense.Dispatch import Dispatch
import threading
import time


# class NumpyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return json.JSONEncoder.default(self, obj)


class SocketServer(object):

    def detailRequst(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("连接成功")

            sock.bind(('localhost', 8001))
            print("绑定socket成功")

            sock.listen(5)
            print("监听成功")
        except Exception as e:
            print("出现异常")
            traceback.print_exc()
        while True:
            # 接受java带来的数据
            conn, addr = sock.accept()
            print("获取地址")
            print(addr)
            szBuf = conn.recv(1024)
            jsonData = json.loads(szBuf.decode())
            dispatchInstantiation = Dispatch()
            if jsonData['account'] == 'hisense' and jsonData['password'] == 'hisense2018':
                print(jsonData['model'])
                print(type(jsonData['model']))
                dispatchInstantiation.dispatch(jsonData['model'])
            conn.close()

    def timerRequst(self):
        while True:
            current_time = time.localtime(time.time())
            if (current_time.tm_hour == 0) and (current_time.tm_min == 0) and (current_time.tm_sec == 0):
                dispatchInstantiation = Dispatch()
                dispatchInstantiation.dispatch('requestAllDate')
            time.sleep(1)
        pass

    def trainRequst(self):
        while True:
            if time.strftime("%d") == '1':
                dispatchInstantiation = Dispatch()
                dispatchInstantiation.dispatch('TrainAllDate')
                pass

    def realTimePrediction(self):
        while True:
            if time.strftime("%M") == '00':
                dispatchInstantiation = Dispatch()
                dispatchInstantiation.dispatch('TrealTime')

    def startProject(self):
        t1 = threading.Thread(target=self.detailRequst, name="detailRequst")
        t2 = threading.Thread(target=self.timerRequst, name='timerRequst')
        t3 = threading.Thread(target=self.trainRequst, name='trainRequst')
        t4 = threading.Thread(target=self.realTimePrediction, name='realTimePrediction')
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()