import logging

from utils import TechPocketApi
from service.stock import Stock
from service.sport import Sport
from service.audio import Audio

class TechPocket(TechPocketApi):
    FREE_TOKEN = 'DAC8D4453347487F24CDFCE061DF089FA1ED786B'

    def __init__(self):
        self._user_id = ''
        self._password = ''
        self._api_token = TechPocket.FREE_TOKEN
        self.stock = Stock(TechPocket.FREE_TOKEN)
        self.sport = Sport(TechPocket.FREE_TOKEN)
        self.audio = Audio(TechPocket.FREE_TOKEN)

    def login(self, user_id: str = None, password: str = None, api_token: str = None) -> None:
        '''
        [Parameters]
        ------------
        user_id: str
        password: str
        api_token: str

        [Returns]
        ------------
        return: None
        '''

        if api_token:
            self._api_token = api_token
            if self.get_balance():
                self.stock = Stock(self._api_token)
                self.sport = Sport(self._api_token)
                logging.info('login successful')
                return None
            else:
                self._api_token = TechPocket.FREE_TOKEN

        elif user_id and password:
            self._user_id = user_id
            self._password = password
            res = self._get_token()

            if res:
                self._api_token = res
                self.stock = Stock(self._api_token)
                self.sport = Sport(self._api_token)
                logging.info('login successful')
                return None

        logging.info('login failed')
        return None

    def get_balance(self) -> int:
        """
        [Parameters]
        ------------

        [Returns]
        ------------
        return: int
        """

        res = self._request('balance', self._api_token)
        if 'balance' in res:
            return res['balance']
        else:
            return 0

    def _get_token(self) -> str or None:
        """
        [Parameters]
        ------------

        [Returns]
        ------------
        return: int
        """
        pass
