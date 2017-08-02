__author__ = 'Joao'
from SolTw import _Utils as _Utils


class URL:
     def __init__(self, dictionary=dict()):
         dictionary= _Utils.CastToDictionary(dictionary)
         dictionary= _Utils.removeEmptyFields(dictionary)
         self.display_url=""
         self.expanded_url=""
         self.indices=""
         self.url=""
         if ("display_url" in dictionary):
             self.display_url=dictionary["display_url"]
         if ("expanded_url" in dictionary):
             self.expanded_url=dictionary["expanded_url"]
         if ("indices" in dictionary):
             self.indices=dictionary["indices"]
         if ("url" in dictionary):
             self.url=dictionary["url"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "URL: "+str(dic)

     def __repr__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "URL: "+str(dic)