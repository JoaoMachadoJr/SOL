#Esse arquivo armazena exemplos de uso da ferramenta

from SOL_FACEBOOK import Facebook
import lib.tweepy as t
from _const import *
from lib.requests import Session
from SOL_TWITTER import Twitter
from SOL_MAIN import SOL

"""
0- FAZENDO LOGIN E ADICIONANDO AS REDES SOCIAIS AO OBJETO SOL
"""
twitter=Twitter(twitter_consumer_key,twitter_consumer_secret,twitter_access_token,twitter_access_token_secret)
facebook=Facebook(facebook_token)

sol = SOL()
sol.socialnetworks.append(twitter)
sol.socialnetworks.append(facebook)
"""
1- AÇÕES COMUNS ENTRE AS REDES SOCIAIS
"""

"""
1.1- POST
"""

"""
1.1.1- POST COM APENAS TEXTO
"""
#FACEBOOK
facebook.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!')

#TWITTER
twitter.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!')

#TODAS AS REDES SOCIAIS
sol.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!')

"""
1.1.2- POST COM TEXTO E IMAGEM
"""
#FACEBOOK
facebook.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!','C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulipas.jpg')

#TWITTER
twitter.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!','C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulipas.jpg')

#TODAS AS REDES SOCIAIS
sol.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!','C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulipas.jpg')

"""
1.1.3- POST COM VÍDEO
"""
#FACEBOOK
facebook.post('','','C:\\Users\\Public\\Videos\\Sample Videos\\Vida selvagem.wmv')

"""
1.2 - READ
"""

#FACEBOOK
for a_item in facebook.read():
    print(a_item.__dict__)

#TWITTER
for a_item in twitter.read():
    print(a_item.__dict__)

#TODAS AS REDES SOCIAIS
for a_item in sol.read():
    print(a_item.__dict__)

"""

"""