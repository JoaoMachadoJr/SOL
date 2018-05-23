#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_MAIN import SocialNetwork
from SOL_FACEBOOK.user import User
from SOL_FACEBOOK.post import Post
from SOL_FACEBOOK.connection import Connection
from SOL_FACEBOOK.factory import Factory
from typing import List


class Facebook(SocialNetwork):
    """
    Essa classe representa a rede social Facebook.
    O endereço dessa rede social é: https://Facebook.com
    A documentação oficial da API de integração com o facebook utilizada por mim pode ser acessada pelo seguinte
      endereço: https://developers.facebook.com/docs/graph-api
    """

    def __init__(self, token: str = ''):
        """
        Args:
            token: Ao passar um token para o construtor, o usuário proprietário do token será registrado como usuário
                   principal
        """
        super().__init__()
        self.__user = None
        if token != '':
            self.login(token)
        self.name = 'Facebook'
        self.website = 'www.facebook.com'

    @property
    def user(self) -> User:
        """Representa o usuário principal do facebook, que estará autenticado."""
        return self.__user

    @user.setter
    def user(self, val: User):
        """
        Para a maioria das redes sociais é recomendável que seja feito algum tipo de validação
        das credenciais de acesso do usuário neste local
        """
        if not self.login(val.token):
            raise Exception('The user must have a valid user.token')

    def post(self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Post = None) -> None:
        """
        Adiciona conteúdo do usuário credenciado à rede social.

        O método prevê a inclusão de diversos tipos de mídia ao conteúdo. Fica sob responsabilidade
        da classe de implementação restringir por meio de excessões combinações de parâmetros que não estejam de acordo
        com a realidade da rede social ou dos recursos implementados.

        Args:
            text:        Uma string contendo o texto que faz parte do conteúdo da publicação.
            image:       Uma string contendo o endereço da imagem que faz parte do conteúdo da publicação.
            video:       Uma string contendo o endereço do video que faz parte do conteúdo da publicação.
            genericfile: Em casos de redes sociais que permitem a inserção de qualquer tipo de arquivo, esse parâmetro
                         deverá ser preenchido com o endereço do arquivo que faz parte do conteúdo da publicação.
            post:        Um objeto do tipo Post que representa uma publicação já preenchida e pronta para ser enviada à
                         rede social.

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        if self.user is None:
            raise ValueError('This SocialNetwork has no authenticated user.')
        else:
            self.user.post(text, image, video, genericfile, post)

    def login(self, token: str) -> User:
        """
        Esse método recebe um token, valida esse token, instancia um objeto representando o usuário dono do token,
        registra esse usuário como o usuário principal dessa instancia Facebook, e retorna o objeto contendo as
        informações desse usuário

        Args:
            token: O token de acesso. Para obtê-lo consulte Facebook.login_instructions
        returns:
            Um objeto contendo informações sobre o usuário dono do token
        """
        dict_user = Connection.get(
            "https://graph.facebook.com/v2.6/me?&fields="+User.fields()+"&access_token=" + str(token))
        a_user = Factory.user(dict_user)
        if a_user.name != '':
            self.__user = a_user
            a_user.token = token
            return a_user

    @staticmethod
    def login_instructions() -> str:
        """
        Instruções de login do facebook:
        1- Acesse a página MEUS APLICATIVOS: https://developers.facebook.com/apps/
        2- Crie um aplicativo e obtenha um ID numérico, que será chamado de APPID nesse tutorial
        3- Acesse a página do Graph API Explorer: https://developers.facebook.com/tools/explorer
        4- Selecione seu aplicativo na direita
        5- Clique em Obter Token > Obter Token de acesso do usuário
        6- Ao abrir a página de permissões, selecione todas as permissões exibidas
        7- Confirme todas as mensagens pop-ups de permissões. Será exibido o seu token de acesso, guarde-o

        (Opcional) Como obter um token de acesso de maior duração
        1- Acesse a página: https://developers.facebook.com/apps/{seu APPID}/dashboard/
        2- No campo Chave Secreta do APlicativo, clique em Mostrar
        3- Copie essa chave secreta, nesse tutorial a chamaremos de CLIENTE_KEY
        4- Acesse o endereço: https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token
                              &client_id={Seu APPID}&client_secret={Sua CLIENTE_KEY}&fb_exchange_token={Seu Token}
        5- A resposta será um json, o texto entre áspas exibido após "Access_token" é um token com 60 dias de duração
        """
        return "Instruções de login do facebook:\n" \
               "1- Acesse a página MEUS APLICATIVOS: https://developers.facebook.com/apps/\n"\
               "2- Crie um aplicativo e obtenha um ID numérico, que será chamado de APPID nesse tutorial\n"\
               "3- Acesse a página do Graph API Explorer: https://developers.facebook.com/tools/explorer\n"\
               "4- Selecione seu aplicativo na direita\n"\
               "5- Clique em Obter Token > Obter Token de acesso do usuário\n"\
               "6- Ao abrir a página de permissões, selecione todas as permissões exibidas\n"\
               "7- Confirme todas as mensagens pop-ups de permissões. Será exibido o seu token de acesso, guarde-o\n"\
               "\n"\
               "(Opcional) Como obter um token de acesso de maior duração\n"\
               "1- Acesse a página: https://developers.facebook.com/apps/{seu APPID}/dashboard/\n"\
               "2- No campo Chave Secreta do APlicativo, clique em Mostrar\n"\
               "3- Copie essa chave secreta, nesse tutorial a chamaremos de CLIENTE_KEY\n"\
               "4- Acesse o endereço: https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token"\
               "&client_id={Seu APPID}&client_secret={Sua CLIENTE_KEY}&fb_exchange_token={Seu Token}\n"\
               "5- A resposta será um json, o texto entre áspas exibido após ""Access_token"" é um token com 60 dias"\
               "de duração"

    def read(self, post_id: str = '', limit: int = 100) -> List[Post]:
        """
        Recupera conteúdo da rede social.
        Atualmente não é possível ler a timeline de um usuário, portanto esse método lê o conteúdo presente no mural
        de um usuário

        O método prevê a solicitação de um Post específico a partir de seu ID.
        O método também prevê a especificação de um limite de Posts a serem retornados.

        Args:
            post_id: Uma string contendo o ID de um Post da rede social, caso queira recuperar um post específico.
            limit:  Um número inteiro contendo a quantidade máxima de registro que devem ser retornados.

        Raises:
            ValueError: Não há um usuário credenciado vinculado ao objeto SocialNetwork
        """
        if self.user is None:
            raise ValueError('This SocialNetwork has no authenticated user.')
        else:
            return self.user.read(post_id, limit)
