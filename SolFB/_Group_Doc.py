__author__ = 'Joao'

import SolFB._User as _User


class Group_Doc:
     def __init__(self, id="",dictionary=dict()):
         self.id=id
         self.from_=""
         self.subject=""
         self.message=""
         self.icon=""
         self.created_time=""
         self.updated_time=""
         self.revision=""
         self.can_edit=""
         self.can_delete=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("from" in dictionary):
             self.from_=_User.User(dictionary=dictionary["from"])
         if ("subject" in dictionary):
             self.subject=dictionary["subject"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("revision" in dictionary):
             self.revision=dictionary["revision"]
         if ("can_edit" in dictionary):
             self.can_edit=dictionary["can_edit"]
         if ("can_delete" in dictionary):
             self.can_delete=dictionary["can_delete"]


     def __str__(self):
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "GROUP_DOC: "+str(dict)
     def getGroup_Doc(self, token=None,timeout=(5,5), maxRetries=50):
         import SolFB._Utility as _Utility
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/Group_Doc?&access_token="+str(token), timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Group_Doc(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista
