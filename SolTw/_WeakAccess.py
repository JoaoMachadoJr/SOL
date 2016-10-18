__author__ = 'Joao'
#from SolTw import _TwitterUser as _TwitterUser

__author__ = 'Joao'
import lib.tweepy as tweepy


class WeakAccess():
    def __init__(self, Consumer_Key, Consumer_Secret):
        from SolTw import _Actions

        self.consumer_key = Consumer_Key
        self.consumer_secret = Consumer_Secret
        self.auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
        self.auth.get_authorization_url()
        if (_Actions.defaultAccess==None):
            _Actions.defaultAccess=self

    def verify_credentials(self):
         from SolTw import _TwitterUser
         api=tweepy.API(self.auth)
         resp=api.verify_credentials()
         if resp!=False:
             resp= _TwitterUser.TwitterUser(dictionary=resp.__dict__)
         return resp

    def rate_limit_status(self):
         api=tweepy.API(self.auth)
         return api.rate_limit_status()