__author__ = 'Joao'
class Sizes:
     def __init__(self, dictionary=dict()):
         self.thumb=""
         self.large=""
         self.medium=""
         self.small=""
         if ("thumb" in dictionary):
             self.thumb=dictionary["thumb"]
         if ("large" in dictionary):
             self.large=dictionary["large"]
         if ("medium" in dictionary):
             self.medium=dictionary["medium"]
         if ("small" in dictionary):
             self.small=dictionary["small"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "SIZES: "+str(dic)