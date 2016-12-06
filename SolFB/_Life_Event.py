__author__ = 'Joao'



from  SolFB import _Actions
from  SolFB._Utility import Utility as _Utility
import SolFB._Photo as _Photo
import SolFB._Comment as _Comment
import SolFB._User as _User

class Life_Event:
     def __init__(self, id="",dictionary=dict()):
         import SolFB._Page as _Page
         self.created_time=""
         self.description=""
         self.end_time=""
         self.from_=""
         self.id=id
         self.is_hidden=""
         self.start_time=""
         self.title=""
         self.updated_time=""
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("end_time" in dictionary):
             self.end_time=dictionary["end_time"]
         if ("from" in dictionary):
             self.from_=_Page.Page(dictionary=dictionary["from"])
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("is_hidden" in dictionary):
             self.is_hidden=dictionary["is_hidden"]
         if ("start_time" in dictionary):
             self.start_time=dictionary["start_time"]
         if ("title" in dictionary):
             self.title=dictionary["title"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
        # print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "LIFE_EVENT: "+str(dict)

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
