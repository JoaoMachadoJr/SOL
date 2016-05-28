__author__ = 'Joao'
import requests

#Variaveis globais

class Settings:
    global token
    token=""

    def debugToken(token):
        r=requests.get("https://graph.facebook.com/v2.6/debug_token?input_token="+token+"&access_token="+token).json()
        return r

