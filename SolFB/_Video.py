__author__ = 'Joao'
class Video:
     def __init__(self, id="",dictionary=dict()):
         self.backdated_time=""
         self.backdated_time_granularity=""
         self.id=id
         self.created_time=""
         self.description=""
         self.embed_html=""
         self.format=""
         self.from_=""
         self.icon=""
         self.is_instagram_eligible=""
         self.length=""
         self.permalink_url=""
         self.picture=""
         self.place=""
         self.privacy=""
         self.source=""
         self.status=""
         self.updated_time=""
         if ("backdated_time" in dictionary):
             self.backdated_time=dictionary["backdated_time"]
         if ("backdated_time_granularity" in dictionary):
             self.backdated_time_granularity=dictionary["backdated_time_granularity"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("embed_html" in dictionary):
             self.embed_html=dictionary["embed_html"]
         if ("format" in dictionary):
             self.format=dictionary["format"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("is_instagram_eligible" in dictionary):
             self.is_instagram_eligible=dictionary["is_instagram_eligible"]
         if ("length" in dictionary):
             self.length=dictionary["length"]
         if ("permalink_url" in dictionary):
             self.permalink_url=dictionary["permalink_url"]
         if ("picture" in dictionary):
             self.picture=dictionary["picture"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
         if ("source" in dictionary):
             self.source=dictionary["source"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "VIDEO: "+str(dict)
