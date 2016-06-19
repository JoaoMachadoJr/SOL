__author__ = 'Joao'


from  SolFB._Utility import Utility as _Utility
from  SolFB._Settings import Settings as _Settings
import requests


import SolFB._Events as _Events

import SolFB._Comment as _Comment
import SolFB._User as _User
class Photo:
     def __init__(self,id="", dictionary=dict()):
         import SolFB._Albums as _Albums
         self.id=id
         self.album=""
         self.backdated_time=""
         self.backdated_time_granularity=""
         self.can_delete=""
         self.can_tag=""
         self.created_time=""
         self.event=""
         self.from_=""
         self.height=""
         self.icon=""
         self.images=""
         self.link=""
         self.name=""
         self.name_tags=""
         self.page_story_id=""
         self.picture=""
         self.place=""
         self.updated_time=""
         self.width=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("album" in dictionary):
             self.album=_Albums.Albums(dictionary=dictionary["album"])
         if ("backdated_time" in dictionary):
             self.backdated_time=dictionary["backdated_time"]
         if ("backdated_time_granularity" in dictionary):
             self.backdated_time_granularity=dictionary["backdated_time_granularity"]
         if ("can_delete" in dictionary):
             self.can_delete=dictionary["can_delete"]
         if ("can_tag" in dictionary):
             self.can_tag=dictionary["can_tag"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("event" in dictionary):
             self.created_time=_Events.Events(dictionary=dictionary["event"])
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("height" in dictionary):
             self.height=dictionary["height"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("images" in dictionary):
             self.images=dictionary["images"]
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("name_tags" in dictionary):
             self.name_tags=dictionary["name_tags"]
         if ("page_story_id" in dictionary):
             self.page_story_id=dictionary["page_story_id"]
         if ("picture" in dictionary):
             self.picture=dictionary["picture"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("width" in dictionary):
             self.width=dictionary["width"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "PHOTO: "+str(dict)

     def getInfo(self, token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token, timeout=timeout).json()
         c=Photo(dictionary=r)
         return c;

     def delete(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token+"&method=delete", timeout=timeout).json()
         return str(r)

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

     def postComment(self, message, token=None, Localpath=None, FileURL=None):
         if (token==None):
            token=_Settings.token
         if (Localpath==None and FileURL==None):
             params={"message":message}
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/comments?&access_token="+token
             s=requests.post(graphurl, params=params).json()
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):

             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/comments?&access_token="+token
             files={'file':open(Localpath,'rb')}
             params={"message":message}
             s=requests.post(graphurl, files=files,params=params).json()

             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/comments?&access_token="+token
             params={"message":message}
             params["attachment_url"]=FileURL
             return requests.post(graphurl,params=params).json()

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

     def getLikesCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=likes.summary(true)&access_token="+token, timeout=timeout).json()
         return r["likes"]["summary"]["total_count"]

     def getCommentCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=comments.summary(true)&access_token="+token, timeout=timeout).json()
         return r["comments"]["summary"]["total_count"]

     def postLike(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         return str(r)

     def getReactions(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/reactions?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista
