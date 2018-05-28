#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Place:
    """
    Essa classe representa um local
    """

    def __init__(self):
        self.__attributes = None
        self.__bounding_box = None
        self.__country = ""
        self.__country_code = ""
        self.__full_name = ""
        self.__id = ""
        self.__name = ""
        self.__place_type = ""
        self.__url = ""

    @property
    def attributes(self) -> 'PlaceAttributes':
        """Atributos relacionados ao local"""
        return self.__attributes

    @attributes.setter
    def attributes(self, val: 'PlaceAttributes'):
        self.__attributes = val

    @property
    def bounding_box(self) -> 'BoundingBox':
        """Objeto do tipo BoundingBox relacionado ao local"""
        return self.__bounding_box

    @bounding_box.setter
    def bounding_box(self, val: 'BoundingBox'):
        self.__bounding_box = val

    @property
    def country(self) -> str:
        """País"""
        return self.__country

    @country.setter
    def country(self, val: str):
        self.__country = val

    @property
    def country_code(self) -> str:
        """Código do país"""
        return self.__country_code

    @country_code.setter
    def country_code(self, val: str):
        self.__country_code = val

    @property
    def full_name(self) -> str:
        """Nome completo do local"""
        return self.__full_name

    @full_name.setter
    def full_name(self, val: str):
        self.__full_name = val

    @property
    def id(self) -> str:
        """Identificador da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def name(self) -> str:
        """Nome do local"""
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def place_type(self) -> str:
        """Tipo"""
        return self.__place_type

    @place_type.setter
    def place_type(self, val: str):
        self.__place_type = val

    @property
    def url(self) -> str:
        """URL"""
        return self.__url

    @url.setter
    def url(self, val: str):
        self.__url = val


class PlaceAttributes:
    """
    Essa classe agrega informações diversas sobre um local
    """

    def __init__(self):
        self.__street_address = ""
        self.__locality = ""
        self.__region = ""
        self.__postal_code = ""
        self.__phone = ""
        self.__twitter = ""
        self.__url = ""
        self.__app_id = ""

    @property
    def street_address(self) -> str:
        """Rua"""
        return self.__street_address

    @street_address.setter
    def street_address(self, val: str):
        self.__street_address = val

    @property
    def locality(self) -> str:
        """Bairro"""
        return self.__locality

    @locality.setter
    def locality(self, val: str):
        self.__locality = val

    @property
    def region(self) -> str:
        """Região"""
        return self.__region

    @region.setter
    def region(self, val: str):
        self.__region = val

    @property
    def postal_code(self) -> str:
        """CEP"""
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, val: str):
        self.__postal_code = val

    @property
    def phone(self) -> str:
        """Telefone"""
        return self.__phone

    @phone.setter
    def phone(self, val: str):
        self.__phone = val

    @property
    def twitter(self) -> str:
        """Perfil no Twitter"""
        return self.__twitter

    @twitter.setter
    def twitter(self, val: str):
        self.__twitter = val

    @property
    def url(self) -> str:
        """URL"""
        return self.__url

    @url.setter
    def url(self, val: str):
        self.__url = val


class BoundingBox:
    """
    Essa classe agrega coordenadas de pontos geógraficos que representam vértices de fronteiras de um local.
    É possível obter informações sobre essa abordagem aqui: https://pt.wikipedia.org/wiki/Caixa_delimitadora_m%C3%ADnima
    """

    def __init__(self):
        self.__coordinates = ""
        self.__type = ""

    @property
    def coordinates(self) -> str:
        """Coordenadas"""
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, val: str):
        self.__coordinates = val

    @property
    def type(self) -> str:
        """Figura geométrica que define a quantidade e configuração dos vértices"""
        return self.__type

    @type.setter
    def type(self, val: str):
        self.__type = val
