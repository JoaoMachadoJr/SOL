#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_MAIN import SocialNetwork
from SOL_TWITTER.user import User
from SOL_TWITTER.tweet import Tweet
from SOL_TWITTER.factory import Factory
from lib import tweepy

class Twitter(SocialNetwork):
    """
    Essa classe representa a rede social Twitter.
    O endereço dessa rede social é: https://twitter.com/
    A documentação oficial da API de integração com o facebook utilizada por mim pode ser acessada pelo seguinte
      endereço: https://dev.twitter.com/rest/public
    Esse projeto fez uso da ferramenta tweepy, cuja documentação pode ser encontrada no endereço: http://www.tweepy.org/
    """

    def __init__(self, consumer_key: str = '',consumer_secret: str = '',access_token: str = '',access_token_secret: str = ''):
        """
        Args:
            consumer_key: Ao passar os quatro tokens para o construtor, o usuário proprietário do token será registrado como
                usuário principal
            consumer_secret: Ao passar os quatro tokens para o construtor, o usuário proprietário do token será registrado como
                usuário principal
            access_token: Ao passar os quatro tokens para o construtor, o usuário proprietário do token será registrado como
                usuário principal
            access_token_secret: Ao passar os quatro tokens para o construtor, o usuário proprietário do token será registrado como
                usuário principal
        """
        self.__user = None
        if (consumer_key!='') and (consumer_secret!='') and (access_token!='') and (access_token_secret!=''):
            self.login(consumer_key,consumer_secret,access_token,access_token_secret)
        self.name='Twitter'
        self.website='www.twitter.com'

    @property
    def user(self) -> User:
        """Representa o usuário principal do twitter, que estará autenticado."""
        return self.__user

    @user.setter
    def user(self, val: User):
        """
        Para a maioria das redes sociais é recomendável que seja feito algum tipo de validação
        das credenciais de acesso do usuário neste local
        """
        if not self.login(val.consumer_key,val.consumer_secret,val.access_token,val.access_token_secret):
            raise Exception('The user must have a valid user.token')

    def post(self, text: str = '', image: str = '', video: str = '', genericfile: str = '', post: Tweet = None) -> None:
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

    def login(self, consumer_key: str = '',consumer_secret: str = '',access_token: str = '',access_token_secret: str = '') -> User:
        """
        Esse método recebe o conjunto de tojens, valida-os, instancia um objeto representando o usuário dono dos tokens,
        registra esse usuário como o usuário principal dessa instancia Twitter, e retorna o objeto contendo as
        informações desse usuário

        Args:
            consumer_key: O token de identificação do aplicativo. Para obtê-lo consulte Twitter.login_instructions
            consumer_secret: O token secreto do aplicativo. Para obtê-lo consulte Twitter.login_instructions
            access_token: O token de acesso. do usuário Para obtê-lo consulte Twitter.login_instructions
            access_token_secret: O token secreto de acesso do usuário. Para obtê-lo consulte Twitter.login_instructions
        returns:
            Um objeto contendo informações sobre o usuário dono do token
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        auth.get_authorization_url()
        dictionary = tweepy.API(auth).me()
        a_user = Factory.user(dictionary)
        a_user.auth=auth
        self.__user=a_user
        return self.user


    @staticmethod
    def login_instructions():
        """
        Instrucoes de login do Twitter:
        login twitter:
        1- Vá para a página https://apps.twitter.com/
        2- Cadastre o seu aplicativo
        3- Acesse a página https://apps.twitter.com/app/, clique no seu aplicativo, e então clique em 'Keys and access tokens'
        4- Copie os campos: Consumer Key e Consumer Secret
        5- Clique em Generate Consumer Key and Secret e confirme a operação
        6- Copie os valores de Access Token e Access Token Secret
        7- Use os tokens obtidos no passo 5 e 7 para fazer o login pelo método Twitter.login
        """
        return """
        Instrucoes de login do Twitter:
        login twitter:
        1- Vá para a página https://apps.twitter.com/
        2- Cadastre o seu aplicativo
        3- Acesse a página https://apps.twitter.com/app/, clique no seu aplicativo, e então clique em 'Keys and access tokens'
        4- Copie os campos: Consumer Key e Consumer Secret
        5- Clique em Generate Consumer Key and Secret e confirme a operação
        6- Copie os valores de Access Token e Access Token Secret
        7- Use os tokens obtidos no passo 5 e 7 para fazer o login pelo método Twitter.login"""


