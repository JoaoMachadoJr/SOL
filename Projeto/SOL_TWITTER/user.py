#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from SOL_MAIN.user import User
from SOL_TWITTER.factory import Factory
from SOL_TWITTER.tweet import Tweet
from SOL_TWITTER.conection import Conection


class User(User):
    """
    Essa classe representa um usuário do Twitter.
    """

    def __init__(self):
        self.auth = None
        self.created_at = ""
        self.description = ""
        self.favourites_count = ""
        self.followers_count = ""
        self.friends_count = ""
        self.id = id
        self.id_str = ""
        self.lang = ""
        self.listed_count = ""
        self.location = ""
        self.name = ""
        self.profile_background_image_url = ""
        self.profile_banner_url = ""
        self.profile_image_url = ""
        self.screen_name = ""
        self.show_all_inline_media = ""
        self.status = None
        self.statuses_count = ""
        self.time_zone = ""
        self.url = ""
        self.verified = ""

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
            Conection.api(self.auth).update_status(status=text)
        else:
            Conection.api(self.auth).update_with_media(filename=a_image, status=a_text)

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
            tweet = Factory.tweet(Conection.api(self.auth).get_status(id=post_id))
            if tweet.user.screen_name != self.screen_name:
                raise ValueError('This tweet does not belong to ' + self.screen_name)
            result.append(tweet)
            return result
        else:
            for info in Conection.api(self.auth).user_timeline(screen_name=self.screen_name, count=limit):
                result.append(Factory.tweet(dictionary=info))
            return result
