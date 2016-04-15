__author__ = 'Joao'
from datetime import *

def date(datestr="", format="%d/%m/%Y"):
    if not datestr:
        return datetime.today().date()
    d=datetime.strptime(datestr, format).date()
    return datetime.combine(d, datetime.min.time())