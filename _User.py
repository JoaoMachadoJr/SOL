__author__ = 'Joao'
import _Entity
import _Tweet
import _Utils
import _Access
import _Actions
import lib.tweepy as tweepy
class User:
     def __init__(self, id="", dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.contributors_enabled=""
         self.created_at=""
         self.default_profile=""
         self.default_profile_image=""
         self.description=""
         self.entities=""
         self.favourites_count=""
         self.follow_request_sent=""
         self.following=""
         self.followers_count=""
         self.friends_count=""
         self.geo_enabled=""
         self.id=id
         self.id_str=""
         self.is_translator=""
         self.lang=""
         self.listed_count=""
         self.location=""
         self.name=""
         self.notifications=""
         self.profile_background_color=""
         self.profile_background_image_url=""
         self.profile_background_image_url_https=""
         self.profile_background_tile=""
         self.profile_banner_url=""
         self.profile_image_url=""
         self.profile_image_url_https=""
         self.profile_link_color=""
         self.profile_sidebar_border_color=""
         self.profile_sidebar_fill_color=""
         self.profile_text_color=""
         self.profile_use_background_image=""
         self.protected=""
         self.screen_name=""
         self.show_all_inline_media=""
         self.status=""
         self.statuses_count=""
         self.time_zone=""
         self.url=""
         self.utc_offset=""
         self.verified=""
         self.withheld_in_countries=""
         self.withheld_scope=""
         if ("contributors_enabled" in dictionary):
             self.contributors_enabled=dictionary["contributors_enabled"]
         if ("created_at" in dictionary):
             self.created_at=dictionary["created_at"]
         if ("default_profile" in dictionary):
             self.default_profile=dictionary["default_profile"]
         if ("default_profile_image" in dictionary):
             self.default_profile_image=dictionary["default_profile_image"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("entities" in dictionary):
             self.entities= _Entity.Entity(dictionary=dictionary["entities"])
         if ("favourites_count" in dictionary):
             self.favourites_count=dictionary["favourites_count"]
         if ("follow_request_sent" in dictionary):
             self.follow_request_sent=dictionary["follow_request_sent"]
         if ("following" in dictionary):
             self.following=dictionary["following"]
         if ("followers_count" in dictionary):
             self.followers_count=dictionary["followers_count"]
         if ("friends_count" in dictionary):
             self.friends_count=dictionary["friends_count"]
         if ("geo_enabled" in dictionary):
             self.geo_enabled=dictionary["geo_enabled"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("is_translator" in dictionary):
             self.is_translator=dictionary["is_translator"]
         if ("lang" in dictionary):
             self.lang=dictionary["lang"]
         if ("listed_count" in dictionary):
             self.listed_count=dictionary["listed_count"]
         if ("location" in dictionary):
             self.location=dictionary["location"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("notifications" in dictionary):
             self.notifications=dictionary["notifications"]
         if ("profile_background_color" in dictionary):
             self.profile_background_color=dictionary["profile_background_color"]
         if ("profile_background_image_url" in dictionary):
             self.profile_background_image_url=dictionary["profile_background_image_url"]
         if ("profile_background_image_url_https" in dictionary):
             self.profile_background_image_url_https=dictionary["profile_background_image_url_https"]
         if ("profile_background_tile" in dictionary):
             self.profile_background_tile=dictionary["profile_background_tile"]
         if ("profile_banner_url" in dictionary):
             self.profile_banner_url=dictionary["profile_banner_url"]
         if ("profile_image_url" in dictionary):
             self.profile_image_url=dictionary["profile_image_url"]
         if ("profile_image_url_https" in dictionary):
             self.profile_image_url_https=dictionary["profile_image_url_https"]
         if ("profile_link_color" in dictionary):
             self.profile_link_color=dictionary["profile_link_color"]
         if ("profile_sidebar_border_color" in dictionary):
             self.profile_sidebar_border_color=dictionary["profile_sidebar_border_color"]
         if ("profile_sidebar_fill_color" in dictionary):
             self.profile_sidebar_fill_color=dictionary["profile_sidebar_fill_color"]
         if ("profile_text_color" in dictionary):
             self.profile_text_color=dictionary["profile_text_color"]
         if ("profile_use_background_image" in dictionary):
             self.profile_use_background_image=dictionary["profile_use_background_image"]
         if ("protected" in dictionary):
             self.protected=dictionary["protected"]
         if ("screen_name" in dictionary):
             self.screen_name=dictionary["screen_name"]
         if ("show_all_inline_media" in dictionary):
             self.show_all_inline_media=dictionary["show_all_inline_media"]
         if ("status" in dictionary):
             self.status=_Tweet.Tweet(dictionary=dictionary["status"])
         if ("statuses_count" in dictionary):
             self.statuses_count=dictionary["statuses_count"]
         if ("time_zone" in dictionary):
             self.time_zone=dictionary["time_zone"]
         if ("url" in dictionary):
             self.url=dictionary["url"]
         if ("utc_offset" in dictionary):
             self.utc_offset=dictionary["utc_offset"]
         if ("verified" in dictionary):
             self.verified=dictionary["verified"]
         if ("withheld_in_countries" in dictionary):
             self.withheld_in_countries=dictionary["withheld_in_countries"]
         if ("withheld_scope" in dictionary):
             self.withheld_scope=dictionary["withheld_scope"]



     def getMentionsTimeline(self, Access : _Access.StrongAccess = None, count=None, since_id=None, max_id=None):
         '''Pega as vezes que fui mencionado. Minhas Mentions
            Documentado em https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         mentions=None
         mentions = api.mentions_timeline(count=count, since_id=since_id, max_id=max_id)
         lista = list()
         for mention in mentions:
             lista.append(_Tweet.Tweet(dictionary=mention))
         return lista

     def getTimeline(self, Access : _Access.WeakAccess = None, count=None, since_id=None, max_id=None, include_rts=False):
         '''Pega a timeline de um usuario
         Documentado em https://dev.twitter.com/rest/reference/get/statuses/user_timeline
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         tweets = api.user_timeline(user_id=self.id ,count=count, since_id=since_id, max_id=max_id, include_rts=include_rts)
         for tweet in tweets:
            lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

     def getHomeTimeline(self, Access : _Access.StrongAccess = None, count=None, since_id=None, max_id=None):
         '''Pega os posts na HOME do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/statuses/home_timeline
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         tweets = api.home_timeline(user_id=self.id ,count=count, since_id=since_id, max_id=max_id)
         lista = list()
         for tweet in tweets:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

     def getRetweetsOfMe(self, Access : _Access.StrongAccess = None, count=None, since_id=None, max_id=None):
         '''Pega os retweets de tweets escritos pelo usuario
         NAO FUNCIONA?!?
         Documentado em https://dev.twitter.com/rest/reference/get/statuses/retweets_of_me
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         tweets = api.retweets_of_me(user_id=self.id ,count=count, since_id=since_id, max_id=max_id)
         lista = list()
         for tweet in tweets:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

     def getFriends(self, Access : _Access.WeakAccess = None, cursor=None):
         '''Pega os amigos do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friends/ids
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         friends = api.friends_ids(user_id=self.id, cursor=cursor)
         lista = list()
         for f in friends:
             lista.append(User(id=f))
         return lista;

     def getFollowers(self, Access : _Access.WeakAccess = None, cursor=None, count=None):
         '''Pega os seguidores do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/followers/ids
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         users = api.followers_ids(user_id=self.id, cursor=cursor,count=count)
         lista = list()
         for u in users:
             lista.append(User(id=u))
         return lista;


     def getFriendshipIncoming(self, Access : _Access.StrongAccess = None, cursor=None):
         '''Pega requisições de amizade do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friendships/incoming
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         friends = api.friendships_incoming( cursor=cursor)
         lista = list()
         for f in friends:
             lista.append(User(id=f))
         return lista;

     def getFriendshipOutgoing(self, Access : _Access.StrongAccess = None, cursor=None):
         '''Pega requisições de amizade feita pelo usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friendships/outgoing
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         friends = api.friendships_outgoing( cursor=cursor)
         lista = list()
         for f in friends:
             lista.append(User(id=f))
         return lista;

     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "USER: "+str(dic)