__author__ = 'Joao'


import SolFB._Photo as _Photo
import SolFB._Events as _Events
import SolFB._User as _User
from  SolFB import _Actions
from  SolFB._Utility import Utility as _Utility
import requests
import SolFB._Comment as _Comment

class Albums:
     def __init__(self,id="", dictionary=dict()):
         self.id=""
         self.can_upload=""
         self.count=""
         self.cover_photo=""
         self.created_time=""
         self.description=""
         self.event=""
         self.from_=""
         self.link=""
         self.location=""
         self.name=""
         self.place=""
         self.privacy=""
         self.type=""
         self.updated_time=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("can_upload" in dictionary):
             self.can_upload=dictionary["can_upload"]
         if ("count" in dictionary):
             self.count=dictionary["count"]
         if ("cover_photo" in dictionary):
             self.cover_photo=_Photo.Photo(dictionary=dictionary["cover_photo"])
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("event" in dictionary):
             self.event=_Events.Events(dictionary=dictionary["event"])
         if ("from" in dictionary):
             self.from_=_User.User(dictionary= dictionary["from"])
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("location" in dictionary):
             self.location=dictionary["location"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
         if ("type" in dictionary):
             self.type=dictionary["type"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ALBUMS: "+str(dict)

     def getPhotos(self, token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
             token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Photos?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Photo.Photo(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def postPhoto(self, token=None, Localpath=None, FileURL=None,message=" "):
         if (token==None):
             token=_Actions.Actions.token
         if (Localpath==None and FileURL==None):
             raise Exception("You should use a LocalPath or a URL")
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
             files={'file':open(Localpath,'rb')}
             params={"description":message}
             s=requests.post(graphurl, files=files,params=params).json()
             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
             params={"description":message}
             params["file_url"]=FileURL
             return requests.post(graphurl,params=params).json()

     def getLikes(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
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
            token=_Actions.Actions.token

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

     def postLike(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         return str(r)

     def postComment(self, message, token=None, Localpath=None, FileURL=None):
         if (token==None):
            token=_Actions.Actions.token
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

     def getLikesCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=likes.summary(true)&access_token="+token, timeout=timeout).json()
         return r["likes"]["summary"]["total_count"]

     def getCommentCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=comments.summary(true)&access_token="+token, timeout=timeout).json()
         return r["comments"]["summary"]["total_count"]
