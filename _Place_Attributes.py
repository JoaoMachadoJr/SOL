__author__ = 'Joao'
import _Utils


class Place_Attributes:
     def __init__(self, dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.street_address=""
         self.locality=""
         self.region=""
         self.iso3=""
         self.postal_code=""
         self.phone=""
         self.twitter=""
         self.url=""
         self.app_id=""
         if ("street_address" in dictionary):
             self.street_address=dictionary["street_address"]
         if ("locality" in dictionary):
             self.locality=dictionary["locality"]
         if ("region" in dictionary):
             self.region=dictionary["region"]
         if ("iso3" in dictionary):
             self.iso3=dictionary["iso3"]
         if ("postal_code" in dictionary):
             self.postal_code=dictionary["postal_code"]
         if ("phone" in dictionary):
             self.phone=dictionary["phone"]
         if ("twitter" in dictionary):
             self.twitter=dictionary["twitter"]
         if ("url" in dictionary):
             self.url=dictionary["url"]
         if ("app:id" in dictionary):
             self.app_id=dictionary["app:id"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "PLACE_ATTRIBUTES: "+str(dic)