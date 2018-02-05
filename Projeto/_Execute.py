
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

sol.post('Oh! Que saudades que tenho, Da aurora da minha vida, Da minha infância querida, Que os anos não trazem mais!','C:\\Users\\joao\\Pictures\\imagens facebook sacanear\\12644892_1051646468228987_2520408126616807931_n.jpg')
