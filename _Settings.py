__author__ = 'Joao'
import sys
import pip
import urllib.request
import requests
import Utility
from shutil import copyfile

#Variaveis globais


global token
token=""

def debugToken(token):
    r=requests.get("https://graph.facebook.com/v2.6/debug_token?input_token="+token+"&access_token="+token).json()
    return r

