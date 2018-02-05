#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entities:
    """
    Essa classe agrega um conjunto de informações que o Twitter chama de ENTITIES
    Esse conjunto agrega em si uma lista de hashtags, urls, imagens/videos e menções a usuários
    """

    def __init__(self):
        self.hashtags = list()
        self.media = list()
        self.urls = list()
        self.user_mentions = list()


