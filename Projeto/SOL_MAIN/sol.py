#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Esse módulo define a classe principal dessa ferramenta

Esse módulo é o módulo de mais alto nível da ferramenta.
Ele funciona como o ponto de partida para o acesso aos demais módulos.
"""
from SOL_MAIN.socialnetwork import SocialNetwork
from SOL_MAIN.socialnetwork import Post
from typing import List


class SOL(object):
    """
    A classe principal da ferramenta, que agrega uma lista de redes sociais permitindo operações conjuntas em todas elas
    """

    def __init__(self):
        self.socialnetworks = []  # type: List[SocialNetwork]

    def post(self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Post = None) -> None:
        """
        Adiciona conteúdo do usuário credenciado a todas as redes sociais cadastradas.

        O método prevê a inclusão de diversos tipos de mídia ao conteúdo. Fica sob responsabilidade
        da classe de implementação restringir por meio de excessões combinações de parâmetros que não estejam de acordo
        com a realidade da rede social ou dos recursos implementados.

        Args:
            text:           Uma string contendo o texto que faz parte do conteúdo da publicação.
            image:          Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:          Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
                            genericfile: Em casos de redes sociais que permitem a inserção de qualquer tipo de arquivo,
                            esse parâmetro deverá ser preenchido com o endereço do arquivo que faz parte do conteúdo da
                            publicação.
            post:           Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada
                            à rede social.
            genericfile:    Um arquivo a ser enviado para a rede social.

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        for aSocialNetwork in self.socialnetworks:
            aSocialNetwork.post(text, image, video, genericfile, post)

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
        limit_sn = limit // len(self.socialnetworks)
        result = list()
        for a_social_network in self.socialnetworks:
            result = result + a_social_network.read(post_id, limit_sn)
        return result

