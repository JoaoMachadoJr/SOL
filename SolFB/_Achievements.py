__author__ = 'Joao'


import SolFB._User as _User
import SolFB._Place as _Place
from  SolFB._Settings import Settings as _Settings
from  SolFB._Utility import Utility as _Utility
import SolFB._Comment as _Comment
import requests


class Achievements:
    def __init__(self, id="",dictionary=dict()):
        self.id=id
        self.application=""
        self.data=""
        self.end_time=""
        self.from_=""
        self.image=""
        self.is_explicitly_shared=""
        self.message=""
        self.message_tags=""
        self.no_feed_story=""
        self.photos=""
        self.place=""
        self.from_=""
        self.publish_time=""
        self.ref=""
        self.start_time=""
        self.tags=""
        self.type=""
        if ("id" in dictionary):
            self.id=dictionary["id"]
        if ("application" in dictionary):
            self.application=dictionary["application"]
        if ("data" in dictionary):
            self.data="data"
        if ("end_time" in dictionary):
            self.end_time=dictionary["end_time"]
        if ("from" in dictionary):
            self.from_=_User.User(dictionary=dictionary["from"])
        if ("image" in dictionary):
            self.image=dictionary["image"]
        if ("is_explicitly_shared" in dictionary):
            self.is_explicitly_shared=dictionary["is_explicitly_shared"]
        if ("message" in dictionary):
            self.message=dictionary["message"]
        if ("message_tags" in dictionary):
            self.message_tags=dictionary["message_tags"]
        if ("no_feed_story" in dictionary):
            self.no_feed_story=dictionary["no_feed_story"]
        if ("photos" in dictionary):
            self.photos=dictionary["photos"]
        if ("place" in dictionary):
            self.place=_Place.Place(dictionary=dictionary["place"])
        if ("publish_time" in dictionary):
            self.publish_time=dictionary["publish_time"]
        if ("ref" in dictionary):
            self.ref=dictionary["ref"]
        if ("from" in dictionary):
            self.from_=_User.User(dictionary=dictionary["from"])
        if ("start_time" in dictionary):
            self.start_time=dictionary["start_time"]
        if ("tags" in dictionary):
            self.tags=dictionary["tags"]
        if ("type" in dictionary):
            self.type=dictionary["type"]

    def __str__(self):
        # print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ARCHIEVEMENT: "+str(dict)

    def getComments(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token

         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_hide,can_like,can_reply_privately,comment_count,created_time,from,like_count,message,message_tags,object,parent,private_reply_conversation,user_likes,message,is_hidden&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Comment.Comment(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista


    def postComment(self, message, token=None, Localpath=None,FileURL=None,timeout=(5,5), maxRetries=50):
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

