__author__ = 'Joao'
import lib.tweepy as tweepy
from SolTw import _WeakAccess as _WeakAccess


class StrongAccess(_WeakAccess.WeakAccess):
    def __init__(self, Consumer_Key, Consumer_Secret,Access_Token, Access_Token_Secret):
        from SolTw import _Actions as _Actions
        self.consumer_key = Consumer_Key
        self.consumer_secret = Consumer_Secret
        self.access_token=Access_Token
        self.access_token_secret=Access_Token_Secret
        self.auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
        self.auth.set_access_token(Access_Token, Access_Token_Secret)
        self.auth.get_authorization_url()
        if (_Actions.defaultAccess==None):
            _Actions.defaultAccess=self

    def me(self):
        from SolTw import _TwitterUser
        return _TwitterUser.TwitterUser(dictionary=tweepy.API(self.auth).me())