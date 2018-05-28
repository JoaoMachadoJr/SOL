#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_MAIN import Post
from SOL_TWITTER.entities import Entities
from SOL_TWITTER.place import Place
from SOL_TWITTER.user import User


class Tweet(Post):
    """
    Essa classe define o conteúdo de um Tweet do Twitter.
    """

    def __init__(self):
        super().__init__()
        self.__coordinates = ""
        self.__created_at = ""
        self.__entities = None
        self.__favorite_count = ""
        self.__favorited = ""
        self.__id = ""
        self.__in_reply_to_screen_name = ""
        self.__lang = ""
        self.__place = None
        self.__quoted_status = None
        self.__retweet_count = ""
        self.__retweeted = ""
        self.__retweeted_status = None
        self.__text = ""
        self.__user = None

    @property
    def coordinates(self) -> str:
        """Coordenadas"""
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, val: str):
        self.__coordinates = val

    @property
    def created_at(self) -> str:
        """Horário de criação"""
        return self.__created_at

    @created_at.setter
    def created_at(self, val: str):
        self.__created_at = val

    @property
    def entities(self) -> Entities:
        """Entidades relacionadas"""
        return self.__entities

    @entities.setter
    def entities(self, val: Entities):
        self.__entities = val

    @property
    def favorite_count(self) -> str:
        """Quantidade de 'curtidas' recebidas"""
        return self.__favorite_count

    @favorite_count.setter
    def favorite_count(self, val: str):
        self.__favorite_count = val

    @property
    def favorited(self) -> str:
        """Informa se o usuário autenticado curtiu esse tweet"""
        return self.__favorited

    @favorited.setter
    def favorited(self, val: str):
        self.__favorited = val

    @property
    def id(self) -> str:
        """Identificador da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def in_reply_to_screen_name(self) -> str:
        """Prenchido apenas para tweets que sejam respostas de outros tweets. Informa o usuário do tweet original"""
        return self.__in_reply_to_screen_name

    @in_reply_to_screen_name.setter
    def in_reply_to_screen_name(self, val: str):
        self.__in_reply_to_screen_name = val

    @property
    def lang(self) -> str:
        """Idioma"""
        return self.__lang

    @lang.setter
    def lang(self, val: str):
        self.__lang = val

    @property
    def place(self) -> Place:
        """Localização"""
        return self.__place

    @place.setter
    def place(self, val: Place):
        self.__place = val

    @property
    def quoted_status(self) -> 'Tweet':
        """Apenas preenchido em tweets que estejam citando outros tweets. Guarda o conteúdo do tweet original"""
        return self.__quoted_status

    @quoted_status.setter
    def quoted_status(self, val: 'Tweet'):
        self.__quoted_status = val

    @property
    def retweet_count(self) -> str:
        """Quantidade de vezes que esse tweet foi compartilhado"""
        return self.__retweet_count

    @retweet_count.setter
    def retweet_count(self, val: str):
        self.__retweet_count = val

    @property
    def retweeted(self) -> str:
        """Indica se esse tweet foi compartilhado pelo usuário corrente"""
        return self.__retweeted

    @retweeted.setter
    def retweeted(self, val: str):
        self.__retweeted = val

    @property
    def retweeted_status(self) -> 'Tweet':
        """Preenchido apenas para tweets que sejam compartilhamentos de outros. Guarda o tweet original"""
        return self.__retweeted_status

    @retweeted_status.setter
    def retweeted_status(self, val: 'Tweet'):
        self.__retweeted_status = val

    @property
    def text(self) -> str:
        """Texto do tweet"""
        return self.__text

    @text.setter
    def text(self, val: str):
        self.__text = val

    @property
    def user(self) -> User:
        """Autor do tweet"""
        return self.__user

    @user.setter
    def user(self, val: User):
        self.__user = val
