__author__ = 'Joao'
import _Entity
import _Tweet
import _Utils
import _Access
import _Actions
import _DirectMessage
import lib.tweepy as tweepy
import _Friendship
import _List
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

     def postTweet(self, msg,latitude=None,longitude=None,place_id=None,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api=tweepy.API(Access.auth)
         api.update_status(lat=latitude,long=longitude,status=msg,place_id=place_id)
         return True

     def postDirectMessage(self, receiver, msg,Access : _Access.StrongAccess = None ):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         if (isinstance(receiver,User)):
             user=receiver.id
         api.send_direct_message(user=user,text=msg)
         return True

     def getDirectMessages(self,Access : _Access.StrongAccess = None, since_id=None, max_id=None, count=None,  full_text=None):
         return _Actions.Actions.getMyMessages(Access=Access, since_id=since_id,max_id=max_id,count=count,full_text=full_text)

     def postDestroyDirectMessage(self,id,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         return _DirectMessage.DirectMessage(dictionary= api.destroy_direct_message(id=id))

     def postFriendshipCreate(self, user,follow : bool=None,Access : _Access.StrongAccess = None):
        if (Access == None):
            Access=_Actions.defaultAccess
        api = tweepy.API(Access.auth)
        return User(dictionary=api.create_friendship(id=user,follow=follow))

     def postFriendshipDestroy(self,user,Access : _Access.StrongAccess = None):
        if (Access == None):
            Access=_Actions.defaultAccess
        api = tweepy.API(Access.auth)
        return User(dictionary=api.destroy_friendship(id=user))

     def getFriends(self, Access : _Access.WeakAccess = None, cursor=None, count=None):
         '''Pega os amigos do usuario
         https://dev.twitter.com/rest/reference/get/friends/list
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         users = api.friends(id=self.id,cursor=cursor,count=count)
         lista = list()
         for u in users:
             lista.append(User(dictionary=u))
         return lista;

     def getFollowers(self, Access : _Access.WeakAccess = None, cursor=None, count=None):
         '''Pega os amigos do usuario
         dev.twitter.com/rest/reference/get/followers/list
         '''
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         users = api.followers(id=self.id,cursor=cursor,count=count)
         lista = list()
         for u in users:
             lista.append(User(dictionary=u))
         return lista;

     def getFriendship(self,target_screen_name:str,Access : _Access.WeakAccess = None):
          if (Access == None):
            Access=_Actions.defaultAccess
          api = tweepy.API(Access.auth)
          resp=api.show_friendship(source_id=self.id,target_screen_name=target_screen_name)
          f1=_Friendship.Friendship(resp[0].__dict__)
          f2=_Friendship.Friendship(resp[1].__dict__)
          return (f1,f2)

     def postUpdateProfile(self,name=None,url=None,location=None,description=None,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.update_profile(name=name,url=url,location=location,description=description)
         return User(dictionary=resp)

     def postUpdateProfileImage(self,filePath,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.update_profile_image(filename=filePath)
         return User(dictionary=resp)

     def postUpdateProfileBanner(self,filePath,width=None, height=None, offset_left=None, offset_right=None,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.update_profile_banner(filename=filePath, width=width, height=height, offset_left=offset_left, offset_right=offset_right)
         return resp==None

     def getSuggestedUsersBySlug(self,slug,lang=None,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.suggested_users(slug=slug,lang=lang)
         lista=list()
         for u in resp:
             lista.append(User(dictionary=u))
         return lista

     def getSuggestedUsersWithTweetBySlug(self,slug,lang=None,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.suggested_users_tweets(slug=slug,lang=lang)
         lista=list()
         for u in resp:
             lista.append(User(dictionary=u))
         return lista

     def getSuggestedCategories(self,lang=None,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.suggested_categories(lang=lang)
         return resp

     def getBlocks(self,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         users = api.blocks()
         lista = list()
         for u in users:
             lista.append(User(dictionary=u))
         return lista;

     def postBlockCreate(self,user,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.create_block(id=user)
         return User(dictionary=resp)

     def postBlockDestroy(self,user,Access : _Access.StrongAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.destroy_block(id=user)
         return User(dictionary=resp)

     def getFavorites(self,page=0,Access : _Access.WeakAccess = None):
         if not self.screen_name:
             return _Actions.Actions.getFavorites(user=self.id,page=page)
         else:
            return _Actions.Actions.getFavorites(user=self.screen_name,page=page)

     def getLists(self,cursor=None,Access : _Access.WeakAccess = None):
         if (Access == None):
            Access=_Actions.defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp= api.lists_all(screen_name=self.screen_name)
         for l in resp:
             lista.append(_List.List(dictionary=l.__dict__))
         return lista

     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "USER: "+str(dic)

     def __repr__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "USER: "+str(dic)

