from lib import tweepy

__author__ = 'Joao'
from SolTw import _TwitterUser
from SolTw import _StrongAccess
from SolTw import _Actions

class AuthenticatedTwitterUser(_TwitterUser.TwitterUser):
    def __init__(self,token : _StrongAccess.StrongAccess):
        dictionary=tweepy.API(token.auth).me()
        usuario=_TwitterUser.TwitterUser(dictionary=dictionary)
        for k in usuario.__dict__.keys():
            self.__dict__[k]=usuario.__dict__[k]
        self.token=token

    def getSentMessages(self,since_id=None, max_id=None, count=None, page=None, full_text=None):
         '''reference: https://dev.twitter.com/rest/reference/get/direct_messages/sent
         '''
         from SolTw import _Actions
         return _Actions.Actions.getMessagesSentByMe(Access=self.token,since_id=since_id,max_id=max_id,count=count,page=page,full_text=full_text)

    def getDirectMessages(self, since_id=None, max_id=None, count=None,  full_text=None):
         '''Reference: https://dev.twitter.com/rest/reference/get/direct_messages
         '''
         return _Actions.Actions.getMyMessages(Access=self.token, since_id=since_id,max_id=max_id,count=count,full_text=full_text)

    def getMentionsTimeline(self,  count=None, since_id=None, max_id=None):
         '''
            Documentado em https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline
         '''
         return _Actions.Actions.getMentionsTimelineFromUser(self.token,count,since_id,max_id)

    def getHomeTimeline(self, count=None, since_id=None, max_id=None):
         '''
            Reference: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
         '''
         return _Actions.Actions.getHomeTimeline(self.token,id,count,since_id,max_id)


    def getFriendshipIncoming(self, cursor=None):
         '''Pega requisições de amizade do usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friendships/incoming
         '''
         return _Actions.Actions.getFriendshipIncomingFromUser(id,self.token,cursor);

    def getFriendshipOutgoing(self, cursor=None):
         '''Pega requisições de amizade feita pelo usuario
         Documentado em https://dev.twitter.com/rest/reference/get/friendships/outgoing
         '''
         return _Actions.Actions.getFriendshipOutgoingFromUser(self.token,cursor)

    def postTweet(self, msg,latitude=None,longitude=None,place_id=None):
         '''
         reference: https://dev.twitter.com/rest/reference/post/statuses/update
         '''
         return _Actions.Actions.postTweet(msg,latitude,longitude,place_id,self.token)

    def postDirectMessage(self, receiver, msg ):
         ''' :reference: https://dev.twitter.com/rest/reference/post/direct_messages/new

         '''
         return _Actions.Actions.postDirectMessage(receiver,msg,self.token)


    def postFriendshipCreate(self, user,follow : bool=None):
        """ :reference: https://dev.twitter.com/rest/reference/post/direct_messages/new

        """
        return _Actions.Actions.postFriendshipCreate(user,follow,self.token)

    def postFriendshipDestroy(self,user):
        """ :reference: https://dev.twitter.com/rest/reference/post/direct_messages/new

        """
        return _Actions.Actions.postFriendshipDestroy(user,self.token)

    def postUpdateProfile(self,name=None,url=None,location=None,description=None):
         """ :reference: https://dev.twitter.com/rest/reference/post/account/update_profile
         """
         return _Actions.Actions.postUpdateProfile(name,url,location,description,self.token)

    def getSuggestedUsersBySlug(self,slug,lang=None):
         """ :reference: https://dev.twitter.com/rest/reference/get/users/suggestions/%3Aslug

         """
         return _Actions.Actions.getSuggestedUsersBySlug(slug,lang,self.token)

    def getSuggestedUsersWithTweetBySlug(self,slug,lang=None):
         """ :reference: https://dev.twitter.com/rest/reference/get/users/suggestions/%3Aslug/members

         """
         return _Actions.Actions.getSuggestedUsersWithTweetBySlug(slug,lang,self.token)

    def getSuggestedCategories(self,lang=None):
         """ :reference: https://dev.twitter.com/rest/reference/get/users/suggestions

         """
         return _Actions.Actions.getSuggestedCategories(lang,self.token)

    def getBlocks(self):
         """ :reference: https://dev.twitter.com/rest/reference/get/blocks/list
            :allowed_param:'cursor'
         """
         return _Actions.Actions.getBlocks(self.token)

    def postBlockCreate(self,user):
         """ :reference: https://dev.twitter.com/rest/reference/post/blocks/create
            :allowed_param:'id', 'user_id', 'screen_name'
         """
         return _Actions.Actions.postBlockCreate(user,self.token)

    def postBlockDestroy(self,user):
         """ :reference: https://dev.twitter.com/rest/reference/post/blocks/destroy
            :allowed_param:'id', 'user_id', 'screen_name'
         """
         return _Actions.Actions.postBlockDestroy(user,self.token)

    def postSubscribe(self,owner_screen_name=None,slug=None,owner_id=None,list_id=None):
         '''
         Reference: https://dev.twitter.com/rest/reference/post/lists/subscribers/create
         '''
         return _Actions.Actions.postSubscribe(owner_screen_name,slug,owner_id,list_id,self.token)

    def postSubscribeDestroy(self,owner_screen_name=None,slug=None,owner_id=None,list_id=None):
         '''
         Reference: https://dev.twitter.com/rest/reference/post/lists/subscribers/create
         '''
         return _Actions.Actions.postSubscribeDestroy(owner_screen_name,slug,owner_id,list_id,self.token)


