#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
from SOL_FACEBOOK import User
from SOL_FACEBOOK.experience import Experience
from SOL_FACEBOOK.page import Page


class Eduction:
    """
    Agrega informações sobre uma instituição de ensino onde um usuário tenha estudado, assim como informações básicas
    sobre quando ocorreu essa experiência
    """

    def __init__(self):
        self.__id = ""
        self.__classes = list()
        self.__concentration = list()
        self.__degree = None
        self.__school = None
        self.__type = ""
        self.__with_ = list()
        self.__year = None

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def classes(self) -> List[Experience]:
        return self.__classes

    @classes.setter
    def classes(self, val: List[Experience]):
        self.__classes = val

    @property
    def concentration(self) -> List[Page]:
        return self.__concentration

    @concentration.setter
    def concentration(self, val: List[Page]):
        self.__concentration = val

    @property
    def degree(self) -> Page:
        return self.__degree

    @degree.setter
    def degree(self, val: Page):
        self.__degree = val

    @property
    def school(self) -> Page:
        return self.__school

    @school.setter
    def school(self, val: Page):
        self.__school = val

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, val: str):
        self.__type = val

    @property
    def with_(self) -> List[User]:
        return self.__with_

    @with_.setter
    def with_(self, val: List[User]):
        self.__with_ = val

    @property
    def year(self) -> Page:
        return self.__year

    @year.setter
    def year(self, val: Page):
        self.__year = val
