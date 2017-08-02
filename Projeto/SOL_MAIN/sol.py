#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Esse módulo define a classe principal dessa ferramenta

Esse módulo é o módulo de mais alto nível da ferramenta.
Ele funciona como o ponto de partida para o acesso aos demais módulos.
"""
from SOL_MAIN.socialnetwork import SocialNetwork


class SOL(object):
    """
    A classe principal da ferramenta
    """
    __SocialNetworks = SocialNetwork()

    def __init__(self):
        pass

