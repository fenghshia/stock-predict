# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : normalization-and-split.py
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


# 加载股票数据
stock_code = "105.AAPL"
today = date.today()
today_str = today.strftime("%Y%m%d")
cache_path = './data-cache/{}'.format(today_str)
stock_k_data = '{}/{}.csv'.format(cache_path, stock_code)
if not os.path.exists(stock_k_data):
    print('stock({}) k data not exist, exit...'.format(stock_code))
    exit()
stock_k_data = pd.read_csv(stock_k_data)
# 数据归一化
stock_close_prices = stock_k_data.iloc[:, 2:3].values
sc = MinMaxScaler(feature_range=(0, 1))
stock_close_prices_log = sc.fit_transform(stock_close_prices)
print("normalization stock close prices :\n{}".format(stock_close_prices_log))
# 数据序列化
x_data_set = list()
y_data_set = list()
for i in range(60, len(stock_close_prices_log)):
    x_data_set.append(stock_close_prices_log[i - 60:i, 0])
    y_data_set.append(stock_close_prices_log[i, 0])
print("x data set :\n{}".format(x_data_set))
print("y data set :\n{}".format(y_data_set))
# 数据随机化
np.random.seed(7)
np.random.shuffle(x_data_set)
np.random.seed(7)
np.random.shuffle(y_data_set)
tf.random.set_seed(7)
# 切分数据
x_train_data_set = np.array(x_data_set[:-300])
x_test_data_set = np.array(x_data_set[-300:])
y_train_data_set = np.array(y_data_set[:-300])
y_test_data_set = np.array(y_data_set[-300:])
# 保存数据
np.save('./data-cache/x_train_data_set.npy', x_train_data_set)
np.save('./data-cache/x_test_data_set.npy', x_test_data_set)
np.save('./data-cache/y_train_data_set.npy', y_train_data_set)
np.save('./data-cache/y_test_data_set.npy', y_test_data_set)
