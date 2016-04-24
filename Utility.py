__author__ = 'Joao'
from datetime import *
import random
import string

def date(datestr="", format="%d/%m/%Y"):
    if not datestr:
        return datetime.today().date()
    d=datetime.strptime(datestr, format).date()
    return datetime.combine(d, datetime.min.time())

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))