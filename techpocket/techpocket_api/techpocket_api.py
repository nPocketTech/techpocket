import requests
import urllib3
from loguru import logger


class TechPocketApi:
    def __init__(self):
        self.__user_id = ""
        self.__password = ""
        self.__api_token = ""
        self.__api_url = "https://api.npocket.tech/"

    def login(self, user_id: str, password: str) -> bool:
        """
        [Parameters]
        ------------
        user_id: str
        password: str

        [Returns]
        ------------
        return: bool
            True, False
        """
        pass

    def login_by_token(self, api_token: str) -> bool:
        """
        [Parameters]
        ------------
        api_token: str

        [Returns]
        ------------
        return: bool
            True, False
        """
        pass

    def get_balance(self) -> int:
        """
        [Parameters]
        ------------

        [Returns]
        ------------
        return: int
        """
        pass
