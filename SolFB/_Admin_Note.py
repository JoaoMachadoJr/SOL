__author__ = 'Joao'


import SolFB._Page as _Page
import SolFB._User as _User

class Admin_Note:
     def __init__(self, id="",dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page-admin-note/
         '''
         self.body=""
         self.from_=""
         self.id=id
         self.user=""
         if ("body" in dictionary):
             self.body=dictionary["body"]
         if ("from" in dictionary):
             self.from_=_Page.Page(dictionary=dictionary["from"])
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("user" in dictionary):
             self.user=_User.User(dictionary=dictionary["user"])


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ADMIN_NOTES: "+str(dict)
