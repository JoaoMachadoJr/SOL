__author__ = 'Joao'
#from SolFB import *
#User_Facebook= User
import sys
sys.path.append("lib")

import _User
import _Access
import _Actions
import _Tweet
import _User
import _Actions
import _List
Actions = _Actions.Actions

Consumer_Key = "aqJhPEV5nKmki92nM8kDKeJdR"
Consumer_Secret= "WQ3aYy6brirvCkYWRtkmf6iyZSUjvzyLxc9Xu9MGFx1MxjYpNw"
Access_Token_Secret="6D1XaR1ZMj2spCGogmD1vHG12RxMk1tvmzs0kkZhlmmsK"
Access_Token="179494740-x4OS9UjoxYDOYElxh8izYMnca5V0ilq3yJpVZ3lR"

#api = tweepy.API()
#ID Smurf= 741008881145548800


#acesso = _Access.StrongAccess(Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret)
acesso = _Access.StrongAccess(Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret)

#Joao = Actions.me()
#Joao2 = _Actions.Actions.getUser(741008881145548800)
#mentions = Joao.getMentionsTimeline(count=2, since_id=None, max_id=None)
#id=mentions[0].user.id
#mentions = _User.User(id=741008881145548800).getTimeline()
#tweetSerra = _Tweet.Tweet(id=742841643259334660)
#tweetPunch = _Tweet.Tweet(id=143763933654827008)
#mentions =_Actions.Actions.getFriendshipInfo(source_id=Joao.id,target_id=Joao2.id);
#help(Joao)
#print(tweetSerra.getRetweeters())






