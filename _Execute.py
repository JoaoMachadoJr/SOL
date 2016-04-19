__author__ = 'Joao'
import _User_Facebook
from Utility import *
User_Facebook=_User_Facebook.User_Facebook
import requests
from _Facebook_Classes import *

'''
#Caso de uso 1 (4 linhas): Pegar posts da Dilma de 2015 (Mesma coisa que o código do wladek fazia)
u = User_Facebook("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
posts=u.getPostsFromPage("Dilmarousseff",date("01/01/2015"),date("31/12/2015"),-1)
for post in posts:
    print(post)
'''

'''
#Caso de uso 2 (4 linhas): Exibir todos os meus posts desde sempre
u = User_Facebook("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
posts=u.getMyPosts(limit=-1)
for post in posts:
    print(post)
'''

'''
#Caso de uso 3 (5 linhas): Pegar os ultimos 100 posts de um grupo e imprimir os que não tiverem textos ou vídeos (O grupo é o A.P.D.A. Associação de Programadores Depressivos Anônimos)
u = User_Facebook("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
posts=u.getPostsFromGroup(id="osadpa", limit=100)
for post in posts:
    if post.object_id=="":
        print(post)
'''

'''
#Caso de uso 4: Imprimir meu Nome, e-mail e religião
u = User_Facebook("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
print("Nome:"+u.name+"; Email:"+u.email+"; Religião:"+u.religion)
'''

u = User_Facebook("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
r=requests.get("https://graph.facebook.com/v2.6/me/books?&access_token="+u.token).json()

lol=u.getInbox()
for l in lol:
    print(str(l))