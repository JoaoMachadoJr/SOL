#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Media:
    """
    Essa classe representa uma media. Usualmente, se trata de uma imagem ou um vídeo.
    """

    def __init__(self):
        self.__display_url = ""
        self.__expanded_url = ""
        self.__id = ""
        self.__media_url = ""
        self.__sizes = None
        self.__source_status_id = ""
        self.__type = ""
        self.__url = ""

    @property
    def display_url(self) -> str:
        """URL para a mídia dentro do Twitter"""
        return self.__display_url

    @display_url.setter
    def display_url(self, val: str):
        self.__display_url = val

    @property
    def expanded_url(self) -> str:
        """Versão expandida da URL"""
        return self.__expanded_url

    @expanded_url.setter
    def expanded_url(self, val: str):
        self.__expanded_url = val

    @property
    def id(self) -> str:
        """Identificador da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def media_url(self) -> str:
        """URL direta para a mídia"""
        return self.__media_url

    @media_url.setter
    def media_url(self, val: str):
        self.__media_url = val

    @property
    def sizes(self) -> 'Size':
        """Informações de tamanho do quadro da mídia"""
        return self.__sizes

    @sizes.setter
    def sizes(self, val: 'Size'):
        self.__sizes = val

    @property
    def source_status_id(self) -> str:
        """Identificador do tweet"""
        return self.__source_status_id

    @source_status_id.setter
    def source_status_id(self, val: str):
        self.__source_status_id = val

    @property
    def type(self) -> str:
        """Tipo de mídia"""
        return self.__type

    @type.setter
    def type(self, val: str):
        self.__type = val

    @property
    def url(self) -> str:
        """URL resumida dentro do Twitter"""
        return self.__url

    @url.setter
    def url(self, val: str):
        self.__url = val


class Size:
    """
    Essa classe agrega as dimensões de uma imagem ou vídeo.
    """

    def __init__(self):
        self.__h = ""
        self.__resize = ""
        self.__w = ""

    @property
    def h(self) -> str:
        """Tamanho vertical"""
        return self.__h

    @h.setter
    def h(self, val: str):
        self.__h = val

    @property
    def resize(self) -> str:
        """Método de enquadramento utilizado. enum{fit, crop}"""
        return self.__resize

    @resize.setter
    def resize(self, val: str):
        self.__resize = val

    @property
    def w(self) -> str:
        """Tamanho horizontal"""
        return self.__w

    @w.setter
    def w(self, val: str):
        self.__w = val
