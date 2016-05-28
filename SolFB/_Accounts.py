__author__ = 'Joao'
class Accounts:
    def __init__(self, id="",dictionary=""):
        self.name=""
        self.perms=list()
        self.id=id
        self.access_token=""
        self.category=""
        if (dictionary!=""):
            self.id=dictionary["id"]
            self.perms=dictionary["perms"]
            self.name=dictionary["name"]
            self.access_token=dictionary["access_token"]
            self.category=dictionary["category"]

    def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ACCOUNTS: "+str(dict)