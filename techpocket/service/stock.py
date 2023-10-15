import pandas as pd

from techpocket.error import TechPocketApi


class Stock(TechPocketApi):
    def __init__(self, token):
        self._token = token

    def get_list(self, key: str) -> pd.DataFrame:
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

        res = self._request('stock/list', self._token, key=key)

        df = pd.DataFrame(
            {'ISIN_code': [], 'industry': [], 'market': [],
             'name': [], 'publish_date': [], 'stock_id': [], 'type': []}
        )

        if 'data_list' in res and res['data_list']:
            df = pd.DataFrame(res['data_list'])

        return df

    def get_ticks_realtime(self, stock_id: str) -> pd.DataFrame:
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

        res = self._request('stock/ticks_realtime', self._token, stock_id=stock_id)

        df = pd.DataFrame(
            {'time': [], 'price': [], 'amount': [], 'volume': []}
        )

        if 'data_list' in res and res['data_list']:
            df = pd.DataFrame(res['data']['ticks'])

        return df

    def get_price_realtime(self, stock_list: list) -> pd.DataFrame:
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

        res = self._request('stock/price_realtime', self._token, stock_list=stock_list)

        df = pd.DataFrame(
            {'max': [], 'min': [], 'open': [], 'close': [], 'spread': [], 'amount': [], 'volume': [], 'volume_last': []}
        )

        if 'data_list' in res and res['data_list']:
            df = pd.DataFrame(res['data_list'])

        return df
