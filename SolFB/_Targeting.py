__author__ = 'Joao'
class Targeting:
    def __init__(self, dictionary=dict()):
        self.countries=list()
        self.locales=list()
        self.regions=""
        self.cities=list()
        self.description=""
        self.properties=""
        if "countries" in dictionary:
            self.countries=dictionary["countries"]
        if "locales" in dictionary:
            self.locales=dictionary["locales"]
        if "regions" in dictionary:
            self.value=dictionary["value"]
        if "cities" in dictionary:
            self.friends=dictionary["friends"]


    def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "TARGETING: "+str(dict)