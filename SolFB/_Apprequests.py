__author__ = 'Joao'


import SolFB._User as _User

class Apprequests:
     def __init__(self, id="",dictionary=dict()):
         self.id=id
         self.action_type=""
         self.application=""
         self.created_time=""
         self.data=""
         self.from_=""
         self.message=""
         self.object=""
         self.to=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("action_type" in dictionary):
             self.action_type=dictionary["action_type"]
         if ("application" in dictionary):
             self.application=dictionary["application"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("data" in dictionary):
             self.data=dictionary["data"]
         if ("from" in dictionary):
             self.from_=_User.User(dictionary=dictionary["from"])
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("object" in dictionary):
             self.object=dictionary["object"]
         if ("to" in dictionary):
             self.to=_User.User(dictionary=dictionary["to"])


     def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "APREQUESTS: "+str(dict)
