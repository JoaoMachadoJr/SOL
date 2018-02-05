#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_MAIN import Post


class Post(Post):
    '''
    Essa classe define o conteúdo de um Post do Facebook.
    '''

    def __init__(self):
        self.id = id
        self.admin_creator = list()
        self.created_time = ""
        self.message = ""
        self.story = ""
        self.caption = ""
        self.description = ""
        self.feed_targeting = ""
        self.created_by = ""
        self.is_hidden = ""
        self.is_published = ""
        self.link = ""
        self.from_ = ""
        self.message_tags = list()
        self.name = ""
        self.picture = ""
        self.place = ""
        self.privacy = ""
        self.properties = ""
        self.shares = 0
        self.source = ""
        self.to = list()
        self.type = ""  # enum{link, status, photo, video, offer}
        self.updated_time = ""
        self.with_tags = list()

class Feed_targeting:
    '''
    Essa classe representa um conjunto de configurações de público alvo empregado em páginas do Facebook
    '''

    def __init__(self, dictionary=None):
        self.age_max=""
        self.age_min=""
        self.genders=""
        self.geo_locations=""
        self.locales=""
        self.education_statuses=""
        self.fan_of=""
        self.relationship_statuses=""