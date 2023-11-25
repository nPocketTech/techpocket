# -*- coding: utf-8 -*-

import json
import time

import requests

from .service.stock import Stock
from .service.sport import Sport
from .service.audio import Audio


class TechPocket:
    BASE_URL = 'https://api.npocket.tech/'
    MAX_RETRY = 3

    def __init__(self, api_token):
        self._api_token = api_token
        self.get_balance()
        self.stock = Stock(self._request)
        self.sport = Sport(self._request)
        self.audio = Audio(self._request)

    def get_balance(self) -> int:
        '''
        [Returns]
        ------------
        balance: int
        '''
        balance = self._request('balance')['balance']
        return balance

    def _request(self, endpoint: str, request_time: int = 0, **kwargs) -> dict:
        '''
        [Parameters]
        ------------
        endpoint: str
        request_time: int
        **kwargs: dict

        [Returns]
        ------------
        response_dict: dict
        '''

        url = f'{self.BASE_URL}/{endpoint}'
        kwargs['token'] = self._api_token
        response = requests.post(url, data=kwargs)

        if response.status_code != 200:
            if request_time < self.MAX_RETRY:
                time.sleep(1)
                response_dict = self._request(endpoint, request_time + 1, **kwargs)
            else:
                response_dict = {'status': {'code': 400, 'msg': 'Bad Request'}}
        else:
            response_dict = json.loads(response.text)
            if response_dict['status']['code'] != 200 and request_time < self.MAX_RETRY:
                time.sleep(1)
                response_dict = self._request(endpoint, request_time + 1, **kwargs)

        if request_time == 0:
            assert response_dict['status']['code'] == 200, response_dict['status']['msg']
            del response_dict['status']

        return response_dict
