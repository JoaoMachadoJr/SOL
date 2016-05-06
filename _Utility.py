__author__ = 'Joao'
from datetime import *
import random
import string
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def date(datestr="", format="%d/%m/%Y"):
    if not datestr:
        return datetime.today().date()
    d=datetime.strptime(datestr, format).date()
    return datetime.combine(d, datetime.min.time())

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def prepareRequest(maxRetries=100):
    s = requests.Session()
    retries = Retry(total=maxRetries)
    s.mount('https://', HTTPAdapter(max_retries=retries))
    return s
