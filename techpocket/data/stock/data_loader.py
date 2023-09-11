import pandas as pd

from techpocket.techpocket_api.techpocket_api import TechPocketApi


class DataLoader(TechPocketApi):
    def __init__(self):
        super(DataLoader, self).__init__()

    def get_list(self, key: str) -> pd.DataFrame:
        """
        [Parameters]
        ------------
        key: str
            '上市股票', '上市權證', '上市ETF', '上市TDR', '上市受益證券', '上櫃股票', '上櫃權證', '上櫃ETF', '上櫃受益證券', '興櫃股票', '上市櫃ETN'

        [Returns]
        ------------
        return: pd.DataFrame
            'ISIN_code', 'industry', 'market', 'name', 'publish_date', 'stock_id', 'type'
        """
        pass

    def get_ticks_realtime(self, stock_id: str) -> pd.DataFrame:
        """
        [Parameters]
        ------------
        stock_id: str
            'TSE', 'OTC', stock_id

        [Returns]
        ------------
        return: pd.DataFrame
            'time', 'price', 'amount', 'volume'
        """
        pass

    def get_price_realtime(self, stock_list: list) -> pd.DataFrame:
        """
        [Parameters]
        ------------
        stock_id: list
            stock_ids, len(stock_id) <= 25

        [Returns]
        ------------
        return: pd.DataFrame
            'stock_id'
                'max', 'min', 'open', 'close', 'spread', 'amount', 'volume', 'volume_last'
        """
        pass