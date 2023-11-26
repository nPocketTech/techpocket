# -*- coding: utf-8 -*-
import pathlib
from pathlib import Path
from datetime import date as date_library

import pandas as pd
from dateutil import parser


class Sport:
    def __init__(self, _request):
        self._request = _request
        self._today = date_library.today().strftime("%Y-%m-%d")

    def get_sport_scores(self, sport: str, date: str = "", df_like=False, save_to: str = "") -> dict or pd.DataFrame:
        '''
        [Parameters]
        ------------
        sport: str
            'NBA', 'MLB', 'CPB', 'NPB', 'KBO', 'FTB', 'ICE', 'TNS'
        date: str
            YYYY-MM-DD

        [Returns]
        ------------
        games: 詳情請上 https://npocket.tech/doc/sport/api#%E5%8D%B3%E6%99%82%E6%AF%94%E5%88%86
        '''
        self._handle_path(save_to)
        date = self._parse_user_input(date) if date else self._today

        games = self._request('sport/scores', sport=sport, date=date)['games']

        if df_like:
            games = pd.json_normalize(games)

            games = games.rename(columns={col: col.replace('.', '_') for col in games.columns})
            if save_to:
                games.to_csv(save_to)

        return games

    def get_sport_odds(self, sport: str, date: str, df_like=False, save_to: str = "") -> dict or pd.DataFrame:
        '''
        [Parameters]
        ------------
        sport: str
            'NBA', 'MLB', 'CPB', 'NPB', 'KBO', 'FTB', 'ICE', 'TNS'
        date: str
            YYYY-MM-DD

        [Returns]
        ------------
        games: 詳情請上 https://npocket.tech/doc/sport/api#%E8%B3%A0%E7%8E%87%E8%A8%98%E9%8C%84
        '''

        date = self._parse_user_input(date) if date else self._today

        games = self._request('sport/odds', sport=sport, date=date)['games']

        if df_like:
            games = self._normalized_save_sport_odds(games, save_to)

        return games

    def get_sport_lineups(self, sport: str, df_like=False, save_to: str = "") -> dict or pd.DataFrame:
        '''
        [Parameters]
        ------------
        sport: str
        [Returns]
        ------------
        games: 詳情請上 https://npocket.tech/doc/sport/api#%E8%B3%BD%E4%BA%8B%E5%90%8D%E5%96%AE
        '''
        games = self._request('sport/lineups', sport=sport)['games']

        if df_like:
            games = self._normalized_save_sport_lineups(games, save_to)

        return games

    def _normalized_save_sport_odds(self, games: dict, save_to: str = '') -> pd.DataFrame:
        path_obj = self._handle_path(save_to)

        res = []
        for game in games:
            odds = pd.DataFrame(game['odds'])
            odds['home'] = game['home']
            odds['away'] = game['away']
            odds['date'] = game['date']
            odds['lottery_id'] = lottery_id = game['lottery_id']
            csv_name = lottery_id + '.csv'

            if save_to and path_obj.is_dir():
                odds.to_csv(path_obj / csv_name)
            res.append(odds)

        games = pd.concat(res, axis=0, ignore_index=True)
        if save_to and path_obj.is_file():
            games.to_csv(save_to)

        return games

    def _normalized_save_sport_lineups(self, games: dict, save_to: str = '') -> pd.DataFrame:
        path_obj = self._handle_path(save_to)

        # 若路徑為資料夾，則分檔案創建
        # 若路徑為資料夾，則一次儲存
        res = []
        for game in games:
            away_name = game['away']['name']
            home_name = game['home']['name']
            csv_name = f"{away_name}-{home_name}-{game['date']}-{game['time']}.csv".replace(':', '')

            away = self._normalize_starting_injuries(game, 'away')
            home = self._normalize_starting_injuries(game, 'home')

            df = pd.concat([home, away])
            df['date'] = game['date']
            df['time'] = game['time']

            if save_to and path_obj.is_dir():
                df.to_csv(path_obj / csv_name)
            res.append(df)

        games = pd.concat(res, axis=0, ignore_index=True)
        if save_to and path_obj.is_file():
            games.to_csv(save_to)

        return games

    @staticmethod
    def _parse_user_input(user_input):
        parsed_date = parser.parse(user_input).strftime("%Y-%m-%d")
        return parsed_date

    @staticmethod
    def _normalize_starting_injuries(game, home_away: str):
        first_data = game[home_away]
        name = first_data['name']

        starting, starting_len = first_data['starting'], len(first_data['starting'])
        starting = pd.DataFrame(starting)
        starting['status_detail'] = None
        starting['status'] = ['starting'] * starting_len

        injuries, injuries_len = first_data['injuries'], len(first_data['injuries'])
        injuries = pd.DataFrame(injuries)
        injuries = injuries.rename(columns={'status': 'status_detail'})
        injuries['status'] = ['injuries'] * injuries_len

        normalized = pd.concat([starting, injuries], axis=0, ignore_index=True)
        normalized['team'] = [name] * len(normalized)

        return normalized

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
