__author__ = 'Joao'
class Cover_Photo:
     def __init__(self, id="",dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/cover-photo/
         '''
         self.id=id
         self.cover_id=""
         self.offset_x=""
         self.offset_y=""
         self.source=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("cover_id" in dictionary):
             self.cover_id=dictionary["cover_id"]
         if ("offset_x" in dictionary):
             self.offset_x=dictionary["offset_x"]
         if ("offset_y" in dictionary):
             self.offset_y=dictionary["offset_y"]
         if ("source" in dictionary):
             self.source=dictionary["source"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "COVER_PHOTO: "+str(dict)
