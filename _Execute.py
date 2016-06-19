__author__ = 'Joao'
#from SolFB import *
#User_Facebook= User
import sys
sys.path.append("lib")

import _User
import _Access
import _Actions
import _Tweet

Actions = _Actions.Actions

Consumer_Key = "aqJhPEV5nKmki92nM8kDKeJdR"
Consumer_Secret= "WQ3aYy6brirvCkYWRtkmf6iyZSUjvzyLxc9Xu9MGFx1MxjYpNw"
Access_Token_Secret="6D1XaR1ZMj2spCGogmD1vHG12RxMk1tvmzs0kkZhlmmsK"
Access_Token="179494740-x4OS9UjoxYDOYElxh8izYMnca5V0ilq3yJpVZ3lR"

print("oi")
x=1
y=x
del(x)
print(y)

pass
#api = tweepy.API()
#ID Smurf= 741008881145548800


#acesso = _Access.StrongAccess(Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret)
acesso = _Access.StrongAccess(Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret)

Joao = Actions.me()
Joao2 = _Actions.Actions.getUser(741008881145548800)
#mentions = Joao.getMentionsTimeline(count=2, since_id=None, max_id=None)
#id=mentions[0].user.id
#mentions = _User.User(id=741008881145548800).getTimeline()
tweetSerra = _Tweet.Tweet(id=742841643259334660)
tweetPunch = _Tweet.Tweet(id=143763933654827008)
mentions =_Actions.Actions.getFriendshipInfo(source_id=Joao.id,target_id=Joao2.id);
for m in mentions:
    print(m)
print(len(mentions))
#print(tweetSerra.getRetweeters())


'''
url="https://api.twitter.com/1.1/users/show.json?screen_name=joaoxmachado"
usuario="joaoxmachado"
params={"CONSUMER_KEY":"aqJhPEV5nKmki92nM8kDKeJdR"}
r = requests.get(url=url, auth=("juninho_machado_s@hotmail.com","Jj246810"))
print(r)
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
