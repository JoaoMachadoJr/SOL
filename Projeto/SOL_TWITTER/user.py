#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from SOL_MAIN.user import User
from SOL_TWITTER.factory import Factory
from SOL_TWITTER.token import Token
from SOL_TWITTER.tweet import Tweet
from SOL_TWITTER.connection import Connection

class User(User):
    """
    Essa classe representa um usuário do Twitter.
    """

    def __init__(self):
        self.__token = None
        self.__created_at = ""
        self.__description = ""
        self.__favourites_count = ""
        self.__followers_count = ""
        self.__friends_count = ""
        self.__id = ""
        self.__lang = ""
        self.__listed_count = ""
        self.__name = ""
        self.__profile_background_image_url = ""
        self.__profile_banner_url = ""
        self.__profile_image_url = ""
        self.__screen_name = ""
        self.__statuses_count = ""
        self.__url = ""

    @property
    def token(self) -> Token:
        """Token de acesso"""
        return self.__token

    @token.setter
    def token(self, val: Token):
        self.__token = val

    @property
    def created_at(self) -> str:
        """Data de criação do perfil"""
        return self.__created_at

    @created_at.setter
    def created_at(self, val: str):
        self.__created_at = val

    @property
    def description(self) -> str:
        """Descrição disponível no perfil"""
        return self.__description

    @description.setter
    def description(self, val: str):
        self.__description = val

    @property
    def favourites_count(self) -> str:
        """Quantidade de tweets curtidos por esse usuário"""
        return self.__favourites_count

    @favourites_count.setter
    def favourites_count(self, val: str):
        self.__favourites_count = val

    @property
    def followers_count(self) -> str:
        """Quantidade de seguidores"""
        return self.__followers_count

    @followers_count.setter
    def followers_count(self, val: str):
        self.__followers_count = val

    @property
    def friends_count(self) -> str:
        """Quantidade de amigos"""
        return self.__friends_count

    @friends_count.setter
    def friends_count(self, val: str):
        self.__friends_count = val

    @property
    def id(self) -> str:
        """Identificador do usuário"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def lang(self) -> str:
        """Idioma"""
        return self.__lang

    @lang.setter
    def lang(self, val: str):
        self.__lang = val

    @property
    def listed_count(self) -> str:
        """Quantidade de grupos que esse usuário participa"""
        return self.__listed_count

    @listed_count.setter
    def listed_count(self, val: str):
        self.__listed_count = val

    @property
    def location(self) -> str:
        """Localização"""
        return self.__location

    @location.setter
    def location(self, val: str):
        self.__location = val

    @property
    def name(self) -> str:
        """Nome"""
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def profile_background_image_url(self) -> str:
        """URL para a imagem de fundo do perfil"""
        return self.__profile_background_image_url

    @profile_background_image_url.setter
    def profile_background_image_url(self, val: str):
        self.__profile_background_image_url = val

    @property
    def profile_banner_url(self) -> str:
        """URL para a imagem de banner"""
        return self.__profile_banner_url

    @profile_banner_url.setter
    def profile_banner_url(self, val: str):
        self.__profile_banner_url = val

    @property
    def profile_image_url(self) -> str:
        """URL para a foto de perfil"""
        return self.__profile_image_url

    @profile_image_url.setter
    def profile_image_url(self, val: str):
        self.__profile_image_url = val

    @property
    def screen_name(self) -> str:
        """Nome identificador do usuário na rede social"""
        return self.__screen_name

    @screen_name.setter
    def screen_name(self, val: str):
        self.__screen_name = val

    @property
    def statuses_count(self) -> str:
        """Quantidade de tweets publicados"""
        return self.__statuses_count

    @statuses_count.setter
    def statuses_count(self, val: str):
        self.__statuses_count = val

    @property
    def url(self) -> str:
        """URL para o perfil do usuário"""
        return self.__url

    @url.setter
    def url(self, val: str):
        self.__url = val

    def post(self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Tweet = None) -> None:
        """
        Envia um tweet do usuário credenciado ao Twitter.

        Note:
            O Twitter não permite o envio de arquivos genéricos, portanto o parâmetro genericfile não deverá ser
            utilizado.
            Não é permitido preencher o parâmetro post simultaneamente com os  parâmetros text, image ou video
            Não é permitido enviar um video e uma imagem simultaneamente

        Args:
            text:        Uma string contendo o texto que faz parte do conteúdo da publicação.
            image:       Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:       Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
            genericfile: Não deverá ser utilizado
            post:        Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada à
                         rede social.

        Raises:
            ValueError: Será lançado se as regras da cláusula NOTE forem desrespeitadas
        """
        if genericfile != '':
            raise ValueError('Unsupported parameter for post on twitter: genericfile')

        if (post is not None) and ((text != '') or (image != '') or video != ''):
            raise ValueError('Cannot use the parameter post and the parameters [text, image, video]')

        if ((image != '') and (video != '')) or ((post is not None) and (post.image != '') and (post.video != '')):
            raise ValueError('Cannot send an image and a video')

        if (video != '') or ((post is not None) and (post.video != '')):
            raise ValueError('Not supported feature')

        if post is None:
            a_text = text
        else:
            a_text = post.text

        if (post is None) or (post.entities is None) or (post.entities.media is None) or (
                len(post.entities.media) == 0):
            a_image = image
        else:
            a_image = post.entities.media[0]

        if a_image == '':
            Connection.api(self.token).update_status(status=text)
        else:
            Connection.api(self.token).update_with_media(filename=a_image, status=a_text)

    def read(self, post_id: str = '', limit: int = 100) -> List[Tweet]:
        """
        Recupera tweets de um usuário.

        O método prevê a solicitação de um tweet específico a partir de seu ID.
        Se nenhum tweet específico for informado, o retorno do método será uma lista contendo os tweets mais recentes.
        O método também prevê a especificação de um limite de tweets a serem retornados.

        Args:
            post_id: Uma string contendo o ID de um Tweet específico da rede social.
            limit:  Um número inteiro contendo a quantidade máxima de registros que devem ser retornados.

        Raises:
            ValueError: O tweet não é do usuário informado

        """
        result = list()
        if post_id != '':
            tweet = Factory.tweet(Connection.api(self.token).get_status(id=post_id))
            if tweet.user.screen_name != self.screen_name:
                raise ValueError('This tweet does not belong to ' + self.screen_name)
            result.append(tweet)
            return result
        else:
            for info in Connection.api(self.token).user_timeline(screen_name=self.screen_name, count=limit):
                result.append(Factory.tweet(dictionary=info))
            return result

    def subscriptions(self) -> List[User]:
        """
        Recupera as páginas que o usuário corrente curtiu.

        :return: Uma lista de páginas
        """
        result = list()
        Tweepy
        for info in Cursor(Connection.api(self.token).home_timeline(screen_name=self.screen_name)).items():
            result.append(Factory.user(dictionary=info))
        return result
