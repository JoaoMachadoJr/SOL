__author__ = 'Joao'
#from SolFB import *
#User_Facebook= User
import sys
sys.path.append("lib")
#import lib.oauth2 as oauth2
import requests
import pip
#pip.main(["install","--target=c:\pasta", "tweepy"])
import lib.oauth2
import lib.httplib2
import lib.tweepy as tweepy

Consumer_Key = "aqJhPEV5nKmki92nM8kDKeJdR"
Consumer_Secret= "WQ3aYy6brirvCkYWRtkmf6iyZSUjvzyLxc9Xu9MGFx1MxjYpNw"
Access_Token_Secret="6D1XaR1ZMj2spCGogmD1vHG12RxMk1tvmzs0kkZhlmmsK"
Access_Token="179494740-x4OS9UjoxYDOYElxh8izYMnca5V0ilq3yJpVZ3lR"


auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

r = api.me()
for k in r.__dict__.keys():
    print("\""+str(k)+"\",",end=" ")


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





