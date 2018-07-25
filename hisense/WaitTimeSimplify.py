# -*- coding: utf-8 -*-
# 原算法简化版本
class WaitTimeSimplify(object):
    '''
    出租车候车时间算法（实际情况简化版）
    Ttotal：蓄车池出租车保有量
    Tway：单次放行车辆数
    Pt：候车点乘客数量
    AT：临时调度出租车的倒车最短时间
    delta：出租车平均载客量
    m：上车区的泊位数
    '''

    # 构造函数
    def __init__(self, Ttotal, Tway, Pt, AT, m=2, delta=2):
        # 计算可调度总公交数量
        self.Ttotal = Ttotal
        self.Tway = Tway
        self.Pt = Pt
        self.delta = delta
        self.AT = AT
        self.m = m
        self.totalCarNum = ((self.Ttotal + self.Tway) * self.delta)

    # 判断目前的排队状态
    def judge(self, BT=20):  # 出租车平均服务时间为BT，暂时定位20
        if self.Pt <= self.totalCarNum:
            print("出租车运力充足")
            return self.waitTime(BT)
        else:
            print("出租车运力不充足")
            return self.waitTime(BT) + self.AT

    # 计算当前显示器显示的等待时间
    def waitTime(self, BT):
        WT = BT * self.Pt / (self.delta * self.m)
        return WT
