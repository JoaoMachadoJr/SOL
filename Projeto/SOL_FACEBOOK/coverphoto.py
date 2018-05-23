#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CoverPhoto:
    """
    Essa classe representa a foto de capa de um usuário
    """

    def __init__(self):
        self.__id = ""
        self.__offset_x = ""
        self.__offset_y = ""
        self.__source = ""

    @property
    def id(self) -> str:
        """Identificador único da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def offset_x(self) -> str:
        """Deslocamento horizontal da foto"""
        return self.__offset_x

    @offset_x.setter
    def offset_x(self, val: str):
        self.__offset_x = val

    @property
    def offset_y(self) -> str:
        """Deslocamento vertical da foto"""
        return self.__offset_y

    @offset_y.setter
    def offset_y(self, val: str):
        self.__offset_y = val

    @property
    def source(self) -> str:
        """Link direto para a imagem"""
        return self.__source

    @source.setter
    def source(self, val: str):
        self.__source = val
