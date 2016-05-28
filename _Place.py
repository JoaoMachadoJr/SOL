__author__ = 'Joao'
class Place:
     def __init__(self, dictionary=dict()):
         self.attributes=""
         self.bounding_box=""
         self.country=""
         self.country_code=""
         self.full_name=""
         self.id=""
         self.name=""
         self.place_type=""
         self.url=""
         if ("attributes" in dictionary):
             self.attributes=dictionary["attributes"]
         if ("bounding_box" in dictionary):
             self.bounding_box=dictionary["bounding_box"]
         if ("country" in dictionary):
             self.country=dictionary["country"]
         if ("country_code" in dictionary):
             self.country_code=dictionary["country_code"]
         if ("full_name" in dictionary):
             self.full_name=dictionary["full_name"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("place_type" in dictionary):
             self.place_type=dictionary["place_type"]
         if ("url" in dictionary):
             self.url=dictionary["url"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "PLACE: "+str(dic)