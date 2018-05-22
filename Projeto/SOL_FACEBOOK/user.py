#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

from SOL_MAIN import User
from SOL_FACEBOOK.post import Post
from SOL_FACEBOOK.connection import Connection
from SOL_FACEBOOK.factory import Factory
from typing import List

class User(User):
    """
    Essa classe representa um usuário do Facebook.
    """

    def __init__(self):
        self.id = ""
        self.about = ""
        self.bio = ""
        self.birthday = ""
        self.cover = ""
        self.education = list()
        self.email = ""
        self.favorite_athletes = list()
        self.favorite_teams = list()
        self.first_name = ""
        self.gender = ""
        self.hometown = None
        self.inspirational_people = list()
        self.interested_in = list()
        self.languages = list()
        self.last_name = ""
        self.link = ""
        self.locale = ""
        self.location = None
        self.middle_name = ""
        self.name = ""
        self.name_format = ""
        self.political = ""
        self.public_key = ""
        self.quotes = ""
        self.relationship_status = ""
        self.religion = ""
        self.significant_other = None
        self.sports = list()
        self.timezone = ""
        self.token=''
        self.viewer_can_send_gift = ""
        self.website = ""
        self.work = list()


    def post (self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Post = None )-> None:
        """
        Envia um post do usuário credenciado ao facebook.

        Note:
            O facebook não permite o envio de arquivos genericos, portanto o argumento genericfile não deverá ser
            utilizado.
            Não é permitido preencher o parâmetro post simultaneamento com os  parâmetros text, image ou video
            Não é permitido enviar um video e uma imagem simultaneamente

        Args:
            text:        Uma string contendo o texto que faz parte do conteúdo da publicação.
            image:       Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:       Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
            genericfile: Não deverá ser utilizado
            post:        Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada à
                         rede social.

        Raises:
            ValueError: Será lançado se as regras do cláusula NOTE forem desrespeitadas
        """
        if genericfile != '':
            raise ValueError('Unsuported parameter for post on facebook: genericfile')

        if (post is not None) and ((text!='') or (image!='') or video!=''):
            raise ValueError('Cannot use the parameter post and the parameters [text, image, video]')

        if ((image != '') and (video != '')) or ((post is not None) and (post.image != '') and (post.video != '')):
            raise ValueError('Cannot send an image and a video')

        if post is not None:
            a_text=post.text
            a_filepath=post.image+post.video
        else:
            a_text=text
            a_filepath=image+video


        if a_filepath != '':
            if (video!='') or ((post is not None) and (post.video != '')):
                a_graphurl = "https://graph-video.facebook.com/" + self.id + "/videos?access_token=" + self.token
            else:
                a_graphurl = "https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+self.token
            a_params = {"description": a_text}
            if Path(a_filepath).exists():
                a_files = {'file': open(a_filepath, 'rb')}
                Connection.post(a_graphurl, files=a_files, params=a_params)
            else:
                a_params["file_url"] = a_filepath
                Connection.post(a_graphurl, params=a_params).json()
        else:
            a_graphurl = "https://graph.facebook.com/v2.6/me/feed?&access_token="+str(self.token)
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
            limit:  Um número inteiro contendo a quantidades máxima de registro que devem ser retornados.

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        from dateutil.parser import parse

        token = self.token
        a_graphurl="https://graph.facebook.com/v2.5/" + self.id + "/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=1000&access_token=" + token;
        r=Connection.get(a_graphurl)
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