'''
#Destruindo meu mais recente Tweet pelo seu objeto
Joao =acesso.me()       #Meu usuario
lista=Joao.getTimeline()      #Minha Timeline
tweet = lista[0]            #Pego o ultimo post da timeline
print(tweet.postDestroy(acesso))   #<--- destruo o post
'''
'''
#Destruindo meu mais recente Tweet pelo seu ID
_Actions.Actions.postDestroyTweetById(741536688992706560)
'''
'''
#Fazendo um post no Twitter
Joao = acesso.me()
texto = "Esse é um texto de teste para um post no twitter"
latitude=-22.503640
longitude= -41.923904
Joao.postTweet(texto,latitude,longitude)
'''
'''
#Respondendo a um post no twitter
Joao=acesso.me()
post=_Tweet.Tweet(763838518422605824)
texto="testando resposta"
post.postReply(msg=texto)
'''
'''
#Retweetando
Joao=acesso.me()
tweet=_Tweet.Tweet(734456681669746693)
tweet.postRetweet(Access=acesso)
'''
'''
#Enviando mensagem
Joao = acesso.me()
Remetente = Actions.getUser("JMachadoJr");
texto = "Teste de envio de mensagem";
Joao.postDirectMessage(Remetente,texto,acesso)
'''
'''
#Enviando mensagem (Pelo ID)
Joao = acesso.me()
texto = "Teste de envio de mensagem";
Joao.postDirectMessage("JMachadoJr",texto,acesso)
'''
'''
#Exibe a ultima mensagem, apaga, e exibe a nova ultima mensagem
Joao=acesso.me()
mensagem=Joao.getDirectMessages(Access=acesso)[0]
print(mensagem)
print(mensagem.postDestroy(Access=acesso))
mensagem=Joao.getDirectMessages(Access=acesso)[0]
print(mensagem)
'''
'''
#Criando amizade entre dois usuarios
Joao=acesso.me()
resposta=Joao.postFriendshipCreate("JmachadoJr", False)
print(resposta)
'''
'''
#Desfazendo amizade entre dois usuarios
Joao=acesso.me()
resposta=Joao.postFriendshipDestroy("JmachadoJr")
print(resposta)
'''
'''
#Pega lista de amigos
Joao=acesso.me()
resposta=Joao.getFriends()
for u in resposta:
    print(u.name)
'''
'''
#Pega lista de seguidores
Joao=acesso.me()
resposta=Joao.getFollowers()
for u in resposta:
    print(u.name)
'''
'''
#Exibe estado de amizade entre dois usuarios
Joao=acesso.me()
resposta=Joao.getFriendship("JmachadoJr")
print(resposta)
'''
'''
#Exibe se o acesso possui credenciais corretamente
print(acesso.verify_credentials())
'''
'''
#Exibe a quantidade de requisições que essa API pode fazer na proxima hora
print(acesso.rate_limit_status())
'''
'''
#Altera minha descrição no meu perfil
Joao=acesso.me()
print(Joao.postUpdateProfile(description="Teste de mudança de descrição"))
'''
'''
#alterando minha imagem de perfil
Joao=acesso.me()
print(Joao.postUpdateProfileImage("C:\\Users\\Joao\\Pictures\\Imagens2\\Foto0022.jpg"))
'''
'''
#Bloqueia um usuario, exibe a lista de bloqueados. Desbloqueia, exibe a lista de bloqueados.
Joao=acesso.me()
print("Bloqueio: "+str(Joao.postBlockCreate("JmachadoJr")))
print("LISTA DE USUARIOS BLOQUEADOS")
for bloqueado in Joao.getBlocks():
    print("Esse usuário está bloqueado: "+str(bloqueado))
print("Desbloqueio "+str(Joao.postBlockDestroy("JmachadoJr")))
print("LISTA DE USUARIOS BLOQUEADOS")
for bloqueado in Joao.getBlocks():
    print("Esse usuário está bloqueado: "+str(bloqueado))
'''
'''
#Altera umagem de fundo
Joao=acesso.me()
print(Joao.postUpdateProfileBanner("C:\\Users\\Joao\\Pictures\\fma.jpg"))
'''
'''
#Pego usuarios sugeridos a partir de um SLUG (SLUG é como um 'tema')
Joao=acesso.me()
print(Joao.getSuggestedUsers(slug="música"))
'''
'''
#Pego slugs sugeridos para mim
Joao=acesso.me()
print(Joao.getSuggestedCategories())
'''
'''
#Pego usuarios vinculados a um SLUG assim como seu ultimo tweet
Joao=acesso.me()
print(Joao.getSuggestedUsersWithTweetBySlug(slug="música"))
'''
'''
#Pego tweetes favoritos de um usuario
Joao=acesso.me()
for tweet in Joao.getFavorites(0):
    print(tweet)
'''
'''
#Favorito um tweet
Joao=acesso.me()
tweet = _Tweet.Tweet(id=767160987720056832)
print(tweet.postFavoriteCreate())
'''
'''
#Desfavorito um tweet
Joao=acesso.me()
tweet = _Tweet.Tweet(id=767160987720056832)
print(tweet.postFavoriteDestroy())
'''
'''
#Pego listas vinculadas ao usuario
Joao=acesso.me()
listas=Joao.getLists()
for l in listas:
    print(l)
'''
'''
#Tweets de uma lista
Joao= acesso.me()
lista = _List.List()
lista.slug="pokemon"
lista.user="LainadAngouleme"
for tweet in lista.getTweets():
    print(tweet)
'''
'''
#Removendo um usuário de uma lista
Joao=acesso.me()
print(_Actions.Actions.postRemoveMemberFromList("NoMansSkyGame",slug="minha-lista",owner_screen_name="joaoxmachado"))
'''
'''
#Listas que NoMAnSky é membro
Joao=acesso.me()
NoMansSky=Actions.getUser("nomanssky")
for lista in NoMansSky.getLists(count=1000):
    print (lista)
'''
'''
#Subscriptions de uma Lista
Joao= acesso.me()
lista = _List.List()
lista.slug="pokemon"
lista.user="LainadAngouleme"
for tweet in lista.getSubscribers():
    print(tweet)
'''
'''
#Faço Subscribe em uma lista
Joao=acesso.me()
print(Joao.postSubscribe(owner_screen_name="LainadAngouleme",slug="hogwarts"))
'''
'''
#Verifico se o usuario é subscriber de uma lista
Joao=acesso.me()
print(Joao.getIsSubscriber(owner_screen_name="LainadAngouleme",slug="hogwarts"))
'''
'''
#Faço Unsubscribe em uma lista
Joao=acesso.me()
print(Joao.postSubscribeDestroy(owner_screen_name="LainadAngouleme",slug="hogwarts"))
'''
'''
#Verifica se um usuario é membro de uma lista
Joao=acesso.me()
SlytherinWorld=Actions.getUser("SlytherinWorld")
print(SlytherinWorld.getIsMember(owner_screen_name="LainadAngouleme",slug="hogwarts"))
'''
'''
#Pega a lista de usuarios de uma lista
Joao= acesso.me()
lista = _List.List()
lista.slug="pokemon"
lista.user="LainadAngouleme"
for tweet in lista.getMembers():
    print(tweet.name)
'''
'''
#Adiciona um usuario a uma lista como membro
Joao= acesso.me()
lista = _List.List()
lista.slug="minha-lista"
lista.user="JoaoxMachado"
print(lista.postMemberCreate(screen_name="NoMansSkyHub"))
'''




