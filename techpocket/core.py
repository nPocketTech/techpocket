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
        self.api_available()
        self.stock = Stock(self._request)
        self.sport = Sport(self._request)
        self.audio = Audio(self._request)

    def api_available(self):
        res = self._request('balance', 0)
        if res['status']['code'] != 200:
            raise Exception(res['status']['msg'])

    def get_balance(self) -> int:
        '''
        [Returns]
        ------------
        return: int balance num
        '''

        res = self._request('balance', 0)
        if res['status']['code'] == 200:
            return res['balance']

        raise Exception(res['status']['msg'])

    def _request(self, endpoint: str, request_time: int, **kwargs) -> dict:
        '''
        [Parameters]
        ------------
        endpoint: str
        request_time: int
        **kwargs: dict

        [Returns]
        ------------
        return: dict
        '''
        response_dict = {'status': {'code': 400, 'msg': 'BadRequest'}, }

        url = f'{self.BASE_URL}/{endpoint}'
        kwargs['token'] = self._api_token
        response = requests.post(url, data=kwargs)

        if response.status_code == 200:
            response_dict = json.loads(response.text)
            if response_dict['status']['code'] == 200:
                return response_dict

        if request_time < self.MAX_RETRY:
            time.sleep(1)
            response_dict = self._request(endpoint, request_time + 1, **kwargs)
        return response_dict
