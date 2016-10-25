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












