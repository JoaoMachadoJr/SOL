#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Video:
    """
    Reresenta um vídeo
    """

    def __init__(self):
        self.__id = ""
        self.__created_time = ""
        self.__description = ""
        self.__embed_html = ""
        self.__format = ""
        self.__from_ = ""
        self.__icon = ""
        self.__length = ""
        self.__permalink_url = ""
        self.__picture = ""
        self.__place = ""
        self.__privacy = ""
        self.__source = ""
        self.__status = ""
        self.__updated_time = ""

    @property
    def id(self) -> str:
        """Identificador da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def created_time(self) -> str:
        """Horário de criação"""
        return self.__created_time

    @created_time.setter
    def created_time(self, val: str):
        self.__created_time = val

    @property
    def description(self) -> str:
        """Descrição do vídeo"""
        return self.__description

    @description.setter
    def description(self, val: str):
        self.__description = val

    @property
    def embed_html(self) -> str:
        """Estrutura html para uso do vídeo para site externo"""
        return self.__embed_html

    @embed_html.setter
    def embed_html(self, val: str):
        self.__embed_html = val

    @property
    def format(self) -> str:
        """Formato"""
        return self.__format

    @format.setter
    def format(self, val: str):
        self.__format = val

    @property
    def from_(self) -> str:
        """Criador do vídeo"""
        return self.__from_

    @from_.setter
    def from_(self, val: str):
        self.__from_ = val

    @property
    def icon(self) -> str:
        """Ícone"""
        return self.__icon

    @icon.setter
    def icon(self, val: str):
        self.__icon = val

    @property
    def length(self) -> str:
        """Duração do vídeo"""
        return self.__length

    @length.setter
    def length(self, val: str):
        self.__length = val

    @property
    def permalink_url(self) -> str:
        """URL para o vídeo"""
        return self.__permalink_url

    @permalink_url.setter
    def permalink_url(self, val: str):
        self.__permalink_url = val

    @property
    def picture(self) -> str:
        """Imagem exibida quando o vídeo não está em reprodução"""
        return self.__picture

    @picture.setter
    def picture(self, val: str):
        self.__picture = val

    @property
    def place(self) -> str:
        """Local relacionado ao vídeo"""
        return self.__place

    @place.setter
    def place(self, val: str):
        self.__place = val

    @property
    def privacy(self) -> str:
        """Configurações de privacidade"""
        return self.__privacy

    @privacy.setter
    def privacy(self, val: str):
        self.__privacy = val

    @property
    def source(self) -> str:
        """URL para o vídeo"""
        return self.__source

    @source.setter
    def source(self, val: str):
        self.__source = val

    @property
    def status(self) -> str:
        """Conteúdo que acompanha o vídeo"""
        return self.__status

    @status.setter
    def status(self, val: str):
        self.__status = val

    @property
    def updated_time(self) -> str:
        """Horário da última atualização"""
        return self.__updated_time

    @updated_time.setter
    def updated_time(self, val: str):
        self.__updated_time = val
