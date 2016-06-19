__author__ = 'Joao'
class Adaccountgroups:
     def __init__(self, id="",dictionary=dict()):
         self.id=id
         self.account_group_id=""
         self.accounts=""
         self.name=""
         self.status=""
         self.users=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("account_group_id" in dictionary):
             self.account_group_id=dictionary["account_group_id"]
         if ("accounts" in dictionary):
             self.accounts=dictionary["accounts"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("users" in dictionary):
             self.users=dictionary["users"]


     def __str__(self):
        # print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ADACCOUNTGROUP: "+str(dict)