__author__ = 'Joao'
from SolTw import _Utils as _Utils


class Hashtags:
     def __init__(self, dictionary=dict()):
         dictionary= _Utils.CastToDictionary(dictionary)
         dictionary= _Utils.removeEmptyFields(dictionary)
         self.indices=""
         self.text=""
         if ("indices" in dictionary):
             self.indices=dictionary["indices"]
         if ("text" in dictionary):
             self.text=dictionary["text"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "HASHTAGS: "+str(dic)

     def __repr__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "HASHTAGS: "+str(dic)