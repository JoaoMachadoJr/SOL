__author__ = 'Joao'


def removeEmptyFields (dictionary):
     dic=dictionary
     dict={}

     for key in dic:
         if not(dic[key]==None or dic[key]==""):
             dict[key]=dic[key]
     return dict

def CastToDictionary (object):
    if isinstance(object, dict):
        return object
    else:
        return object.__dict__