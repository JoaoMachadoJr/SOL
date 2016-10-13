__author__ = 'Joao'
import _User
import lib.tweepy as tweepy
import _Access
import _Tweet
import _DirectMessage
import _List
import _Place

global defaultAccess
defaultAccess=None

class Actions:

    def setDefaultAccess(Access : _Access.WeakAccess):
        defaultAccess=Access

    def getUser(UsernameOrId, Access : _Access.WeakAccess = None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        user = api.get_user(UsernameOrId)
        return _User.User(dictionary=user)

    def getMultipleUsers(Ids_List, Access : _Access.WeakAccess = None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        users = api.lookup_users(Ids_List)
        lista = list()
        for user in users:
            lista.append(_User.User(dictionary=user))
        return lista

    def me(Access : _Access.WeakAccess = None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return _User.User(dictionary=api.me())

    def getTimelineFromUser(username, Access : _Access.WeakAccess=None, count=None, since_id=None, max_id=None, include_rts=False):
        if (Access == None):
            Access=defaultAccess
        return Actions.getUser(username,Access).getTimeline(Access,count=count,since_id=since_id,max_id=max_id,include_rts=include_rts)

    def getRetweetsFromTweet(id, Access : _Access.WeakAccess = None, count=None):
        return _Tweet.Tweet(id=id).getRetweets(Access=Access,count=count)

    def getTweet(id, Access : _Access.WeakAccess = None):
        return _Tweet.Tweet(id=id).getShow(Access)

    def getOembedFromTweet( url,Access : _Access.WeakAccess = None, maxwidth=None, hide_media=None, omit_script=None,align=None,related=None,lang=None):
        '''Retorna um Tweet em formato OEMBED, a partir de uma url
        documentado em https://dev.twitter.com/rest/reference/get/statuses/oembed
        '''
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return api.get_oembed(url=url,maxwidth=maxwidth,hide_media=hide_media,omit_script=omit_script,align=align,related=related,lang=lang)

    def getRetweetersFromTweet( id,Access : _Access.WeakAccess = None, cursor=None, stringify_ids=None):
        return _Tweet.Tweet(id=id).getRetweeters(id=id,cursor=cursor,stringify_ids=stringify_ids)

    def getMultipleTweet(ids : list, Access : _Access.WeakAccess = None, include_entities=None, trim_user=None, map=None):
         '''Pega os tweets a partir de uma lista de ids
         Documentado em https://dev.twitter.com/rest/reference/get/statuses/lookup
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

    def getMessagesSentByMe(Access : _Access.StrongAccess = None, since_id=None, max_id=None, count=None, page=None, full_text=None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.sent_direct_messages(since_id=since_id, max_id=max_id, count=count, page=page, full_text=full_text)
        lista = list()
        for m in messages:
            lista.append(_DirectMessage.DirectMessage(dictionary=m))
        return lista

    def getMyMessages(Access : _Access.StrongAccess = None, since_id=None, max_id=None, count=None,  full_text=None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.direct_messages(since_id=since_id, max_id=max_id, count=count, full_text=full_text)
        lista = list()
        for m in messages:
            lista.append(_DirectMessage.DirectMessage(dictionary=m))
        return lista

    def getMessageFromId(id,Access : _Access.StrongAccess = None, full_text=None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.get_direct_message(id=id,full_text=full_text)
        return _DirectMessage.DirectMessage(dictionary=messages)

    def searchTweets(q, Access : _Access.WeakAccess = None,lang=None, locale=None, since_id=None, geocode=None,max_id=None, since=None, until=None, result_type=None, count=None,include_entities=None, from_=None, to=None, source=None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        messages = api.search(q=q,lang=lang,locale=locale,since_id=since_id,geocode=geocode,max_id=max_id,since=since,until=until,result_type=result_type,count=count,include_entities=include_entities,to=to,source=source)
        lista = list()
        for m in messages:
            lista.append(_Tweet.Tweet(dictionary=m))
        return lista

    def getFriendshipInfo(source_id=None, source_screen_name=None,target_id=None,target_screen_name=None, Access : _Access.WeakAccess = None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return api.show_friendship(source_id=source_id, source_screen_name=source_screen_name,target_id=target_id,target_screen_name=target_screen_name )

    def postDestroyTweetById(id, Access : _Access.StrongAccess = None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return api.destroy_status(id)

    def postTweet(msg,latitude=None,longitude=None,reply_to=None,place_id=None,Access : _Access.StrongAccess = None):
        if (Access == None):
            Access=defaultAccess
        api = tweepy.API(Access.auth)
        return api.update_status(lat=latitude,long=longitude,status=msg,in_reply_to_status_id=reply_to,place_id=place_id)

    def postRetweet(id):
        return _Tweet.Tweet(id).postRetweet()

    def getFavorites(user, page=0,Access : _Access.WeakAccess = None):
         if (Access == None):
            Access=defaultAccess
         api = tweepy.API(Access.auth)
         resp = api.favorites(id=user,page=page)
         lista = list()
         for u in resp:
             lista.append(_Tweet.Tweet(dictionary=u))
         return lista

    def getTweetsFromList(owner_screen_name=None, slug=None, owner_id=None, list_id=None,since_id=None, max_id=None, count=None, include_rts=None,Access : _Access.WeakAccess = None):
         if (Access == None):
            Access=defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.list_timeline(owner_screen_name=owner_screen_name, slug=slug, owner_id=owner_id, list_id=list_id, since_id=since_id, max_id=max_id, count=count, include_rts=include_rts)
         lista = list()
         for tweet in resp:
             lista.append(_Tweet.Tweet(dictionary=tweet))
         return lista

    def postRemoveMemberFromList(screen_name=None, user_id=None, owner_screen_name=None,owner_id=None, slug=None, list_id=None,Access : _Access.WeakAccess = None):
         if (Access == None):
            Access=defaultAccess
         api = tweepy.API(Access.auth)
         resp=api.remove_list_member(screen_name=screen_name, user_id=user_id, owner_screen_name=owner_screen_name, owner_id=owner_id, slug=slug, list_id=list_id)
         return resp

    def getSubscribersFromList(owner_screen_name=None,slug=None,owner_id=None,list_id=None,cursor=None,Access : _Access.WeakAccess = None):
         '''
         Reference: list_subscribers
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.list_subscribers(owner_screen_name=owner_screen_name,slug=slug,owner_id=owner_id,list_id=list_id,cursor=cursor)
         for U in resp:
             lista.append(_User.User(dictionary=U.__dict__))
         return lista
    def getUserIsSubscriber(owner_screen_name=None,slug=None,screen_name=None,owner_id=None,list_id=None,user_id=None,Access : _Access.WeakAccess = None):
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

    def getUserIsMember(list_id=None,slug=None,user_id=None,screen_name=None,owner_screen_name=None,owner_id=None,Access : _Access.WeakAccess = None):
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

    def getMembersFromList(owner_screen_name=None,slug=None,list_id=None,owner_id=None,cursor=None,Access : _Access.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/lists/members
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.list_members(owner_screen_name=owner_screen_name,slug=slug,list_id=list_id,owner_id=owner_id,cursor=cursor)
         for L in resp:
             lista.append(_User.User(dictionary=L.__dict__))
         return lista

    def getList(owner_screen_name=None,owner_id=None,slug=None,list_id=None,Access : _Access.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/lists/show
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.get_list(owner_screen_name=owner_screen_name,owner_id=owner_id,slug=slug,list_id=list_id)
         return _List.List(dictionary=resp.__dict__)



    def postListMemberCreate(screen_name=None,user_id=None,owner_screen_name=None,owner_id=None,slug=None,list_id=None,Access : _Access.StrongAccess = None):
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

    def getTrendsByPlace(id=None,exclude=None,Access : _Access.WeakAccess = None):
         '''
         Reference: https://dev.twitter.com/rest/reference/get/trends/place
         '''
         if (Access == None):
             Access=defaultAccess
         api = tweepy.API(Access.auth)
         lista = list()
         resp=api.trends_place(id=id,exclude=exclude)
         return resp[0]

    def getTrendsAvailable(Access : _Access.WeakAccess = None):
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

    def getSubscriptionsFromUser(screen_name=None,user_id=None,cursor=None,Access : _Access.WeakAccess = None):
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













