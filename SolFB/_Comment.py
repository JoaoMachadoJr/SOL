__author__ = 'Joao'

import SolFB._Story_Attachment as _Story_Attachment

from  SolFB._Utility import Utility as _Utility
from  SolFB import _Actions
#import SolFB._User as _User

class Comment:
     def __init__(self,id="", dictionary=dict()):
         import SolFB._User as _User
         self.id=id
         self.attachment=""
         self.can_comment=""
         self.can_remove=""
         self.can_hide=""
         self.can_like=""
         self.can_reply_privately=""
         self.comment_count=""
         self.created_time=""
         self.from_=""
         self.like_count=""
         self.message=""
         self.message_tags=""
         self.object=""
         self.parent=""
         self.private_reply_conversation=""
         self.user_likes=""
         self.message=""
         self.is_hidden=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("attachment" in dictionary):
             self.attachment=_Story_Attachment.Story_Attachment(dictionary["attachment"])
         if ("can_comment" in dictionary):
             self.can_comment=dictionary["can_comment"]
         if ("can_remove" in dictionary):
             self.can_remove=dictionary["can_remove"]
         if ("can_hide" in dictionary):
             self.can_hide=dictionary["can_hide"]
         if ("can_like" in dictionary):
             self.can_like=dictionary["can_like"]
         if ("can_reply_privately" in dictionary):
             self.can_reply_privately=dictionary["can_reply_privately"]
         if ("comment_count" in dictionary):
             self.comment_count=dictionary["comment_count"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("from" in dictionary):
             self.from_=_User.User(dictionary=dictionary["from"])
         if ("like_count" in dictionary):
             self.like_count=dictionary["like_count"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("message_tags" in dictionary):
             self.message_tags=dictionary["message_tags"]
         if ("object" in dictionary):
             self.object=dictionary["object"]
         if ("parent" in dictionary):
             self.parent=dictionary["parent"]
         if ("private_reply_conversation" in dictionary):
             self.private_reply_conversation=dictionary["private_reply_conversation"]
         if ("user_likes" in dictionary):
             self.user_likes=dictionary["user_likes"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("is_hidden" in dictionary):
             self.is_hidden=dictionary["is_hidden"]


     def __str__(self):
        # print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "COMMENT: "+str(dict)

     def getInfo(self, token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token, timeout=timeout).json()
         c=Comment(dictionary=r)
         return c;

     def getLikes(self,token=None, timeout=(5,5), maxRetries=50):
         import SolFB._User as _User
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

     def postLike(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         return str(r)

     def deleteLike(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token+"&method=delete", timeout=timeout).json()
         return str(r)

     def update(self,message=None, token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         if message==None:
             message=self.message
         params={"message":message}
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token,params=params, timeout=timeout).json()
         return str(r)

     def delete(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Actions.Actions.token
         self.update(message=" ",token=token)
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token+"&method=delete", timeout=timeout).json()
         return str(r)


