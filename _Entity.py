__author__ = 'Joao'
class Entity:
     def __init__(self, dictionary=dict()):
         self.hashtags=""
         self.media=""
         self.urls=""
         self.user_mentions=""
         if ("hashtags" in dictionary):
             self.hashtags=dictionary["hashtags"]
         if ("media" in dictionary):
             self.media=dictionary["media"]
         if ("urls" in dictionary):
             self.urls=dictionary["urls"]
         if ("user_mentions" in dictionary):
             self.user_mentions=dictionary["user_mentions"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ENTITY: "+str(dic)