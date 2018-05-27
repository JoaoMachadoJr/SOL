#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pathlib import Path
from typing import List
from SOL_FACEBOOK.connection import Connection
from SOL_FACEBOOK.experience import Experience
from SOL_FACEBOOK.page import Page
from SOL_FACEBOOK.post import Post
import SOL_MAIN


class User(SOL_MAIN.User):
    """
    Essa classe representa um usuário do Facebook.
    """

    def __init__(self):
        self.__id = ""
        self.__about = ""
        self.__bio = ""
        self.__bio = ""
        self.__cover = ""
        self.__email = ""
        self.__first_name = ""
        self.__gender = ""
        self.__hometown = None
        self.__languages = list()
        self.__last_name = ""
        self.__middle_name = ""
        self.__name = ""
        self.__quotes = ""
        self.__significant_other = None
        self.__token = ''
        self.__website = ""

    @property
    def id(self) -> str:
        """Identificador da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def about(self) -> str:
        """Sessão 'Sobre' do perfil do usuário"""
        return self.__about

    @about.setter
    def about(self, val: str):
        self.__about = val

    @property
    def bio(self) -> str:
        """Autobiografia"""
        return self.__bio

    @bio.setter
    def bio(self, val: str):
        self.__bio = val

    @property
    def cover(self) -> str:
        """Foto de capa"""
        return self.__cover

    @cover.setter
    def cover(self, val: str):
        self.__cover = val

    @property
    def email(self) -> str:
        """Endereço de e-mail"""
        return self.__email

    @email.setter
    def email(self, val: str):
        self.__email = val

    @property
    def first_name(self) -> str:
        """Primeiro nome"""
        return self.__first_name

    @first_name.setter
    def first_name(self, val: str):
        self.__first_name = val

    @property
    def gender(self) -> str:
        """Gênero"""
        return self.__gender

    @gender.setter
    def gender(self, val: str):
        self.__gender = val

    @property
    def hometown(self) -> Page:
        """Cidade natal"""
        return self.__hometown

    @hometown.setter
    def hometown(self, val: Page):
        self.__hometown = val

    @property
    def languages(self) -> List[Experience]:
        """Idiomas"""
        return self.__languages

    @languages.setter
    def languages(self, val: List[Experience]):
        self.__languages = val

    @property
    def last_name(self) -> str:
        """Sobrenome"""
        return self.__last_name

    @last_name.setter
    def last_name(self, val: str):
        self.__last_name = val

    @property
    def middle_name(self) -> str:
        """Nome do meio"""
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, val: str):
        self.__middle_name = val

    @property
    def name(self) -> str:
        """Nome como exibido no perfil"""
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def quotes(self) -> str:
        """Citações favoritas"""
        return self.__quotes

    @quotes.setter
    def quotes(self, val: str):
        self.__quotes = val

    @property
    def significant_other(self) -> 'User':
        """Interesse romântico"""
        return self.__significant_other

    @significant_other.setter
    def significant_other(self, val: 'User'):
        self.__significant_other = val

    @property
    def token(self) -> str:
        """Token de acesso de um usuário"""
        return self.__token

    @token.setter
    def token(self, val: str):
        self.__token = val

    @property
    def website(self) -> str:
        """Site externo relacionado ao usuário"""
        return self.__website

    @website.setter
    def website(self, val: str):
        self.__website = val

    def post(self, text: str = '', picture: str = '', video: str = '',
             genericfile: str = '', post: Post = None) -> None:
        """
        Envia um post do usuário credenciado ao facebook.

        Note:
            O facebook não permite o envio de arquivos genéricos, portanto o argumento genericfile não deverá ser
            utilizado.
            Não é permitido preencher o parâmetro post simultaneamente com os  parâmetros text, picture ou video
            Não é permitido enviar um video e uma imagem simultaneamente

        Args:
            text:        Uma string contendo o texto que faz parte do conteúdo da publicação.
            picture:     Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:       Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
            genericfile: Não deverá ser utilizado
            post:        Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada à
                         rede social.

        Raises:
            ValueError: Será lançado se as regras do cláusula NOTE forem desrespeitadas
        """
        if genericfile != '':
            raise ValueError('Unsupported parameter for post on facebook: genericfile')

        if (post is not None) and ((text != '') or (picture != '') or video != ''):
            raise ValueError('Cannot use the parameter post and the parameters [text, picture, video]')

        if ((picture != '') and (video != '')) or ((post is not None) and (post.picture != '') and (post.video != '')):
            raise ValueError('Cannot send an picture and a video')

        if post is not None:
            a_text = post.text
            if post.video is not None:
                a_filepath = post.video.source
            else:
                a_filepath = post.picture
        else:
            a_text = text
            a_filepath = picture + video

        if a_filepath != '':
            if (video != '') or ((post is not None) and (post.video != '')):
                a_graphurl = "https://graph-video.facebook.com/" + self.id + "/videos?access_token=" + self.token
            else:
                a_graphurl = "https://graph.facebook.com/v2.6/" + self.id + "/photos?access_token=" + self.token
            a_params = {"description": a_text}
            if Path(a_filepath).exists():
                a_files = {'file': open(a_filepath, 'rb')}
                Connection.post(a_graphurl, files=a_files, params=a_params)
            else:
                a_params["file_url"] = a_filepath
                Connection.post(a_graphurl, params=a_params)
        else:
            a_graphurl = "https://graph.facebook.com/v2.6/me/feed?&access_token=" + str(self.token)
            a_params = {"message": a_text}
            Connection.post(a_graphurl, params=a_params)

    def read(self, postID: str = '', limit: int = 100) -> List[Post]:
        """
        Recupera conteúdo da rede social.
        Atualmente não é possível ler a timeline de um usuário, portanto esse método lê o conteúdo presente no mural
        de um usuário

        O método prevê a solicitação de um Post específico a partir de seu ID.
        O método também prevê a especificação de um limite de Posts a serem retornados.

        Args:
            postID: Uma string contendo o ID de um Post da rede social, caso queira recuperar um post específico.
            limit:  Um número inteiro contendo a quantidade máxima de registro que devem ser retornados.

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        from dateutil.parser import parse

        token = self.token
        a_graphurl = "https://graph.facebook.com/v2.5/" + self.id + "/feed?fields=" + User.fields() + "&limit=1000&access_token=" + token;
        r = Connection.get(a_graphurl)
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                post = _Post_Facebook.Post_Facebook(dictionary=a)
                if ((len(lista) == limit) or (
                        dateMin != "" and parse(post.created_time).replace(tzinfo=None) < dateMin)):
                    return lista
                lista.append(post)
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    @staticmethod
    def fields() -> str:
        """Campos a serem recuperados em uma consulta"""
        return "id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message," \
               "message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type," \
               "story,targeting,to,type,updated_time,with_tags"
