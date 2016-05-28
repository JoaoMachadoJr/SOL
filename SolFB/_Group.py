__author__ = 'Joao'


import requests
from  SolFB._Settings import Settings as _Settings
from  SolFB._Utility import Utility as _Utility
import SolFB._Cover_Photo as _Cover_Photo
import SolFB._User as _User
import SolFB._Group_Doc as _Group_Doc


import SolFB._Post_Facebook as _Post_Facebook
from dateutil.parser import parse

import SolFB._Video as _Video

class Group:
     def __init__(self,id="", dictionary=dict()):
         self.id=id
         self.cover=""
         self.description=""
         self.email=""
         self.icon=""
         self.link=""
         self.member_request_count=""
         self.name=""
         self.owner=""
         self.parent=""
         self.privacy=""
         self.updated_time=""
         self.cover_url=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("cover" in dictionary):
             self.cover=_Cover_Photo.Cover_Photo(dictionary=dictionary["cover"])
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("email" in dictionary):
             self.email=dictionary["email"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("member_request_count" in dictionary):
             self.member_request_count=dictionary["member_request_count"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("owner" in dictionary):
             self.owner=dictionary["owner"]
         if ("parent" in dictionary):
             self.parent=dictionary["parent"]
         if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("cover_url" in dictionary):
             self.cover_url=dictionary["cover_url"]
         if ("administrator" in dictionary):
             self.administrator=dictionary["administrator"]
         if ("unread" in dictionary):
             self.unread=dictionary["unread"]


     def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "GROUP: "+str(dict)

     def getAdmins(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/admins?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getDocs(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/docs?fields=id,from,subject,message,icon,created_time,updated_time,revision,can_edit,can_delete&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Group_Doc.Group_Doc(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getEvents(self,token=None, timeout=(5,5), maxRetries=50):
         import SolFB._Events as _Events
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/docs?fields=id,can_guests_invite,cover,description,end_time,guest_list_enabled,is_page_owned,is_viewer_admin,name,owner,parent_group,start_time,ticket_uri,timezone,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Events.Events(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getAlbums(self,token=None, timeout=(5,5), maxRetries=50):
         import SolFB._Albums as _Albums
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/albums?fields=id,can_upload,count,cover_photo,created_time,description,event,from,link,location,name,place,privacy,type,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Albums.Albums(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getFiles(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/files?fields=id,from,group,download_link,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getPosts(self, token=None, dateMin="", dateMax="", limit=100, timeout=(5,5), maxRetries=50):
         if (token==None):
             token=_Settings.token

         params={}
         if (token == None):
            token = _Settings.token
         if (dateMin!="" and dateMax!="" and dateMin > dateMax):
            raise Exception("Cannot use dateMin > dateMax")
         if (dateMax != ""):
            params["until"]=dateMax

         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.5/"+self.id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=100&access_token="+token, timeout=timeout).json()
         lista = list()
         while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                post=_Post_Facebook.Post_Facebook(dictionary=a)
                if ((len(lista)==limit) or (dateMin!="" and parse(post.created_time).replace(tzinfo=None)<dateMin)):
                    return lista
                lista.append(post)
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
         return lista

     def postPost (self,message=" ", token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
             token=_Settings.token
         params={"message":message}
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?&access_token="+str(token)
         s=requests.post(url,params=params).json()
         return s

     def getMembers(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/members?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista



     def getPhotos(self, token=None, timeout=(5,5), maxRetries=50):
         import SolFB._Photo as _Photo
         if (token==None):
             token=_Settings.token
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
             token=_Settings.token
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

     def getVideos(self, token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
             token=_Settings.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Videos?fields=id,created_time,description,embed_html,format,from,icon,picture,privacy,source,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Video.Video(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getGroupFromUsername(username, token=None):
         if (token==None):
             token=_Settings.token
         id=username
         id2=requests.get("https://graph.facebook.com/search?q="+id+"&type=group&access_token="+token).json()
         id=id2["data"][0]["id"]

         meta=requests.get("https://graph.facebook.com/v2.3/"+id+"?metadata=1&access_token="+token).json()
         meta=meta["metadata"]["type"]
         if(meta!="group"):
             raise Exception("ERROR: This ID is not from a group")
         r=_Utility.prepareRequest().get("https://graph.facebook.com/v2.6/"+id+"?fields=id,cover,description,email,icon,link,member_request_count,name,owner,parent,privacy,updated_time&access_token="+token).json()
         return Group(dictionary=r)


     def postVideo(self,message=" ", token=None, Localpath=None, FileURL=None):
         if (token==None):
             token=_Settings.token
         if (Localpath==None and FileURL==None):
             raise Exception("You should use a LocalPath or a URL")
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):


             graphurl="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
             files={'file':open(Localpath,'rb')}
             params={"description":message}
             s=requests.post(graphurl, files=files,params=params).json()

             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
             params={"description":message}
             params["file_url"]=FileURL
             return requests.post(graphurl,params=params).json()
