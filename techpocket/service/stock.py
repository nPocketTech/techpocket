import pathlib
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Stock:
    def __init__(self, _request):
        self._request = _request

    def get_list(self, key: str, df_like: bool = False, save_to: str = '') -> dict:
        '''
        [Parameters]
        ------------
        key: str
            '上市股票', '上市權證', '上市ETF', '上市TDR', '上市受益證券', '上櫃股票', '上櫃權證', '上櫃ETF', '上櫃受益證券', '興櫃股票', '上市櫃ETN'

        [Returns]
        ------------
        data_list: 詳情請上 https://npocket.tech/doc/stock/api#%E8%82%A1%E7%A5%A8%E6%B8%85%E5%96%AE
        '''

        self._handle_path(save_to)
        data_list = self._request('stock/list', key=key)['data_list']

        if df_like:
            data_list = pd.DataFrame(data_list)
            if save_to:
                data_list.to_csv(save_to)

        return data_list

    def get_ticks_realtime(self, stock_id: str, df_like=False, save_to='', plot=False) -> dict or tuple[
        dict, pd.DataFrame]:
        '''
        [Parameters]
        ------------
        stock_id: str
            'TSE', 'OTC', stock_id

        [Returns]
        ------------
        data: 詳情請上 https://npocket.tech/doc/stock/api#%E5%8D%B3%E6%99%82%E8%B5%B0%E5%8B%A2
        '''
        path_obj = self._handle_path(save_to)
        data = self._request('stock/ticks_realtime', stock_id=stock_id)['data']

        if df_like:
            ticks = data.pop('ticks')
            ticks = pd.DataFrame(ticks)

            if plot:
                self._plot_ticks_realtime(ticks, path_obj.parent / f'{stock_id}.png')

            if save_to:
                ticks.to_csv(save_to)

            return data, ticks

        return data

    def get_price_realtime(self, stock_list: list, df_like=False, save_to='') -> dict or pd.DataFrame or None:
        '''
        [Parameters]
        ------------
        stock_id: list
            stock_ids, len(stock_id) <= 25

        [Returns]
        ------------
        data_list: 詳情請上 https://npocket.tech/doc/stock/api#%E5%8D%B3%E6%99%82%E8%82%A1%E5%83%B9
        '''
        self._handle_path(save_to)
        data_list = self._request('stock/price_realtime', stock_list=stock_list)['data_list']

        if df_like:
            if not data_list:
                return None

            data_list = pd.DataFrame(data_list)
            data_list[stock_list] = stock_list

            if save_to:
                data_list.to_csv(save_to)

        return data_list

    @staticmethod
    def _plot_ticks_realtime(df: pd.DataFrame, save_to):
        df = df.copy()

        fig, ax1 = plt.subplots(figsize=(10, 5))
        sns.set(style="whitegrid")
        df['timestamp'] = pd.to_datetime(df['time'], format='%H:%M')

        sns.lineplot(x='timestamp', y='amount', data=df, label='Amount', color='blue', ax=ax1)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Amount', color='blue')

        ax2 = ax1.twinx()
        sns.lineplot(x='timestamp', y='price', data=df, label='Price', color='red', ax=ax2)
        ax2.set_ylabel('Price', color='red')

        xformatter = mdates.DateFormatter('%H:%M')
        xlocator = mdates.MinuteLocator(byminute=[0, 30], interval=1)
        ax1.xaxis.set_major_locator(xlocator)
        ax1.xaxis.set_major_formatter(xformatter)

        ax1.legend(loc='best')
        ax2.legend(loc='best')
        plt.title('Ticks Realtime')
        plt.tight_layout()

        plt.savefig(save_to, dpi=600)
        plt.show()

    @staticmethod
    def _handle_path(save_to: str) -> pathlib.Path:
        path_obj = Path(save_to)

        # 如果不存在則創建父資料夾路徑
        if path_obj != '':
            if path_obj.suffix:
                path_obj.parent.mkdir(parents=True, exist_ok=True)
                open(path_obj, 'w').close()
            else:
                path_obj.mkdir(parents=True, exist_ok=True)

        return path_obj
