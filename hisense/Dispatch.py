# -*- coding: utf-8 -*-
import hisense.MultipleRegressionPredict as MultipleRegressionPredict
import hisense.BpNNPredict as BpNNPredict
import hisense.WaitTimeSimplify as WaitTimeSimplify
from hisense.DayPassengerDate import *
from hisense.BpNNPassengerDate import *
from hisense.vehicleTrain.AirportBus import AirportBusTrain
from hisense.vehicleTrain.Aviation import AviationTrain
from hisense.vehicleTrain.Bus import BusTrain
from hisense.vehicleTrain.Coach import CoachTrain
from hisense.vehicleTrain.PrivateCar import PrivateCarTrain
from hisense.vehicleTrain.Subway import SubwayTrain
from hisense.vehicleTrain.Taxi import TaxiTrain
from hisense.util.UniversalPassengerDate import UniversalPassengerDate
from hisense.util.UniversalTrainData import UniversalTrainData


class Dispatch(object):

    def dayPassengerToDatabase(self):
        dayPassengerDate = DayPassengerDate()
        TrafficSend = MultipleRegressionPredict.predict(dayPassengerDate.getlastyearfeature(),
                                                        dayPassengerDate.getlastyearresult(),
                                                        dayPassengerDate.getpredictfeature(),
                                                        dayPassengerDate.getpredictresult())
        print("查询日客流量")

    def bpNNPassengerDateToDatabase(self):
        temp = BpNNPassengerDate()
        TrafficSend = BpNNPredict.predict(temp.getHistorical())
        print("查询小时客流量")

    def waitTimeToDatebase(self):
        mark = WaitTimeSimplify.WaitTimeSimplify(80, 20, 300, 2)
        time = mark.judge()
        print("候车时间查询")

    def airportBusDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('8')
            lastDayAmount = universalPassengerDate.getLastDayAmount('8')
            lastHourAmount = universalPassengerDate.getLastHourAmount('8')
            actualAmount = universalPassengerDate.getActualAmount('8')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('8')
            lastDayAmount = universalPassengerDate.getLastHoursList('8')
        # todo: 参数需要修改
        airportBusTrain = AirportBusTrain(lastWeekAmount, lastDayAmount, lastHourAmount)
        airportBusTrain.predict()

    def aviationTrainDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('6')
            lastDayAmount = universalPassengerDate.getLastDayAmount('6')
            lastHourAmount = universalPassengerDate.getLastHourAmount('6')
            actualAmount = universalPassengerDate.getActualAmount('6')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('6')
            lastDayAmount = universalPassengerDate.getLastHoursList('6')
        aviationTrain = AviationTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        aviationTrain.predict()

    def busTrainDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('1')
            lastDayAmount = universalPassengerDate.getLastDayAmount('1')
            lastHourAmount = universalPassengerDate.getLastHourAmount('1')
            actualAmount = universalPassengerDate.getActualAmount('1')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('1')
            lastDayAmount = universalPassengerDate.getLastHoursList('1')
        busTrain = BusTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        busTrain.predict()

    def coachTrainDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('5')
            lastDayAmount = universalPassengerDate.getLastDayAmount('5')
            lastHourAmount = universalPassengerDate.getLastHourAmount('5')
            actualAmount = universalPassengerDate.getActualAmount('5')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('5')
            lastDayAmount = universalPassengerDate.getLastHoursList('5')
        coachTrain = CoachTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        coachTrain.predict()

    def privateCarTrainDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('7')
            lastDayAmount = universalPassengerDate.getLastDayAmount('7')
            lastHourAmount = universalPassengerDate.getLastHourAmount('7')
            actualAmount = universalPassengerDate.getActualAmount('7')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('7')
            lastDayAmount = universalPassengerDate.getLastHoursList('7')
        privateCarTrain = PrivateCarTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        privateCarTrain.predict()

    def subwayTrainDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('2')
            lastDayAmount = universalPassengerDate.getLastDayAmount('2')
            lastHourAmount = universalPassengerDate.getLastHourAmount('2')
            actualAmount = universalPassengerDate.getActualAmount('2')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('2')
            lastDayAmount = universalPassengerDate.getLastHoursList('2')
        subwayTrain = SubwayTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        subwayTrain.predict()

    def taxiTrainDatebase(self, Type):
        universalPassengerDate = UniversalPassengerDate()
        if Type == 'Day':
            lastWeekAmount = universalPassengerDate.getLastWeekAmount('3')
            lastDayAmount = universalPassengerDate.getLastDayAmount('3')
            lastHourAmount = universalPassengerDate.getLastHourAmount('3')
            actualAmount = universalPassengerDate.getActualAmount('3')
        if Type == 'Hour':
            lastWeekAmount = universalPassengerDate.getLastWeeksList('3')
            lastDayAmount = universalPassengerDate.getLastHoursList('3')
        taxiTrain = TaxiTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        taxiTrain.predict()

    def airportBusTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('8')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastDayAmount()
        lastHourAmount = universalTrainData.getlastDayAmount()
        actualAmount = universalTrainData.getactualAmount()
        airportBusTrain = AirportBusTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        airportBusTrain.train()
        pass

    def aviationTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('6')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastDayAmount()
        lastHourAmount = universalTrainData.getlastHourAmount()
        actualAmount = universalTrainData.getactualAmount()
        aviationTrain = AviationTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        aviationTrain.train()
        pass

    def busTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('1')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastDayAmount()
        lastHourAmount = universalTrainData.getlastHourAmount()
        actualAmount = universalTrainData.getactualAmount()
        busTrain = BusTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        busTrain.train()
        pass

    def coachTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('5')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastDayAmount()
        lastHourAmount = universalTrainData.getlastHourAmount()
        actualAmount = universalTrainData.getactualAmount()
        coachTrain = CoachTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        coachTrain.train()
        pass

    def privateCarTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('7')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastDayAmount()
        lastHourAmount = universalTrainData.getlastHourAmount()
        actualAmount = universalTrainData.getactualAmount()
        privateCarTrain = PrivateCarTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        privateCarTrain.train()
        pass

    def subwayTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('2')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastDayAmount()
        lastHourAmount = universalTrainData.getlastHourAmount()
        actualAmount = universalTrainData.actualAmount
        subwayTrain = SubwayTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        subwayTrain.train()
        pass

    def taxiTrain(self):
        universalTrainData = UniversalTrainData()
        universalTrainData.getFromDB('3')
        lastWeekAmount = universalTrainData.getlastWeekAmount()
        lastDayAmount = universalTrainData.getlastWeekAmount()
        lastHourAmount = universalTrainData.getlastHourAmount()
        actualAmount = universalTrainData.getactualAmount()
        taxiTrain = TaxiTrain(lastWeekAmount, lastDayAmount, lastHourAmount, actualAmount)
        taxiTrain.train()
        pass

    def dispatch(self, requestType):
        if requestType == 'RegularHour':
            self.airportBusDatebase('Hour')
            self.aviationTrainDatebase('Hour')
            self.busTrainDatebase('Hour')
            self.coachTrainDatebase('Hour')
            self.privateCarTrainDatebase('Hour')
            self.subwayTrainDatebase('Hour')
            self.taxiTrainDatebase('Hour')
            pass
        elif requestType == 'RegularDay':
            self.airportBusDatebase('Day')
            self.aviationTrainDatebase('Day')
            self.busTrainDatebase('Day')
            self.coachTrainDatebase('Day')
            self.privateCarTrainDatebase('Day')
            self.subwayTrainDatebase('Day')
            self.taxiTrainDatebase('Day')
            pass
        elif requestType == 'TrainAllDate':
            self.airportBusTrain()
            self.aviationTrain()
            self.busTrain()
            self.coachTrain()
            self.privateCarTrain()
            self.subwayTrain()
            self.taxiTrain()
            pass
        elif requestType == 'requestDAYDate':
            self.dayPassengerToDatabase()
        elif requestType == 'requestHourDate':
            self.bpNNPassengerDateToDatabase()
        elif requestType == 'requestWaiterTimeDate':
            self.waitTimeToDatebase()
