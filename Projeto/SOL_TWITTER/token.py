#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Token:
    """
    Essa classe armazena o conjunto de tokens necessários para operações com a rede social Twitter
    """

    def __init__(self):
        self.__consumer_key = ""
        self.__consumer_secret = ""
        self.__access_token = ""
        self.__access_token_secret = ""

    @property
    def consumer_key(self) -> str:
        return self.__consumer_key

    @consumer_key.setter
    def consumer_key(self, val: str):
        self.__consumer_key = val

    @property
    def consumer_secret(self) -> str:
        return self.__consumer_secret

    @consumer_secret.setter
    def consumer_secret(self, val: str):
        self.__consumer_secret = val

    @property
    def access_token(self) -> str:
        return self.__access_token

    @access_token.setter
    def access_token(self, val: str):
        self.__access_token = val

    @property
    def access_token_secret(self) -> str:
        return self.__access_token_secret

    @access_token_secret.setter
    def access_token_secret(self, val: str):
        self.__access_token_secret = val
