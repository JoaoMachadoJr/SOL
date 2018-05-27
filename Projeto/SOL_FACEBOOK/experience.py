#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Experience:
    """
    Essa classe vincula informações sobre um gosto, pessoa, atividade ou entidade genérica a um usuário
    Exemplo: Um atleta favorito, um time, uma figura pública inspiracional, um idioma, uma área de conhecimento
    """

    def __init__(self):
        self.__id = ""
        self.__description = ""
        self.__from_ = None
        self.__name = ""
        self.__with_ = list()

    @property
    def id(self) -> str:
        """Identificador único da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def description(self) -> str:
        """Descrição da entidade"""
        return self.__description

    @description.setter
    def description(self, val: str):
        self.__description = val

    @property
    def from_(self) -> 'User':
        """Usuário proprietário da entidade"""
        return self.__from_

    @from_.setter
    def from_(self, val: 'User'):
        self.__from_ = val

    @property
    def name(self) -> str:
        """Nome da experiência"""
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def with_(self) -> List['User']:
        """Outros usuário relacionados"""
        return self.__with_

    @with_.setter
    def with_(self, val: List['User']):
        self.__with_ = val
