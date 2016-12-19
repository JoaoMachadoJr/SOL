__author__ = 'Joao'
class Place:
    def __init__(self, id="",dictionary=dict()):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/place/
        '''
        self.name=""
        self.latitude=""
        self.longitude=""
        self.id=""
        if "name" in dictionary:
            self.name=dictionary["name"]
        if "location" in dictionary:
            self.latitude=dictionary["location"]["latitude"]
            self.longitude=dictionary["location"]["longitude"]
        if "id" in dictionary:
            self.id=dictionary["id"]
    def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "PLACE: "+str(dict)