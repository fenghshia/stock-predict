# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : akshare-data.py
# @Time        : 2025/2/8 下午3:00
# @IDE         : PyCharm
# @Description : Input Here
# --*-- Author : FengHShia --*--
import os
import akshare as aks
from datetime import date

import pandas as pd


class AkshareData:

    # 创建本地数据缓存
    today = date.today()
    today_str = today.strftime("%Y%m%d")

    @property
    def cache_path(self) -> str:
        cache_path = './data-cache/{}'.format(self.today_str)
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
            print('new cache dir: {}'.format(cache_path))
        return cache_path

    @property
    def stocks_data(self) -> pd.DataFrame:
        # 保存美股全股票数据
        if not os.path.exists("{}/stocks.csv".format(self.cache_path)):
            stocks = aks.stock_us_spot_em()
            stocks.to_csv("{}/stocks.csv".format(self.cache_path), index=False)
            print('saved stocks data')
        else:
            stocks = pd.read_csv("{}/stocks.csv".format(self.cache_path))
            print('stocks data exists')
        return stocks

    def stock_k_data(self, stock_code: str) -> pd.DataFrame:
        # 保存指定的股票K线数据
        if not os.path.exists("{}/{}.csv".format(self.cache_path, stock_code)):
            stock_k_data = aks.stock_us_hist(
                symbol=stock_code, period='daily', start_date='20200101', adjust='qfq')
            stock_k_data.to_csv("{}/{}.csv".format(self.cache_path, stock_code), index=False)
            print('saved stock({}) k data'.format(stock_code))
        else:
            stock_k_data = pd.read_csv("{}/{}.csv".format(self.cache_path, stock_code))
            print('stock({}) k data exists'.format(stock_code))
        return stock_k_data


if __name__ == '__main__':
    ak_data = AkshareData()
    print(ak_data.today)
    print(ak_data.today_str)
    print(ak_data.cache_path)
    print(ak_data.stocks_data)
    print(ak_data.stock_k_data("105.AAPL"))
