__author__ = 'Joao'
class Privacy:
    def __init__(self, id="",dictionary=dict()):
        self.allow=""
        self.deny=""
        self.value=""
        self.friends=list()
        self.description=""
        self.properties=""
        if "allow" in dictionary:
            self.allow=dictionary["allow"]
        if "deny" in dictionary:
            self.deny=dictionary["deny"]
        if "value" in dictionary:
            self.value=dictionary["value"]
        if "friends" in dictionary:
            self.friends=dictionary["friends"]
        if "description" in dictionary:
            self.description=dictionary["description"]


    def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "PRIVACY: "+str(dict)