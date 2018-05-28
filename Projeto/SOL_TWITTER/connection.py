#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SOL_TWITTER.token import Token
from lib.tweepy.auth import OAuthHandler
from lib.tweepy.api import API


class Connection:
    """
    Essa classe será usada para o uso da api do Tweepy
    """

    auth = None

    @staticmethod
    def api(token: Token) -> API:
        """
        Esse método retorna um objeto da API do tweepy devidamente autenticado
        """
        auth = OAuthHandler(token.consumer_key, token.consumer_secret)
        auth.set_access_token(token.access_token, token.access_token_secret)
        auth.get_authorization_url()
        return API(auth)
