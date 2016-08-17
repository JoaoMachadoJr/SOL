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
#Caso de uso 1 (4 linhas): Pegar posts da Dilma de 2015 (Mesma coisa que o código do wladek fazia)
u = User("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
posts=Page("Dilmarousseff").getPosts(dateMin=Utility.date("01/01/2015"),dateMax=Utility.date("31/12/2015"),limit=100)
for post in posts:
    print(post)
'''

'''
#Caso de uso 2 (4 linhas): Exibir todos os meus posts desde sempre
u = User("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
posts=u.getMyPosts(limit=-1)
for post in posts:
    print(post)
'''

'''
#Caso de uso 3 (5 linhas): Pegar os ultimos 100 posts de um grupo e imprimir os que não tiverem textos ou vídeos (O grupo é o A.P.D.A. Associação de Programadores Depressivos Anônimos)
u = User("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
posts=Group.getGroupFromUsername("osadpa").getPosts(limit=100)
for post in posts:
    if post.object_id=="":
        print(post)
'''

'''
#Caso de uso 4: Imprimir meu Nome, e-mail e religião
u = User("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
print("Nome:"+u.name+"; Email:"+u.email+"; Religião:"+u.religion)
'''


#TWITTER===============================================================================================





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
POST friendships/update
                                            GET friendships/show
GET friends/list
GET followers/list
GET friendships/lookup
GET account/settings
GET account/verify_credentials
POST account/settings
POST account/update_profile
POST account/update_profile_image
GET blocks/list
GET blocks/ids
POST blocks/create
POST blocks/destroy
                                                GET users/lookup
                                                GET users/show
                                                GET users/search
POST account/remove_profile_banner
POST account/update_profile_banner
GET users/profile_banner
POST mutes/users/create
POST mutes/users/destroy
GET mutes/users/ids
GET mutes/users/list
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
POST lists/members/create_all
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
