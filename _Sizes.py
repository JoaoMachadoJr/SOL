__author__ = 'Joao'
import _Size
import _Utils
class Sizes:
     def __init__(self, dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.thumb=""
         self.large=""
         self.medium=""
         self.small=""
         if ("thumb" in dictionary):
             self.thumb=_Size.Size(dictionary=dictionary["thumb"])
         if ("large" in dictionary):
             self.large=_Size.Size(dictionary=dictionary["large"])
         if ("medium" in dictionary):
             self.medium=_Size.Size(dictionary=dictionary["medium"])
         if ("small" in dictionary):
             self.small=_Size.Size(dictionary=dictionary["small"])


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "SIZES: "+str(dic)