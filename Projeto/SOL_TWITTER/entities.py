#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from SOL_TWITTER.media import Media


class Entities:
    """
    Essa classe agrega um conjunto de informações que o Twitter chama de ENTITIES
    Esse conjunto agrega em si uma lista de hashtags, urls, imagens/videos e menções a usuários
    """

    def __init__(self):
        self.__hashtags = list()
        self.__media = list()
        self.__urls = list()
        self.__user_mentions = list()

    @property
    def hashtags(self) -> List[str]:
        """Hashtags"""
        return self.__hashtags

    @hashtags.setter
    def hashtags(self, val: List[str]):
        self.__hashtags = val

    @property
    def media(self) -> List[Media]:
        """Vídeo ou imagem"""
        return self.__media

    @media.setter
    def media(self, val: List[Media]):
        self.__media = val

    @property
    def urls(self) -> List[str]:
        """URLs"""
        return self.__urls

    @urls.setter
    def urls(self, val: List[str]):
        self.__urls = val

    @property
    def user_mentions(self) -> List[str]:
        """Usuários mencionados"""
        return self.__user_mentions

    @user_mentions.setter
    def user_mentions(self, val: List[str]):
        self.__user_mentions = val
