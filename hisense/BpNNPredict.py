# -*- coding: utf-8 -*-
from sklearn.externals import joblib


def predict(X):
    clf = joblib.load("../model/BpNN.m")
    result = clf.predict(X)
    return result
