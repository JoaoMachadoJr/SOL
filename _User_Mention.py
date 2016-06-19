__author__ = 'Joao'
import _Utils
class User_Mention:
     def __init__(self, id="",dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.id=id
         self.id_str=""
         self.indices=""
         self.name=""
         self.screen_name=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("indices" in dictionary):
             self.indices=dictionary["indices"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("screen_name" in dictionary):
             self.screen_name=dictionary["screen_name"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "USER_MENTION: "+str(dic)