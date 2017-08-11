#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from SOL_MAIN.user import User


class SocialNetwork(ABC):
    """
    A classe que define o comportamento de uma rede social
    A ferramenta SOL_MAIN é extensível e admite a adição de novas redes sociais.
    Essa classe define o acesso a recursos comuns à maioria das redes sociais, isso nos permite aumentar a abstração
    e facilitar a integração entre diferentes redes sociais
    """

    @property
    @abstractmethod
    def user(self) -> User:
        """Representa o usuário principal da aplicação."""
        raise NotImplementedError('Not Implemented Feature!')

    @user.setter
    @abstractmethod
    def user(self, val: User):
        """
        Para a maioria das redes sociais é recomendável que seja feito algum tipo de validação
         das credenciais de acesso do usuário neste local
        """
        raise NotImplementedError('Not Implemented Feature!')

    def post(self)->None:
        if self.user is None:
            raise ValueError('A user must be defined in order to use this feature.')
        else:
            self.user.post()

    def __init__(self):
        pass
