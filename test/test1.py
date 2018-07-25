# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def TrueFalseListCombine(TFlist1, TFlist2):
    return [l1 and l2 for l1, l2 in zip(TFlist1, TFlist2)]


ts_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
Mean = pd.DataFrame([np.mean(i) for i in ts_list])
mean_low = Mean > Mean.quantile(0.1)
mean_up = Mean < Mean.quantile(0.9)
TF = TrueFalseListCombine(mean_low.values, mean_up.values)
mean_index = Mean[TF].index.values
Std = pd.DataFrame([np.std(i) for i in ts_list])
std_low = Std > Std.quantile(0.1)
std_up = Std < Std.quantile(0.9)
TF = TrueFalseListCombine(std_low.values, std_up.values)
std_index = Std[TF].index.values
valid_index = list(set(mean_index) & set(std_index))
# print(set(mean_index))
# print(valid_index)
a=list(set([1,2,3])&set([2,3,4]))
print(a)
