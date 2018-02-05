#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Media():
    """
    Essa classe representa uma media. Usualmente, se trata de uma imagem ou um vídeo.
    """

    def __init__(self):
        self.display_url = ""
        self.expanded_url = ""
        self.id = id
        self.media_url = ""
        self.sizes = None
        self.source_status_id = ""
        self.type = ""
        self.url = ""

class Size():
    """
    Essa classe agrega as dimensões de uma imagem ou vídeo.
    """

    def __init__(self):
        self.h = ""
        self.resize = ""
        self.w = ""