__author__ = 'Joao'
import _Sizes
import _Utils

class Media:
     def __init__(self, id="",dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.display_url=""
         self.expanded_url=""
         self.id=id
         self.id_str=""
         self.indices=""
         self.media_url=""
         self.media_url_https=""
         self.sizes=""
         self.source_status_id=""
         self.source_status_id_str=""
         self.type=""
         self.url=""
         if ("display_url" in dictionary):
             self.display_url=dictionary["display_url"]
         if ("expanded_url" in dictionary):
             self.expanded_url=dictionary["expanded_url"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("indices" in dictionary):
             self.indices=dictionary["indices"]
         if ("media_url" in dictionary):
             self.media_url=dictionary["media_url"]
         if ("media_url_https" in dictionary):
             self.media_url_https=dictionary["media_url_https"]
         if ("sizes" in dictionary):
             self.sizes=_Sizes.Sizes(dictionary=dictionary["sizes"])
         if ("source_status_id" in dictionary):
             self.source_status_id=dictionary["source_status_id"]
         if ("source_status_id_str" in dictionary):
             self.source_status_id_str=dictionary["source_status_id_str"]
         if ("type" in dictionary):
             self.type=dictionary["type"]
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
         return "MEDIA: "+str(dic)