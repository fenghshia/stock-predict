import akshare as ak


class Stocks:

    data = ak.stock_us_spot_em()

    @classmethod
    def search(cls, **kwargs):
        if len(kwargs) == 0:
            raise SearchRageZero()
        if len(kwargs) > 1:
            raise TooManyKeys()
        column_name = list(kwargs.keys())[0]
        s_str = kwargs[column_name]
        if column_name not in cls.data.columns:
            raise ColumnNotExist()
        return cls.data[cls.data[column_name].map(lambda x: s_str in x.lower())]

    @classmethod
    def reflash(cls):
        cls.data = ak.stock_us_spot_em()


class SearchRageZero(Exception):
    pass


class TooManyKeys(Exception):
    pass


class ColumnNotExist(Exception):
    pass


if __name__ == '__main__':
    print(Stocks.data.head())
    stocks = Stocks.search(名称='woods')
    print(stocks)
