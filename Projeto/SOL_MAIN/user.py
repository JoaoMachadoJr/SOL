#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from SOL_MAIN.post import Post
from typing import List


class User(ABC):
    """
    Essa classe representa o usuário de uma rede social.
    """

    @abstractmethod
    def post(self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Post = None) -> None:
        """
        Adiciona conteúdo desse usuário credenciado à rede social.

        O método prevê a inclusão de diversos tipos de mídia ao conteúdo. Fica sob responsabilidade
        da classe de implementação restringir por meio de excessões combinações de parâmetros que não estejam de acordo
        com a realidade da rede social ou dos recursos implementados.

        Args:
            text:        Uma string contendo o texto que faz parte do conteúdo da publicação.
            image:       Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:       Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
            genericfile: Em casos de redes sociais que permitem a inserção de qualquer tipo de arquivo, esse
                         parâmetro deverá ser preenchido com o endereço do arquivo que faz parte do conteúdo da
                         publicação.
            post:        Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada à
                         rede social.
        """
        raise NotImplementedError('Not Implemented Feature!')

    @abstractmethod
    def read(self, post_id: str = '', limit: int = 100) -> List[Post]:
        """
        Recupera conteúdo da rede social.

        O método prevê a solicitação de um Post específico a partir de seu ID.
        O método também prevê a especificação de um limite de Posts a serem retornados.

        Args:
            post_id: Uma string contendo o ID de um Post da rede social, caso queira recuperar um post específico.
            limit:  Um número inteiro contendo a quantidades máxima de registro que devem ser retornados.

        :return: Uma lista de Posts

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        raise NotImplementedError('Not Implemented Feature!')
