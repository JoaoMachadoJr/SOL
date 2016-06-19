__author__ = 'Joao'
class Page_Label:
     def __init__(self,id="", dictionary=dict()):
         self.creation_time=""
         self.creator_id=""
         self.from_=""
         self.id=id
         self.name=""
         if ("creation_time" in dictionary):
             self.creation_time=dictionary["creation_time"]
         if ("creator_id" in dictionary):
             self.creator_id=dictionary["creator_id"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("name" in dictionary):
             self.name=dictionary["name"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "PAGE LABEL: "+str(dict)
