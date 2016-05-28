__author__ = 'Joao'
class Hashtags:
     def __init__(self, dictionary=dict()):
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