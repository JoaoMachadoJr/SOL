__author__ = 'Joao'
class Friendship:
     def __init__(self, dictionary=dict()):
         self.following_requested=""
         self.id_str=""
         self.following_received=""
         self.live_following=""
         self.notifications_enabled=""
         self.blocking=""
         self.all_replies=""
         self.following=""
         self.muting=""
         self._api=""
         self.followed_by=""
         self.want_retweets=""
         self.screen_name=""
         self.blocked_by=""
         self.id=""
         self.marked_spam=""
         self.can_dm=""
         if ("following_requested" in dictionary):
             self.following_requested=dictionary["following_requested"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("following_received" in dictionary):
             self.following_received=dictionary["following_received"]
         if ("live_following" in dictionary):
             self.live_following=dictionary["live_following"]
         if ("notifications_enabled" in dictionary):
             self.notifications_enabled=dictionary["notifications_enabled"]
         if ("blocking" in dictionary):
             self.blocking=dictionary["blocking"]
         if ("all_replies" in dictionary):
             self.all_replies=dictionary["all_replies"]
         if ("following" in dictionary):
             self.following=dictionary["following"]
         if ("muting" in dictionary):
             self.muting=dictionary["muting"]
         if ("_api" in dictionary):
             self._api=dictionary["_api"]
         if ("followed_by" in dictionary):
             self.followed_by=dictionary["followed_by"]
         if ("want_retweets" in dictionary):
             self.want_retweets=dictionary["want_retweets"]
         if ("screen_name" in dictionary):
             self.screen_name=dictionary["screen_name"]
         if ("blocked_by" in dictionary):
             self.blocked_by=dictionary["blocked_by"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("marked_spam" in dictionary):
             self.marked_spam=dictionary["marked_spam"]
         if ("can_dm" in dictionary):
             self.can_dm=dictionary["can_dm"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "FRIENDSHIP: "+str(dic)


     def __repr__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "FRIENDSHIP: "+str(dic)