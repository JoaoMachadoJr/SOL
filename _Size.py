__author__ = 'Joao'
import _Utils


class Size:
     def __init__(self, dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.h=""
         self.resize=""
         self.w=""
         if ("h" in dictionary):
             self.h=dictionary["h"]
         if ("resize" in dictionary):
             self.resize=dictionary["resize"]
         if ("w" in dictionary):
             self.w=dictionary["w"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "SIZE: "+str(dic)