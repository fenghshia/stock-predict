import akshare as ak


class Stocks:

    data = ak.stock_us_spot_em()

    @classmethod
    def search(cls, **kwargs):
        if len(kwargs) == 0:
            raise SearchRageZero()
        if len(kwargs) > 1:
            raise TooManyKeys(kwargs)
        column_name = list(kwargs.keys())[0]
        s_str = kwargs[column_name]
        if column_name not in cls.data.columns:
            raise ColumnNotExist(cls.data.columns, column_name)
        return cls.data[cls.data[column_name].map(lambda x: s_str in x.lower())]

    @classmethod
    def reflash(cls):
        cls.data = ak.stock_us_spot_em()


class SearchRageZero(Exception):

    def __str__(self):
        return '未输入查询项, 格式: <查询列名>=<匹配项>'


class TooManyKeys(Exception):

    def __init__(self, kwargs):
        self.search_key = kwargs

    def __str__(self):
        return '输入过多查询项, 仅支持查询1项. 当前查询项: {}'.format(self.search_key)


class ColumnNotExist(Exception):

    def __init__(self, columns: list, column_name: str):
        self.columns = columns
        self.column_name = column_name

    def __str__(self):
        return '输入的查询列不存在.\nDataform列 : {}\n查询列 : {}'.format(
            ' | '.join(self.columns), self.column_name
        )


if __name__ == '__main__':
    print(Stocks.data.head())
    stocks = Stocks.search(名称x='woods')
    print(stocks)
