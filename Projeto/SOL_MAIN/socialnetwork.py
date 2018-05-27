#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from SOL_MAIN.user import User
from SOL_MAIN.post import Post
from typing import List


class SocialNetwork(ABC):
    """
    A classe que define o comportamento de uma rede social
    A ferramenta SOL_MAIN é extensível e admite a adição de novas redes sociais.
    Essa classe define o acesso a recursos comuns à maioria das redes sociais, isso nos permite aumentar a abstração e
    facilitar a integração entre diferentes redes sociais
    """

    def __init__(self):
        self.__website = ""
        self.__name = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def website(self) -> str:
        return self.__website

    @website.setter
    def website(self, val: str):
        self.__website = val

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

    def post(self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Post = None) -> None:
        """
        Adiciona conteúdo do usuário credenciado à rede social.

        O método prevê a inclusão de diversos tipos de mídia ao conteúdo. Fica sob responsabilidade
        da classe de implementação restringir por meio de excessões combinações de parâmetros que não estejam de acordo
        com a realidade da rede social ou dos recursos implementados.

        Args:
            text:           Uma string contendo o texto que faz parte do conteúdo da publicação.
            image:          Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:          Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
            genericfile:    Em casos de redes sociais que permitem a inserção de qualquer tipo de arquivo, esse
                            parâmetro deverá ser preenchido com o endereço do arquivo que faz parte do conteúdo da
                            publicação.
            post:           Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada
                            à rede social.

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        if self.user is None:
            raise ValueError('This SocialNetwork has no authenticated user.')
        else:
            self.user.post(text, image, video, genericfile, post)

    def read(self, post_id: str = '', limit: int = 100) -> List[Post]:
        """
        Recupera conteúdo da rede social.

        O método prevê a solicitação de um Post específico a partir de seu ID.
        O método também prevê a especificação de um limite de Posts a serem retornados.

        Args:
            post_id: Uma string contendo o ID de um Post da rede social, caso queira recuperar um post específico.
            limit:  Um número inteiro contendo a quantidade máxima de registro que devem ser retornados.

        :return: Uma lista de Posts

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        if self.user is None:
            raise ValueError('This SocialNetwork has no authenticated user.')
        else:
            return self.user.read(post_id, limit)
