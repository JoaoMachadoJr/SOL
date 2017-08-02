__author__ = 'Joao'
from SolTw import _Utils as _Utils


class Bounding_box:
     def __init__(self, dictionary=dict()):
         dictionary= _Utils.CastToDictionary(dictionary)
         dictionary= _Utils.removeEmptyFields(dictionary)
         self.coordinates=""
         self.type=""
         if ("coordinates" in dictionary):
             self.coordinates=dictionary["coordinates"]
         if ("type" in dictionary):
             self.type=dictionary["type"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "BOUNDING_BOX: "+str(dic)

     def __repr__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "BOUNDING_BOX: "+str(dic)