# -*- coding: utf-8 -*-
class WaitTime(object):
    '''
    出租车候车时间算法（文档完整版）
    Ttotal:蓄车池出租车保有量
    Tway：单次放行车辆数
    Pt：候车点乘客数量
    P：显示屏之间的乘客数量，list格式，对应方案中的Pt(1)和Pt(i)
    AT:临时调度出租车的倒车最短时间
    delta：出租车平均载客量
    i：第i个显示屏
    m：上车区的泊位数
    '''

    # 构造函数
    def __init__(self, Ttotal, Tway, Pt, P, AT, delta=2):
        # 计算可调度总公交数量
        self.Ttotal = Ttotal
        self.Tway = Tway
        self.Pt = Pt  # 候车点乘客数量
        self.P = P  # 每个牌子下对应的候车人数
        self.delta = delta
        self.AT = AT
        self.totalCarNum = ((self.Ttotal + self.Tway) * self.delta)

    # 计算当前第i个显示器显示的等待时间
    def waitTime(self, i, m, BT=20):
        tempSum = 0
        for ite in range(i):
            tempSum += self.P[ite]
        WT = BT * tempSum / (self.delta * m)
        return WT

    # 判断运力正常的显示器位置
    def normalQueue(self):
        tempSum = 0
        for i, element in enumerate(self.P):
            tempSum += element
            if tempSum > self.totalCarNum:
                break
        return i

    # 判断目前的排队状态
    def judge(self, i, m=2):  # 暂时让m=2
        if self.Pt <= self.totalCarNum:
            return self.waitTime(i, m)
        else:
            print("出租车运力不充足")
            middle = self.normalQueue()  # middle为中间值，代表能满足运力和不能满足运力显示器的交界
            print("阀值为%d" % middle)
            if i <= middle:
                print("时间不大于阀值")
                return self.waitTime(i, m)
            else:
                print("时间大于阀值")
                return self.waitTime(i, m) + self.AT
