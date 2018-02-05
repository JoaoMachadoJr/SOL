#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod

class Post(ABC):
    '''
    Essa classe define o conteúdo do principal tipo de publicação na rede social.
    '''

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self,val: str):
        self.__text=val

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, val: str):
        self.__image = val

    @property
    def video(self) -> str:
        return self.__video

    @video.setter
    def video(self, val: str):
        self.__video = val

    @property
    def genericfile(self) -> str:
        return self.__genericfile

    @genericfile.setter
    def genericfile(self, val: str):
        self.__genericfile = val

