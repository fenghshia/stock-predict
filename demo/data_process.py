# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : data_process.py
# @Time        : 2025/2/8 下午3:26
# @IDE         : PyCharm
# @Description : Input Here
# --*-- Author : FengHShia --*--
import os
import numpy as np
import pandas as pd
import tensorflow as tf
from datetime import date
from sklearn.preprocessing import MinMaxScaler
from akshare_data import AkshareData as aksd


class NormalizationAndSplit():

    aksd = aksd()
    sc = MinMaxScaler(feature_range=(0, 1))
    # 归一化
    stock_close_prices_log = sc.fit_transform(aksd.stock_k_data("105.AAPL").iloc[:, 2:3].values)
    seed = 7

    @property
    def train_split(self):
        return self.stock_close_prices_log[:-300]

    @property
    def test_split(self):
        return self.stock_close_prices_log[-300:]

    def train_data_orgnize(self):
        x_train_data_set = list()
        y_train_data_set = list()
        for i in range(60, len(self.train_split)):
            x_train_data_set.append(self.train_split[i - 60:i, 0])
            y_train_data_set.append(self.train_split[i, 0])
        return x_train_data_set, y_train_data_set

    def test_data_orgnize(self):
        x_test_data_set = list()
        y_test_data_set = list()
        for i in range(60, len(self.test_split)):
            x_test_data_set.append(self.test_split[i - 60:i, 0])
            y_test_data_set.append(self.test_split[i, 0])
        return np.array(x_test_data_set), np.array(y_test_data_set)

    def train_data_random(self):
        x_train_data_set, y_train_data_set = self.train_data_orgnize()
        np.random.seed(self.seed)
        np.random.shuffle(x_train_data_set)
        np.random.seed(self.seed)
        np.random.shuffle(y_train_data_set)
        return np.array(x_train_data_set), np.array(y_train_data_set)

    def data_save(self):
        x_train_data_set, y_train_data_set = self.train_data_random()
        x_test_data_set, y_test_data_set = self.test_data_orgnize()
        np.save('{}/x_train_data_set.npy'.format(self.aksd.cache_path), x_train_data_set)
        np.save('{}/y_train_data_set.npy'.format(self.aksd.cache_path), y_train_data_set)
        np.save('{}/x_test_data_set.npy'.format(self.aksd.cache_path), x_test_data_set)
        np.save('{}/y_test_data_set.npy'.format(self.aksd.cache_path), y_test_data_set)


if __name__ == '__main__':
    NormalizationAndSplit().data_save()
