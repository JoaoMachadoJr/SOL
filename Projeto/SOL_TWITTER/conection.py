#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.tweepy as tweepy


class Conection:
    """
    Essa classe será usada para o uso da api do Tweepy
    """

    auth = None

    @staticmethod
    def api(auth : tweepy.OAuthHandler) -> tweepy.API:
        """
        Esse método retorna um objeto da API do tweepy devidamente autenticado

        """
        return tweepy.API(auth)



