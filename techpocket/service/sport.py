class Sport:
    def __init__(self, _request):
        self._request = _request

    def get_sport_scores(self, sport: str, date: str) -> dict:
        '''
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
        '''
        res = self._request('sport/scores', 0, sport=sport, date=date)

        if res['status']['code'] == 200:
            res.pop('status', None)
            return res

        raise Exception(res['status']['msg'])

    def get_sport_odds(self, sport: str, date: str) -> dict:
        '''
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
        '''
        res = self._request('sport/odds', 0, sport=sport, date=date)

        if res['status']['code'] == 200:
            res.pop('status', None)
            return res

        raise Exception(res['status']['msg'])

    def get_sport_lineups(self, sport) -> dict:
        '''
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
        '''
        res = self._request('sport/lineups', 0, sport=sport)

        if res['status']['code'] == 200:
            res.pop('status', None)
            return res

        raise Exception(res['status']['msg'])
