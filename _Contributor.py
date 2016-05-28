__author__ = 'Joao'
class Contributor:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.id_str=""
         self.screen_name=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
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
         return "CONTRIBUTOR: "+str(dic)