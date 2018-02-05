#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Place:
    """
    Essa classe representa um local
    """

    def __init__(self):
        self.attributes = None
        self.bounding_box = None
        self.country = ""
        self.country_code = ""
        self.full_name = ""
        self.id = id
        self.name = ""
        self.place_type = ""
        self.url = ""

class Place_Attributes:
    """
    Essa classe agrega informações diversas sobre um local
    """

    def __init__(self):
        self.street_address = ""
        self.locality = ""
        self.region = ""
        self.iso3 = ""
        self.postal_code = ""
        self.phone = ""
        self.twitter = ""
        self.url = ""
        self.app_id = ""

class Bounding_box:
    """
    Essa classe agrega coordenadas de pontos geógraficos que representam vértices de fronteiras de um local.
    É possível obter informações sobre essa abordagem aqui: https://pt.wikipedia.org/wiki/Caixa_delimitadora_m%C3%ADnima
    """

    def __init__(self):
        self.coordinates = ""
        self.type = ""


