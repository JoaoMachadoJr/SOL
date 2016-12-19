__author__ = 'Joao'
import requests
from dateutil.parser import parse

from SolFB import _User, _Utility, _Actions
from  SolFB._Utility import Utility as _Utility
from  SolFB import _Actions
import requests
import SolFB._Place as _Place
import SolFB._Privacy as _Privacy
import SolFB._Targeting as _Targeting
import SolFB._Feed_Targeting as _Feed_Targeting
import SolFB._Story_Attachment as _Story_Attachment
import SolFB._Comment as _Comment
import SolFB._Properties as _Properties


class Post_Facebook: #Classe para os POSTs das redes sociais
    def __init__(self, id="", created_time="", message="", story="", dictionary=dict()):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/post
        '''
        self.id=id
        self.admin_creator=list()
        self.created_time = created_time
        self.message=message
        self.story = story
        self.caption=""
        self.description=""
        self.feed_targeting=""
        self.created_by=""
        self.icon=""
        self.is_hidden=""
        self.is_published=""
        self.link=""
        self.from_=""
        self.message_tags=list()
        self.name=""
        self.object_id=""
        self.parent_id=""
        self.picture=""
        self.place=_Place.Place()
        self.privacy = _Privacy.Privacy()
        self.properties=list()
        self.shares=0
        self.source=""
        self.status_type="" #enum{mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, approved_friend}
        self.targeting=_Targeting.Targeting()
        self.to=list()
        self.type="" #enum{link, status, photo, video, offer}
        self.updated_time=""
        self.with_tags=list()
        if ("id" in dictionary):
             self.id=dictionary["id"]
        if ("admin_creator" in dictionary):
             for i in dictionary["admin_creator"]:
                self.admin_creator.append(_User.User(dictionary=i))
        if ("application" in dictionary):
             self.application=dictionary["application"]
        if ("call_to_action" in dictionary):
             self.call_to_action=dictionary["call_to_action"]
        if ("caption" in dictionary):
             self.caption=dictionary["caption"]
        if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
        if ("description" in dictionary):
             self.description=dictionary["description"]
        if ("feed_targeting" in dictionary):
             self.feed_targeting=_Feed_Targeting.Feed_Targeting(dictionary=dictionary["feed_targeting"])
        if ("from" in dictionary):
             self.from_= _User.User(dictionary=dictionary["from"])
        if ("icon" in dictionary):
             self.icon=dictionary["icon"]
        if ("is_hidden" in dictionary):
             self.is_hidden=dictionary["is_hidden"]
        if ("is_published" in dictionary):
             self.is_published=dictionary["is_published"]
        if ("link" in dictionary):
             self.link=dictionary["link"]
        if ("message" in dictionary):
             self.message=dictionary["message"]
        if ("message_tags" in dictionary):
             self.message_tags=dictionary["message_tags"]
        if ("name" in dictionary):
             self.name=dictionary["name"]
        if ("object_id" in dictionary):
             self.object_id=dictionary["object_id"]
        if ("parent_id" in dictionary):
             self.parent_id=dictionary["parent_id"]
        if ("picture" in dictionary):
             self.picture=dictionary["picture"]
        if ("place" in dictionary):
             self.place=dictionary["place"]
        if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
        if ("properties" in dictionary):
             for i in dictionary["properties"]:
                self.properties.append(_Properties.Properties(dictionary=i))
        if ("shares" in dictionary):
             self.shares=dictionary["shares"]
        if ("source" in dictionary):
             self.source=dictionary["source"]
        if ("status_type" in dictionary):
             self.status_type=dictionary["status_type"]
        if ("story" in dictionary):
             self.story=dictionary["story"]
        if ("story_tags" in dictionary):
             self.story_tags=dictionary["story_tags"]
        if ("targeting" in dictionary):
             self.targeting=dictionary["targeting"]
        if ("to" in dictionary):
             for i in dictionary["to"]:
                self.to.append(_User.User(dictionary=i))
        if ("type" in dictionary):
             self.type=dictionary["type"]
        if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
        if ("with_tags" in dictionary):
             self.with_tags=dictionary["with_tags"]

    def __str__(self):
        dic=self.__dict__
        lista=list()
        for key in dic:
         lista.append(key)
        for key in lista:
         if dic[key]==None or dic[key]=="":
             del dic[key]
        return "POST: "+str(dic)




    def getLikes(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Referece: https://developers.facebook.com/docs/graph-api/reference/v2.8/object/likes
         '''
         if (token==None):
            token= _Actions.Actions.token
         #print("token="+str(token))
         r= _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r= _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def getLikesCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token= _Actions.Actions.token
         r= _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=likes.summary(true)&access_token="+token, timeout=timeout).json()
         return r["likes"]["summary"]["total_count"]

    def getCommentCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token= _Actions.Actions.token
         r= _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=comments.summary(true)&access_token="+token, timeout=timeout).json()
         return r["comments"]["summary"]["total_count"]

    def postLike(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/object/likes
         '''
         if (token==None):
            token= _Actions.Actions.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         return str(r)

    def getReactions(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/post/reactions
         '''
         if (token==None):
            token= _Actions.Actions.token
         #print("token="+str(token))
         r= _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/reactions?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r= _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def getAttachments(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/attachment
         '''
         if (token==None):
            token= _Actions.Actions.token
         #print("token="+str(token))
         r= _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Attachments?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Story_Attachment.Story_Attachment(a))
             if ("paging" in r and "next" in r["paging"]):
                 r= _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def getComments(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/object/comments
         '''
         if (token==None):
            token= _Actions.Actions.token

         r= _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Comment.Comment(dictionary=a))
             if ("next" in r["paging"]):
                 r= _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def postComment(self, message, token=None, Localpath=None, FileURL=None):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/object/comments
         '''
         if (token==None):
            token= _Actions.Actions.token
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


