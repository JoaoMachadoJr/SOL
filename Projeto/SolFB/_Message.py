__author__ = 'Joao'
class Message:
     def __init__(self, id="",dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/message/
         '''
         self.created_time=""
         self.from_=""
         self.id=id
         self.message=""
         self.subject=""
         self.tags=""
         self.to=""
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("subject" in dictionary):
             self.subject=dictionary["subject"]
         if ("tags" in dictionary):
             self.tags=dictionary["tags"]
         if ("to" in dictionary):
             self.to=dictionary["to"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "MESSAGE: "+str(dict)
