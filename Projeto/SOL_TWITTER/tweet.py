#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_MAIN import Post
from SOL_TWITTER.entities import Entities

class Tweet(Post):
    '''
    Essa classe define o conteúdo de um Tweet do Twitter.
    '''

    def __init__(self):
        self.coordinates = None
        self.created_at = ""
        self.entities = None
        self.favorite_count = ""
        self.favorited = ""
        self.id = id
        self.in_reply_to_screen_name = ""
        self.lang = ""
        self.place = None
        self.quoted_status = None
        self.retweet_count = ""
        self.retweeted = ""
        self.retweeted_status = None
        self.text = ""
        self.user = None