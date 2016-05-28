__author__ = 'Joao'
class Thread:
     def __init__(self, id="",dictionary=dict()):
         self.id=""
         self.comments=list()
         self.to=""
         self.unread=""
         self.unseen=""
         self.updated_time=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("comments" in dictionary):
             self.comments=dictionary["comments"]
         if ("to" in dictionary):
             self.to=dictionary["to"]
         if ("unread" in dictionary):
             self.unread=dictionary["unread"]
         if ("unseen" in dictionary):
             self.unseen=dictionary["unseen"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "THREAD: "+str(dict)
