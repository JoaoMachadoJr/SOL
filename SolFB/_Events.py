__author__ = 'Joao'


import requests
import SolFB._Post_Facebook as _Post_Facebook
from  SolFB._Utility import Utility as _Utility
from  SolFB import _Actions
import SolFB._Cover_Photo as _Cover_Photo
import SolFB._Group as _Group
import SolFB._Live_Videos as _Live_Videos

import SolFB._Video as _Video
import SolFB._User as _User
import SolFB._Comment as _Comment
from dateutil.parser import parse
class Events:
     def __init__(self,id="", dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event
         '''
         self.id=id
         self.can_guests_invite=""
         self.cover=""
         self.description=""
         self.end_time=""
         self.guest_list_enabled=""
         self.is_page_owned=""
         self.is_viewer_admin=""
         self.name=""
         self.owner=""
         self.parent_group=""
         self.start_time=""
         self.ticket_uri=""
         self.timezone=""
         self.updated_time=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("can_guests_invite" in dictionary):
             self.can_guests_invite=dictionary["can_guests_invite"]
         if ("cover" in dictionary):
             self.cover=_Cover_Photo.Cover_Photo(dictionary=dictionary["cover"])
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("end_time" in dictionary):
             self.end_time=dictionary["end_time"]
         if ("guest_list_enabled" in dictionary):
             self.guest_list_enabled=dictionary["guest_list_enabled"]
         if ("is_page_owned" in dictionary):
             self.is_page_owned=dictionary["is_page_owned"]
         if ("is_viewer_admin" in dictionary):
             self.is_viewer_admin=dictionary["is_viewer_admin"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("owner" in dictionary):
             self.owner=dictionary["owner"]
         if ("parent_group" in dictionary):
             self.parent_group=_Group.Group(dictionary=dictionary["parent_group"])
         if ("start_time" in dictionary):
             self.start_time=dictionary["start_time"]
         if ("ticket_uri" in dictionary):
             self.ticket_uri=dictionary["ticket_uri"]
         if ("timezone" in dictionary):
             self.timezone=dictionary["timezone"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("rsvp_status" in dictionary):
             self.rsvp_status=dictionary["rsvp_status"]

     def __str__(self):
        # print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "EVENT: "+str(dict)


     def getAdmins(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/admins/
         '''
         if (token==None):
            token=_Actions.Actions.token
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

     def getAttending(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         User: https://developers.facebook.com/docs/graph-api/reference/event/attending/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Attending?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getDeclined(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/declined/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/declined?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getInterested(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/interested/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/interested?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getLive_Videos(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/live_videos/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/live_videos?fields=id,broadcast_start_time,creation_time,description,from,is_reference_only,live_views,permalink_url,seconds_left,status,title,total_views,video&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Live_Videos.Live_Videos(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getMaybe(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/maybe/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/maybe?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getNoReply(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/noreply/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/noreply?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getRoles(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/roles/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/noles?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getPicture(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/picture/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Picture?fields=height,is_silhouette,url,width&redirect=0&type=large&access_token="+token, timeout=timeout).json()
         return r["data"]["url"]

     def getComments(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/comments/
         '''
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

     def getPhotos(self, token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/photos/
         '''
         import SolFB._Photo as _Photo
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

     def getVideos(self, token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/videos/
         '''
         if (token==None):
             token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Videos?fields=backdated_time,backdated_time_granularity,id,created_time,description,embed_html,format,from,icon,is_instagram_eligible,length,permalink_url,picture,place,privacy,source,status,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Video.Video(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista


     def postVideo(self,message=" ", token=None, Localpath=None, FileURL=None):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/videos/
         '''
         if (token==None):
             token=_Actions.Actions.token
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

     def postPhoto(self, token=None, Localpath=None, FileURL=None,message=" "):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/photos/
         '''
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

     def postPost (self,message=" ", token=None):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/feed
         '''
         if (token==None):
             token=_Actions.Actions.token
         params={"message":message}
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?&access_token="+str(token)
         s=requests.post(url,params=params).json()
         return s

     def getPosts(self, token=None, dateMin="", dateMax="", limit=100, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/event/feed
         '''
         if (token==None):
             token=_Actions.Actions.token

         params={}
         if (token == None):
            token = _Actions.Actions.token
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
