#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC


class SocialNetwork(ABC):
    """
    A classe que define o comportamento de uma rede social
    A ferramenta SOL_MAIN é extensível e admite a adição de novas redes sociais.
    Essa clase define o acesso a recursos comuns à maioria das redes sociais, isso nos permite aumentar a abstração
    e facilitar a integração entre diferentes redes sociais
    """



    def __init__(self):
        pass