'''FALTA                                    JÁ FEITO                              REMOVIDOS (Incapacidade ou desinteresse em concluir)

                                            GET statuses/mentions_timeline
                                            GET statuses/user_timeline
                                            GET statuses/home_timeline
                                            GET statuses/retweets_of_me
                                            GET statuses/retweets/:id
                                            GET statuses/show/:id
                                            POST statuses/destroy/:id
                                            POST statuses/update
                                            POST statuses/retweet/:id
                                                                                    POST statuses/unretweet/:id
                                                                                    POST statuses/update_with_media
                                            GET statuses/oembed
                                            GET statuses/retweeters/ids
                                            GET statuses/lookup
                                            GET direct_messages/sent
                                            GET direct_messages/show
                                            GET search/tweets
                                            GET direct_messages
                                            POST direct_messages/destroy
                                            POST direct_messages/new
                                                                                  (REMOVED) GET friendships/no_retweets/ids
                                            GET friends/ids
                                            GET followers/ids
                                            GET friendships/incoming
                                            GET friendships/outgoing
                                            POST friendships/create
                                            POST friendships/destroy
                                                                                   (Não atendido pelo Tweepy) POST friendships/update
                                            GET friendships/show
                                            GET friends/list
                                            GET followers/list
                                            GET friendships/lookup
                                                                                    (Não atendido pelo Tweepy)GET account/settings
                                            GET account/verify_credentials
                                                                                    (Não atendido pelo Tweepy)POST account/settings
                                            POST account/update_profile
                                            POST account/update_profile_image
                                            GET blocks/list
                                                                                    (Se o metodo acima funciona, esse metodo é pouco interessante)GET blocks/ids
                                            POST blocks/create
                                            POST blocks/destroy
                                            GET users/lookup
                                            GET users/show
                                            GET users/search
                                                                                    (Não atendido pelo Tweepy) POST account/remove_profile_banner
                                            POST account/update_profile_banner
                                                                                    (Não atendido pelo Tweepy) GET users/profile_banner
                                                                                    (Não atendido pelo Tweepy)POST mutes/users/create
                                                                                    (Não atendido pelo Tweepy)POST mutes/users/destroy
                                                                                    (Não atendido pelo Tweepy)GET mutes/users/ids
                                                                                    (Não atendido pelo Tweepy)GET mutes/users/list
                                            GET users/suggestions/:slug
                                            GET users/suggestions
                                            GET users/suggestions/:slug/members
                                            GET favorites/list
                                            POST favorites/destroy
                                            POST favorites/create
                                            GET lists/list
                                            GET lists/statuses
                                            POST lists/members/destroy
                                            GET lists/memberships
                                            GET lists/subscribers
                                            POST lists/subscribers/create
                                            GET lists/subscribers/show

                                            POST lists/subscribers/destroy
                                                                                    (Redundante) POST lists/members/create_all
                                            GET lists/members/show
                                            GET lists/members
                                            POST lists/members/create
POST lists/destroy
POST lists/update
POST lists/create
GET lists/show
GET lists/subscriptions

POST lists/members/destroy_all
GET lists/ownerships
GET saved_searches/list
GET saved_searches/show/:id
POST saved_searches/create
POST saved_searches/destroy/:id
GET geo/id/:place_id
GET geo/reverse_geocode
GET geo/search
POST geo/place

GET trends/place
GET trends/available
                                            GET application/rate_limit_status
GET help/configuration
GET help/languages
GET help/privacy
GET help/tos
GET trends/closest
POST users/report_spam
'''
