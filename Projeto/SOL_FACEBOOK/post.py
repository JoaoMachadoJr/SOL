#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from SOL_FACEBOOK.video import Video
import SOL_MAIN


class Post(SOL_MAIN.Post):
    """
    Essa classe define o conteúdo de um Post do Facebook.
    """

    def __init__(self):
        self.__id = ""
        self.__created_time = ""
        self.__message = ""
        self.__feed_targeting = None
        self.__is_hidden = ""
        self.__link = ""
        self.__from_ = ""
        self.__message_tags = list()
        self.__picture = ""
        self.__place = ""
        self.__privacy = ""
        self.__shares = ""
        self.__video = None
        self.__type = ""  # enum{link, status, photo, video, offer}
        self.__with_ = list()

    @property
    def id(self) -> str:
        """Identificador da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def created_time(self) -> str:
        """Horário de criação do Post"""
        return self.__created_time

    @created_time.setter
    def created_time(self, val: str):
        self.__created_time = val

    @property
    def message(self) -> str:
        """O texto do Post"""
        return self.__message

    @message.setter
    def message(self, val: str):
        self.__message = val

    @property
    def feed_targeting(self) -> 'FeedTargeting':
        """Público alvo do Post"""
        return self.__feed_targeting

    @feed_targeting.setter
    def feed_targeting(self, val: 'FeedTargeting'):
        self.__feed_targeting = val

    @property
    def is_hidden(self) -> str:
        """Indica se o Post está oculto"""
        return self.__is_hidden

    @is_hidden.setter
    def is_hidden(self, val: str):
        self.__is_hidden = val

    @property
    def link(self) -> str:
        """Url para o Post"""
        return self.__link

    @link.setter
    def link(self, val: str):
        self.__link = val

    @property
    def from_(self) -> str:
        """Remetente do Post"""
        return self.__from_

    @from_.setter
    def from_(self, val: str):
        self.__from_ = val

    @property
    def message_tags(self) -> List[str]:
        """Lista de perfis mencionados no Post"""
        return self.__message_tags

    @message_tags.setter
    def message_tags(self, val: List[str]):
        self.__message_tags = val

    @property
    def picture(self) -> str:
        """URL para imagem anexada ao Post"""
        return self.__picture

    @picture.setter
    def picture(self, val: str):
        self.__picture = val

    @property
    def place(self) -> str:
        """Indicador do local relacionado ao Post"""
        return self.__place

    @place.setter
    def place(self, val: str):
        self.__place = val

    @property
    def privacy(self) -> str:
        """Configurações de privacidade do Post"""
        return self.__privacy

    @privacy.setter
    def privacy(self, val: str):
        self.__privacy = val

    @property
    def shares(self) -> str:
        """Quantidade de compartilhamentos do Post"""
        return self.__shares

    @shares.setter
    def shares(self, val: str):
        self.__shares = val

    @property
    def video(self) -> Video:
        """Video anexado ao Post"""
        return self.__video

    @video.setter
    def video(self, val: Video):
        self.__video = val

    @property
    def type(self) -> str:
        """Tipo de conteúdo do Post:  enum{link, status, photo, video, offer}"""
        return self.__type

    @type.setter
    def type(self, val: str):
        self.__type = val

    @property
    def with_(self) -> List[str]:
        """Perfis mencionados no Post como co-participantes do conteúdo"""
        return self.__with_

    @with_.setter
    def with_(self, val: List[str]):
        self.__with_ = val


class FeedTargeting:
    """
    Essa classe representa um conjunto de configurações de público alvo
    """

    def __init__(self):
        self.__age_max = ""
        self.__age_min = ""
        self.__genders = ""
        self.__geo_locations = ""
        self.__locales = ""
        self.__education_statuses = ""
        self.__fan_of = ""
        self.__relationship_statuses = ""

    @property
    def age_max(self) -> str:
        """Idade máxima"""
        return self.__age_max

    @age_max.setter
    def age_max(self, val: str):
        self.__age_max = val

    @property
    def age_min(self) -> str:
        """Idade mínima"""
        return self.__age_min

    @age_min.setter
    def age_min(self, val: str):
        self.__age_min = val

    @property
    def genders(self) -> str:
        """Gêneros"""
        return self.__genders

    @genders.setter
    def genders(self, val: str):
        self.__genders = val

    @property
    def geo_locations(self) -> str:
        """Localizações geográficas"""
        return self.__geo_locations

    @geo_locations.setter
    def geo_locations(self, val: str):
        self.__geo_locations = val

    @property
    def locales(self) -> str:
        """Países"""
        return self.__locales

    @locales.setter
    def locales(self, val: str):
        self.__locales = val

    @property
    def education_statuses(self) -> str:
        """Escolaridade"""
        return self.__education_statuses

    @education_statuses.setter
    def education_statuses(self, val: str):
        self.__education_statuses = val

    @property
    def fan_of(self) -> str:
        """Fã de:"""
        return self.__fan_of

    @fan_of.setter
    def fan_of(self, val: str):
        self.__fan_of = val

    @property
    def relationship_statuses(self) -> str:
        """Relacionamento"""
        return self.__relationship_statuses

    @relationship_statuses.setter
    def relationship_statuses(self, val: str):
        self.__relationship_statuses = val
