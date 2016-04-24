__author__ = 'Joao'
import _User_Facebook
from Utility import *
User_Facebook=_User_Facebook.User_Facebook
import requests
from _Facebook_Classes import *
import _Post_Facebook
import _Settings
from PIL import Image
import sys
sys.path.append("lib")



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
pagetoken="CAACxxfv6ORIBAEUcPcyie4PTIMNP62kQ5ZBJ8ACkffNJlomXb8GBRr3CYlpQyxUy430ZAXk97Yc2wUrozIzbqjZAPwkIgwQiI3EUGQLRZBGfIKSMFSSupEe1ZBpQsI5s13xBsdZCU2jDtpvbzKrwrGElnKfvqCr5X3HK8nVW59dE1dw62Ge3EpiZAr8l7MhdjwZD"
_Settings.token=u.token
caminho="C:\\A.jpg"
caminho2="C:\\bbb.mp4"
#DilmaRousseff
#369570969735973
r=requests.get("https://graph.facebook.com/v2.6/369570969735973?&access_token="+u.token).json()
e=Page(dictionary=r)
#r=requests.get("https://graph.facebook.com/v2.5/"+e.id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=100&access_token="+u.token,timeout=(10,10)).json()

#e.access_token=pagetoken
lista=e.postVideo(path=caminho2,token=pagetoken)
print(lista)
for adm in lista:
    print(adm)
print(len(lista))
