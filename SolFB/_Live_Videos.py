__author__ = 'Joao'


from  SolFB._Settings import Settings as _Settings
from  SolFB._Utility import Utility as _Utility
import SolFB._Comment as _Comment
import SolFB._User as _User
import SolFB._Video as _Video
class Live_Videos:
     def __init__(self, id="",dictionary=dict()):
         self.id=id
         self.broadcast_start_time=""
         self.creation_time=""
         self.description=""
         self.from_=""
         self.is_reference_only=""
         self.live_views=""
         self.permalink_url=""
         self.seconds_left=""
         self.status=""
         self.title=""
         self.total_views=""
         self.video=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("broadcast_start_time" in dictionary):
             self.broadcast_start_time=dictionary["broadcast_start_time"]
         if ("creation_time" in dictionary):
             self.creation_time=dictionary["creation_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("is_reference_only" in dictionary):
             self.is_reference_only=dictionary["is_reference_only"]
         if ("live_views" in dictionary):
             self.live_views=dictionary["live_views"]
         if ("permalink_url" in dictionary):
             self.permalink_url=dictionary["permalink_url"]
         if ("seconds_left" in dictionary):
             self.seconds_left=dictionary["seconds_left"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("title" in dictionary):
             self.title=dictionary["title"]
         if ("total_views" in dictionary):
             self.total_views=dictionary["total_views"]
         if ("video" in dictionary):
             self.video=_Video.Video(dictionary=dictionary["video"])


     def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "LIVE_VIDEO: "+str(dict)

     def getLikes(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista
     def getComments(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token

         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Comment.Comment(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista
