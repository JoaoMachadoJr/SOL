__author__ = 'Joao'
import lib.tweepy as tweepy
from SolTw import _DirectMessage as _DirectMessage
from SolTw import _WeakAccess as _WeakAccess
from SolTw import _StrongAccess as _StrongAccess
from SolTw import _TwitterUser as _TwitterUser
from SolTw import  _Tweet as _Tweet
from SolTw import _List as _List
from SolTw import _Place as _Place
from SolTw import _AuthenticatedTwitterUser

global defaultAccess
defaultAccess=None

class Actions:

    def setDefaultAccess(Access : _WeakAccess.WeakAccess):
        defaultAccess=Access

    def getUser(UsernameOrId, Access : _WeakAccess.WeakAccess = None):
        """ :reference: https://dev.twitter.com/rest/reference/get/users/show
        """
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        user = api.get_user(UsernameOrId)
        return _TwitterUser.TwitterUser(dictionary=user)

    def getMultipleUsers(Ids_List, Access : _WeakAccess.WeakAccess = None):
        """:reference: https://dev.twitter.com/rest/reference/get/users/show
        """
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        users = api.lookup_users(Ids_List)
        lista = list()
        for user in users:
            lista.append(_TwitterUser.TwitterUser(dictionary=user))
        return lista

    def me(Access : _StrongAccess.StrongAccess = None):
        """Return the Object of the authenticated user
        """
        return _AuthenticatedTwitterUser.AuthenticatedTwitterUser(Access)

    def getTimelineFromUser(username, Access : _WeakAccess.WeakAccess=None, count=None, since_id=None, max_id=None, include_rts=False):
         '''
         Reference https://dev.twitter.com/rest/reference/get/statuses/user_timeline
         '''
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         tweets = api.user_timeline(screen_name=username ,count=count, since_id=since_id, max_id=max_id, include_rts=include_rts)
         for tweet in tweets:
            lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

    def getRetweetsFromTweet(id, Access : _WeakAccess.WeakAccess = None, count=None):
         '''Reference https://dev.twitter.com/rest/reference/get/statuses/retweets/%3Aid
         '''
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         tweets = api.retweets(id=id ,count=count)
         lista = list()
         for tweet in tweets:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

    def getTweet(id, Access : _WeakAccess.WeakAccess = None):
         '''Reference https://dev.twitter.com/rest/reference/get/statuses/show/%3Aid
         '''
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         return _Tweet.Tweet(dictionary=api.get_status(id=id))

    def getOembedFromTweet( url,Access : _WeakAccess.WeakAccess = None, maxwidth=None, hide_media=None, omit_script=None,align=None,related=None,lang=None):
        '''Reference https://dev.twitter.com/rest/reference/get/statuses/oembed
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return api.get_oembed(url=url,maxwidth=maxwidth,hide_media=hide_media,omit_script=omit_script,align=align,related=related,lang=lang)

    def getRetweetersFromTweet( id,Access : _WeakAccess.WeakAccess = None, cursor=None, stringify_ids=None):
         '''Reference https://dev.twitter.com/rest/reference/get/statuses/retweeters/ids
         '''
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         users = api.retweeters(id=id,cursor=cursor,stringify_ids=stringify_ids)
         lista = list()
         for user in users:
             lista.append(_TwitterUser.TwitterUser(id=user))
         return lista;


    def getMultipleTweet(ids : list, Access : _WeakAccess.WeakAccess = None, include_entities=None, trim_user=None, map=None):
         '''https://dev.twitter.com/rest/reference/get/statuses/lookup
         '''
         if (Access == None):
            Access=defaultAccess
         string = ""
         for id in ids:
             string+=str(id)+","
         api = tweepy.API(Access.auth)
         tweets = api._statuses_lookup(id=string,include_entities=include_entities,trim_user=trim_user,map=map)
         lista = list()
         for tweet in tweets:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

    def getMessagesSentByMe(Access : _StrongAccess.StrongAccess = None, since_id=None, max_id=None, count=None, page=None, full_text=None):
        '''reference: https://dev.twitter.com/rest/reference/get/direct_messages/sent
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.sent_direct_messages(since_id=since_id, max_id=max_id, count=count, page=page, full_text=full_text)
        lista = list()
        for m in messages:
            lista.append(_DirectMessage.DirectMessage(dictionary=m))
        return lista

    def getMyMessages(Access : _StrongAccess.StrongAccess = None, since_id=None, max_id=None, count=None,  full_text=None):
        '''Reference: https://dev.twitter.com/rest/reference/get/direct_messages
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.direct_messages(since_id=since_id, max_id=max_id, count=count, full_text=full_text)
        lista = list()
        for m in messages:
            lista.append(_DirectMessage.DirectMessage(dictionary=m))
        return lista

    def getMessageFromId(id,Access : _StrongAccess.StrongAccess = None, full_text=None):
        """ :reference: https://dev.twitter.com/rest/reference/get/direct_messages/show
        """
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.get_direct_message(id=id,full_text=full_text)
        return _DirectMessage.DirectMessage(dictionary=messages)

    def searchTweets(q, Access : _WeakAccess.WeakAccess = None,lang=None, locale=None, since_id=None, geocode=None,max_id=None, since=None, until=None, result_type=None, count=None,include_entities=None, from_=None, to=None, source=None):
        '''Reference: reference: https://dev.twitter.com/rest/reference/get/search/tweets
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.search(q=q,lang=lang,locale=locale,since_id=since_id,geocode=geocode,max_id=max_id,since=since,until=until,result_type=result_type,count=count,include_entities=include_entities,to=to,source=source)
        lista = list()
        for m in messages:
            lista.append(_Tweet.Tweet(dictionary=m))
        return lista

    def getFriendshipInfo(source_id=None, source_screen_name=None,target_id=None,target_screen_name=None, Access : _WeakAccess.WeakAccess = None):
        '''reference: https://dev.twitter.com/rest/reference/get/friendships/show
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return api.show_friendship(source_id=source_id, source_screen_name=source_screen_name,target_id=target_id,target_screen_name=target_screen_name )

    def postDestroyTweetById(id, Access : _StrongAccess.StrongAccess = None):
        '''Reference: reference: https://dev.twitter.com/rest/reference/post/statuses/destroy/%3Aid
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        try:
            api.destroy_status(id)
            return True
        except tweepy.TweepError:
            return False

    def postTweet(msg,latitude=None,longitude=None,reply_to=None,place_id=None,Access : _StrongAccess.StrongAccess = None):
        '''Reference: https://dev.twitter.com/rest/reference/post/statuses/update
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        try:
            api.update_status(lat=latitude,long=longitude,status=msg,in_reply_to_status_id=reply_to,place_id=place_id)
            return True;
        except tweepy.TweepError:
             return False


    def postRetweet(id,Access : _StrongAccess.StrongAccess = None):
         '''Reference:  https://dev.twitter.com/rest/reference/post/statuses/retweet/%3Aid
         '''
         if (Access == None):
             Access= defaultAccess
         api=tweepy.API(Access.auth)
         try:
             api.retweet(id)
             api.retweets
             return True
         except tweepy.TweepError:
             return False

    def getFavorites(user, page=0,Access : _WeakAccess.WeakAccess = None):
         '''Reference: https://dev.twitter.com/rest/reference/get/favorites/list
         '''
         if (Access == None):
            Access=defaultAccess
         api = tweepy.API(Access.auth)
         resp = api.favorites(id=user,page=page)
         lista = list()
         for u in resp:
             lista.append(_Tweet.Tweet(dictionary=u))
         return lista

    def getTweetsFromList(owner_screen_name=None, slug=None, owner_id=None, list_id=None,since_id=None, max_id=None, count=None, include_rts=None,Access : _WeakAccess.WeakAccess = None):
         '''Reference: https://dev.twitter.com/docs/api/1.1/get/lists/statuses
         '''
         if (Access == None):
            Access=defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.list_timeline(owner_screen_name=owner_screen_name, slug=slug, owner_id=owner_id, list_id=list_id, since_id=since_id, max_id=max_id, count=count, include_rts=include_rts)
         lista = list()
         for tweet in resp:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista

    def postRemoveMemberFromList(screen_name=None, user_id=None, owner_screen_name=None,owner_id=None, slug=None, list_id=None,Access : _WeakAccess.WeakAccess = None):
         '''Reference: https://dev.twitter.com/docs/api/1.1/post/lists/members/destroy
         '''
         if (Access == None):
            Access=defaultAccess
         api = tweepy.API(Access.auth)
         try:
             resp=api.remove_list_member(screen_name=screen_name, user_id=user_id, owner_screen_name=owner_screen_name, owner_id=owner_id, slug=slug, list_id=list_id)
             return True
         except tweepy.TweepError:
            return False


    def getSubscribersFromList(owner_screen_name=None,slug=None,owner_id=None,list_id=None,cursor=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference:  https://dev.twitter.com/docs/api/1.1/get/lists/subscribers
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.list_subscribers(owner_screen_name=owner_screen_name,slug=slug,owner_id=owner_id,list_id=list_id,cursor=cursor)
         for U in resp:
             lista.append(_TwitterUser.TwitterUser(dictionary=U.__dict__))
         return lista
    def getUserIsSubscriber(owner_screen_name=None,slug=None,screen_name=None,owner_id=None,list_id=None,user_id=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/docs/api/1.1/get/lists/subscribers/show
         '''
         try:
             if (Access == None):
                 Access=defaultAccess
             api = tweepy.API(Access.auth)
             lista = list()
             resp=api.show_list_subscriber(owner_screen_name=owner_screen_name,slug=slug,screen_name=screen_name,owner_id=owner_id,list_id=list_id,user_id=user_id)
             return True
         except tweepy.TweepError:
             return False

    def getUserIsMember(list_id=None,slug=None,user_id=None,screen_name=None,owner_screen_name=None,owner_id=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/lists/members/show
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         try:
             resp=api.show_list_member(list_id=list_id,slug=slug,user_id=user_id,screen_name=screen_name,owner_screen_name=owner_screen_name,owner_id=owner_id)
             return True
         except tweepy.TweepError:
             return False

    def getMembersFromList(owner_screen_name=None,slug=None,list_id=None,owner_id=None,cursor=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/lists/members
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.list_members(owner_screen_name=owner_screen_name,slug=slug,list_id=list_id,owner_id=owner_id,cursor=cursor)
         for L in resp:
             lista.append(_TwitterUser.TwitterUser(dictionary=L.__dict__))
         return lista

    def getList(owner_screen_name=None,owner_id=None,slug=None,list_id=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/lists/show
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.get_list(owner_screen_name=owner_screen_name,owner_id=owner_id,slug=slug,list_id=list_id)
         return _List.List(dictionary=resp.__dict__)



    def postListMemberCreate(screen_name=None,user_id=None,owner_screen_name=None,owner_id=None,slug=None,list_id=None,Access : _StrongAccess.StrongAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/post/lists/members/create
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         try:
            resp=api.add_list_member(screen_name=screen_name,user_id=user_id,owner_screen_name=owner_screen_name,owner_id=owner_id,slug=slug,list_id=list_id)
            return True
         except tweepy.TweepError:
             return False

    def getTrendsByPlace(id=None,exclude=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/trends/place
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.trends_place(id=id,exclude=exclude)
         return resp[0]

    def getTrendsAvailable(Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/trends/available
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.trends_available()
         for place in resp:
             lista.append(_Place.Place(dictionary=place))
         return lista

    def getSubscriptionsFromUser(screen_name=None,user_id=None,cursor=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/lists/subscriptions
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.lists_subscriptions(screen_name=screen_name,user_id=user_id,cursor=cursor)
         for L in resp:
             lista.append(_List.List(dictionary=L.__dict__))
         return lista

    def getTrendsClosest(lat=None,long=None,Access : _WeakAccess.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/trends/closest
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.trends_closest(lat=lat,long=long)
         return resp[0]

    def postDestroyDirectMessage(self,id,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/post/direct_messages/destroy
            :allowed_param:'id'
         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         return _DirectMessage.DirectMessage(dictionary= api.destroy_direct_message(id=id))

    def postReply( id,msg,latitude=None,longitude=None,place_id=None,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/post/statuses/update
            :allowed_param:'status', 'in_reply_to_status_id', 'lat', 'long', 'source', 'place_id', 'display_coordinates', 'media_ids'
         """
         if (Access == None):
            Access= defaultAccess
         api=tweepy.API(Access.auth)
         resp=api.update_status(in_reply_to_status_id=id, lat=latitude,long=longitude,status=msg,place_id=place_id)
         return _Tweet.Tweet(dictionary=resp.__dictt__())

    def postFavoriteTweetCreate(id,Access  : _StrongAccess.StrongAccess = None ):
         ''' :reference:https://dev.twitter.com/rest/reference/post/favorites/create
         '''
         from SolTw import _Tweet
         if (Access == None):
            Access= defaultAccess
         api=tweepy.API(Access.auth)
         return _Tweet.Tweet(dictionary=api.create_favorite(id=id))

    def postFavoriteTweetDestroy(id,Access  : _StrongAccess.StrongAccess = None ):
         ''' :reference:https://dev.twitter.com/rest/reference/post/favorites/destroy
         '''
         from SolTw import _Tweet
         if (Access == None):
            Access= defaultAccess
         api=tweepy.API(Access.auth)
         return _Tweet.Tweet(dictionary=api.destroy_favorite(id=id))

    def getMentionsTimelineFromUser( Access : _StrongAccess.StrongAccess = None, count=None, since_id=None, max_id=None):
        '''
            Reference: https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline
        '''
        if (Access == None):
            Access= defaultAccess
        api = tweepy.API(Access.auth)
        mentions = api.mentions_timeline(count=count, since_id=since_id, max_id=max_id)
        lista = list()
        for mention in mentions:
            lista.append(_Tweet.Tweet(dictionary=mention))
        return lista

    def getHomeTimelineFromUser( Access : _StrongAccess.StrongAccess = None,id=id, count=None, since_id=None, max_id=None):
         '''
            Reference: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
         '''
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         tweets = api.home_timeline(user_id=id ,count=count, since_id=since_id, max_id=max_id)
         lista = list()
         for tweet in tweets:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista;

    def getFriendsFromUser(id, Access : _WeakAccess.WeakAccess = None, cursor=None):
         '''Pega os amigos do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friends/list
         '''
         from SolTw import _TwitterUser
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         friends = api.friends(user_id=id, cursor=cursor)
         lista = list()
         for f in friends:
             lista.append(_TwitterUser.TwitterUser(dictionary=f))
         return lista;

    def getFollowersFromUser( id,Access : _WeakAccess.WeakAccess = None, cursor=None, count=None):
         '''Pega os seguidores do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/followers/list
         '''
         from SolTw import _TwitterUser
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         users = api.followers(user_id=id, cursor=cursor,count=count)
         lista = list()
         for u in users:
             lista.append(_TwitterUser.TwitterUser(dictionary=u))
         return lista;

    def getFriendshipIncomingFromUser(id, Access : _StrongAccess.StrongAccess = None, cursor=None):
         '''Pega requisições de amizade do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friendships/incoming
         '''
         from SolTw import _TwitterUser
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         friends = api.friendships_incoming( cursor=cursor)
         lista = list()
         for f in friends:
             lista.append(_TwitterUser.TwitterUser(id=f))
         return lista;

    def getFriendshipOutgoingFromUser( Access : _StrongAccess.StrongAccess = None, cursor=None):
         '''Pega requisições de amizade feita pelo usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friendships/outgoing
         '''
         from SolTw import _TwitterUser
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         friends = api.friendships_outgoing( cursor=cursor)
         lista = list()
         for f in friends:
             lista.append(_TwitterUser.TwitterUser(id=f))
         return lista;
    def postTweet( msg,latitude=None,longitude=None,place_id=None,Access : _StrongAccess.StrongAccess = None):
         '''
            reference: https://dev.twitter.com/rest/reference/post/statuses/update
         '''
         if (Access == None):
            Access= defaultAccess
         api=tweepy.API(Access.auth)
         api.update_status(lat=latitude,long=longitude,status=msg,place_id=place_id)
         return True

    def postDirectMessage( receiver, msg,Access : _StrongAccess.StrongAccess = None ):
         """ :reference: https://dev.twitter.com/rest/reference/post/direct_messages/new

        """
         from SolTw import _TwitterUser
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         if (isinstance(receiver,_TwitterUser.TwitterUser)):
             user=receiver.id
         api.send_direct_message(user=user,text=msg)
         return True


    def postFriendshipCreate( user,follow : bool=None,Access : _StrongAccess.StrongAccess = None):
        """ :reference: https://dev.twitter.com/rest/reference/post/friendships/create

        """

        from SolTw import _TwitterUser
        if (Access == None):
            Access= defaultAccess
        api = tweepy.API(Access.auth)
        return _TwitterUser.TwitterUser(dictionary=api.create_friendship(id=user,follow=follow))

    def postFriendshipDestroy( user,Access : _StrongAccess.StrongAccess = None):
        """ :reference: https://dev.twitter.com/rest/reference/post/friendships/destroy

        """
        from SolTw import _TwitterUser
        if (Access == None):
            Access= defaultAccess
        api = tweepy.API(Access.auth)
        return _TwitterUser.TwitterUser(dictionary=api.destroy_friendship(id=user))

    def getFriendship(source_id:str,target_screen_name:str,Access : _WeakAccess.WeakAccess = None):
          """ :reference: https://dev.twitter.com/rest/reference/get/friendships/show
          """
          from SolTw import _Friendship
          if (Access == None):
            Access= defaultAccess
          api = tweepy.API(Access.auth)
          resp=api.show_friendship(source_id=source_id,target_screen_name=target_screen_name)
          f1= _Friendship.Friendship(resp[0].__dict__)
          f2= _Friendship.Friendship(resp[1].__dict__)
          return (f1,f2)

    def postUpdateProfile(name=None,url=None,location=None,description=None,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/post/account/update_profile
         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.update_profile(name=name,url=url,location=location,description=description)
         return _TwitterUser.TwitterUser(dictionary=resp)

    def getSuggestedUsersBySlug(slug,lang=None,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/get/users/suggestions/%3Aslug

         """

         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.suggested_users(slug=slug,lang=lang)
         lista=list()
         for u in resp:
             lista.append(_TwitterUser.TwitterUser(dictionary=u))
         return lista

    def getSuggestedUsersWithTweetBySlug(slug,lang=None,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/get/users/suggestions/%3Aslug/members

         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.suggested_users_tweets(slug=slug,lang=lang)
         lista=list()
         for u in resp:
             lista.append(_TwitterUser.TwitterUser(dictionary=u))
         return lista

    def getSuggestedCategories(lang=None,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/get/users/suggestions

         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.suggested_categories(lang=lang)
         return resp

    def getBlocks(Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/get/blocks/list
            :allowed_param:'cursor'
         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         users = api.blocks()
         lista = list()
         for u in users:
             lista.append(_TwitterUser.TwitterUser(dictionary=u))
         return lista;

    def postBlockCreate(user,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/post/blocks/create
            :allowed_param:'id', 'user_id', 'screen_name'
         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.create_block(id=user)
         return _TwitterUser.TwitterUser(dictionary=resp)

    def postBlockDestroy(user,Access : _StrongAccess.StrongAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/post/blocks/destroy
            :allowed_param:'id', 'user_id', 'screen_name'
         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.destroy_block(id=user)
         return _TwitterUser.TwitterUser(dictionary=resp)

    def getListsFromUser(screen_name,Access : _WeakAccess.WeakAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/get/lists/list
            '
         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp= api.lists_all(screen_name=screen_name)
         for l in resp:
             lista.append(_List.List(dictionary=l.__dict__))
         return lista



    def getListsMembershipFromUser(screen_name,count=None, cursor=None,filter_to_owned_lists=None,Access : _WeakAccess.WeakAccess = None):
         """ :reference: https://dev.twitter.com/rest/reference/get/lists/memberships

         """
         if (Access == None):
            Access= defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp= api.lists_memberships(screen_name=screen_name,filter_to_owned_lists=filter_to_owned_lists,cursor=cursor,count=count)
         for l in resp:
             lista.append(_List.List(dictionary=l.__dict__))
         return lista