from functools import reduce
import pandas as pd
from utils import TechPocketApi


class Sport(TechPocketApi):
    def __init__(self, token):
        self._token = token

    def get_sport_scores(self, sport: str, date: str) -> pd.DataFrame:
        """
        [Parameters]
        ------------
        sport: str
            'NBA', 'MLB', 'CPB', 'NPB', 'KBO', 'FTB', 'ICE', 'TNS'
        date: str
            YYYY-MM-DD

        [Returns]
        ------------
        return: list[dict]
            date: str,
                YYYY-MM-DD
            time: str,
                hh:mm
            status: str,
                 'Playing', 'Final'
            away: dict,
                name: str,
                score: int,
                box: list,
                hit: int (basketball),
                error: int (basketball)
            home: dict,
                name: str,
                score: int,
                box: list,
                hit: int (baseball),
                error: int (baseball)
        """
        res = self._request('sport/scores', self._token, sport=sport, date=date)

        df = pd.DataFrame({
            'date': [], 'time': [], 'status': [], 'away_name': [], 'away_score': [],
            'away_box': [], 'home_name': [], 'home_score': [], 'home_box': []
        })

        if 'games' in res and res['games']:

            for game in res['games']:
                game['away']['box'] = ', '.join(game['away']['box'])
                game['home']['box'] = ', '.join(game['home']['box'])

            df = pd.DataFrame(res['games'])
            df = df[['date', 'time', 'status']]

            away_df = self.flatten_dict(res['games'], 'away', prefix='away_')
            home_df = self.flatten_dict(res['games'], 'home', prefix='home_')

            df = pd.merge(df, away_df, left_index=True, right_index=True)
            df = pd.merge(df, home_df, left_index=True, right_index=True).reset_index(drop=True)

        return df

    def get_sport_odds(self, sport: str, date: str) -> pd.DataFrame:
        """
        [Parameters]
        ------------
        sport: str
            'NBA', 'MLB', 'CPB', 'NPB', 'KBO', 'FTB', 'ICE', 'TNS'
        date: str
            YYYY-MM-DD

        [Returns]
        ------------
        return: list[dict]
            date: str,
                YYYY-MM-DD
            time: str,
                hh:mm
            lottery_id: str,
            away: str,
            home: str,
            odds: dict,
                away_is_plus: int,
                away_handi: int,
                away_normal: int,
                home_handi: int,
                home_normal: int,
                total: int,
                big: int,
                small: int,
                update_time: str
                handi: int (basketball, tennis)
                big_15：int (soccer, tennis, hockey),
                big_25：int (soccer, tennis, hockey),
                big_35：int (soccer, tennis, hockey),
                small_15：int (soccer, tennis, hockey),
                small_25：int (soccer, tennis, hockey),
                small_35：int (soccer, tennis, hockey),
                num_024：int (soccer, tennis, hockey),
                num_135：int (soccer, tennis, hockey),
                tie_handi：int (soccer, tennis, hockey),
                tie_normal: int (soccer, tennis, hockey)
        """
        res = self._request('sport/odds', self._token, sport=sport, date=date)

        df = pd.DataFrame(
            {'date': [], 'time': [], 'lottery_id': [], 'away': [], 'home': []}
        )

        if 'games' in res and res['games']:
            odds_df = self.flatten_dict(res['games'], 'odds')
            df = pd.DataFrame(res['games'])
            df = df[['date', 'time', 'lottery_id', 'away', 'home']]
            df = pd.merge(df, odds_df, left_index=True, right_index=True).reset_index(drop=True)

        return df

    def get_sport_lineups(self, sport) -> pd.DataFrame:
        """
        [Parameters]
        ------------
        sport: str
            'NBA'

        [Returns]
        ------------
        return: list[dict]
            date: str,
                YYYY-MM-DD
            time: str,
                hh:mm
            away: dict,
                name: str,
                starting: dict,
                    name：str,
                    pos: str
                injuries: dict:
                    name: str,
                    pos: str,
                    status: str
            home: dict,
                name: str,
                starting: dict,
                    name：str,
                    pos: str
                injuries: dict:
                    name: str,
                    pos: str,
                    status: str
        """
        res = self._request('sport/lineups', self._token, sport=sport)

        df = pd.DataFrame(
            {'date': [], 'time': [], 'away': [], 'home': []}
        )

        if 'games' in res and res['games']:
            away_df = self.flatten_dict(res['games'], 'away', prefix='away_')
            home_df = self.flatten_dict(res['games'], 'away', prefix='home_')

            df = pd.DataFrame(res['games'])
            df = df[['date', 'time']]

            df = pd.merge(df, away_df, left_index=True, right_index=True)
            df = pd.merge(df, home_df, left_index=True, right_index=True).reset_index(drop=True)


        return df

    @staticmethod
    def flatten_dict(d: dict, col_name: str, prefix: str = None) -> pd.DataFrame:
        dfs = []

        for i, game in enumerate(d):
            if isinstance(game[col_name], dict):
                df = pd.DataFrame(game[col_name], index=[i])
            else:
                df = pd.DataFrame(game[col_name])
                df.index = [i] * len(df)
            dfs.append(df)

        res_df = pd.concat(dfs)
        if prefix:
            res_df = res_df.add_prefix(prefix)

        return res_df
