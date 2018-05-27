#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.tweepy.auth import OAuthHandler
from lib.tweepy.api import API


class Connection:
    """
    Essa classe será usada para o uso da api do Tweepy
    """

    auth = None

    @staticmethod
    def api(auth: OAuthHandler) -> API:
        """
        Esse método retorna um objeto da API do tweepy devidamente autenticado

        """
        return API(auth)
