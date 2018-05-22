#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CoverPhoto:
    """
    Essa classe representa a foto de capa de um usuário
    """

    def __init__(self):
        self.__id = ""
        self.__cover_id = ""
        self.__offset_x = ""
        self.__offset_y = ""
        self.__source = ""

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def cover_id(self) -> str:
        return self.__cover_id

    @cover_id.setter
    def cover_id(self, val: str):
        self.__cover_id = val

    @property
    def offset_x(self) -> str:
        return self.__offset_x

    @offset_x.setter
    def offset_x(self, val: str):
        self.__offset_x = val

    @property
    def offset_y(self) -> str:
        return self.__offset_y

    @offset_y.setter
    def offset_y(self, val: str):
        self.__offset_y = val

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, val: str):
        self.__source = val
