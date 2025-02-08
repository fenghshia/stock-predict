# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : akshare-data.py
# @Time        : 2025/2/8 下午3:00
# @IDE         : PyCharm
# @Description : Input Here
# --*-- Author : FengHShia --*--
import os
import pandas as pd
import akshare as aks
from datetime import date


# 创建本地数据缓存
today = date.today()
today_str = today.strftime("%Y%m%d")
cache_path = './data-cache/{}'.format(today_str)
if not os.path.exists(cache_path):
    os.makedirs(cache_path)
    print('new cache dir: {}'.format(cache_path))
# 保存美股全股票数据
if not os.path.exists("{}/stocks.csv".format(cache_path)):
    stocks = aks.stock_us_spot_em()
    stocks.to_csv("{}/stocks.csv".format(cache_path), index=False)
    print('saved stocks data')
else:
    print('stocks data exists')
# 保存指定的股票K线数据
stock_code = "105.AAPL"
if not os.path.exists("{}/{}.csv".format(cache_path, stock_code)):
    stock_k_data = aks.stock_us_hist(
        symbol=stock_code, period='daily', start_date='20200101', adjust='qfq')
    stock_k_data = stock_k_data.to_csv("{}/{}.csv".format(cache_path, stock_code), index=False)
    print('saved stock({}) k data'.format(stock_code))
else:
    print('stock({}) k data exists'.format(stock_code))
