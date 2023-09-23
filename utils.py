import json
import logging
import time

import requests


class TechPocketApi:
    BASE_URL = 'https://api.npocket.tech/'
    MAX_TRY = 5

    def _request(self, endpoint: str, token: str, **kwargs) -> dict:
        '''
        [Parameters]
        ------------
        url: str
        token: str
        kwargs: str

        [Returns]
        ------------
        return: dict
        '''

        kwargs['token'] = token
        url = f'{TechPocketApi.BASE_URL}/{endpoint}'
        try_count = 0
        response = ''

        try:
            while try_count < TechPocketApi.MAX_TRY:
                response = requests.post(url, data=kwargs)
                if response.status_code == 200:
                    break

            response.raise_for_status()
            data = self._handle_data(json.loads(response.text))
            return data

        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.HTTPError):
                status_code = e.response.status_code
                match status_code:
                    case 400:
                        logging.critical('BadRequest')
                    case 401:
                        logging.critical('Unauthorized')
                    case 404:
                        logging.critical('NotFound')
                    case 405:
                        logging.critical('MethodNotAllowed')
                    case 413:
                        logging.critical('PayloadTooLarge')
                    case 415:
                        logging.critical('UnsupportedMediaType')
                    case 429:
                        logging.critical('TooManyRequests')
                    case 500:
                        logging.critical('InternalServerError')
                    case 503:
                        logging.critical('ServiceUnavailable')
            return {}

    @staticmethod
    def _handle_data(data: dict) -> dict:
        '''
        [Parameters]
        ------------
        data: dict

        [Returns]
        ------------
        return: dict
        '''

        if data['status']['code'] == 200:
            data.pop('status', None)
            return data
        else:
            logging.critical(data['status']['msg'])
        return {}
