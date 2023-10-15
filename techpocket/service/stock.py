class Stock:
    def __init__(self, _request):
        self._request = _request

    def get_list(self, key: str) -> dict:
        '''
        [Parameters]
        ------------
        key: str
            '上市股票', '上市權證', '上市ETF', '上市TDR', '上市受益證券', '上櫃股票', '上櫃權證', '上櫃ETF', '上櫃受益證券', '興櫃股票', '上市櫃ETN'

        [Returns]
        ------------
        return: pd.DataFrame
            'ISIN_code', 'industry', 'market', 'name', 'publish_date', 'stock_id', 'type'
        '''
        res = self._request('stock/list', 0, key=key)

        if res['status']['code'] == 200:
            res.pop('status', None)
            return res

        raise Exception(res['status']['msg'])

    def get_ticks_realtime(self, stock_id: str) -> dict:
        '''
        [Parameters]
        ------------
        stock_id: str
            'TSE', 'OTC', stock_id

        [Returns]
        ------------
        return: pd.DataFrame
            'time', 'price', 'amount', 'volume'
        '''
        res = self._request('stock/ticks_realtime', 0, stock_id=stock_id)

        if res['status']['code'] == 200:
            res.pop('status', None)
            return res

        raise Exception(res['status']['msg'])

    def get_price_realtime(self, stock_list: list) -> dict:
        '''
        [Parameters]
        ------------
        stock_id: list
            stock_ids, len(stock_id) <= 25

        [Returns]
        ------------
        return: pd.DataFrame
            'stock_id'
                'max', 'min', 'open', 'close', 'spread', 'amount', 'volume', 'volume_last'
        '''
        res = self._request('stock/price_realtime', 0, stock_list=stock_list)

        if res['status']['code'] == 200:
            res.pop('status', None)
            return res

        raise Exception(res['status']['msg'])
