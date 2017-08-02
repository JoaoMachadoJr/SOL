__author__ = 'Joao'
class Properties:
     def __init__(self, dictionary=dict()):
         self.name=""
         self.text=""
         self.href=""
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("text" in dictionary):
             self.text=dictionary["text"]
         if ("href" in dictionary):
             self.href=dictionary["href"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "PROPERTIES: "+str(dict)