__author__ = 'Joao'
import _Utils
class Coordinates:
     def __init__(self, dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
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
         return "COORDINATES: "+str(dic)
