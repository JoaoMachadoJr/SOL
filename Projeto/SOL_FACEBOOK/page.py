#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SOL_FACEBOOK.coverphoto import CoverPhoto


class Page:
    """
    Essa classe representa uma página do Facebook
    """

    def __init__(self):
        self.__id = ""
        self.__about = ""
        self.__token = ""
        self.__best_page = None
        self.__category = ""
        self.__category_list = ""
        self.__contact_address = ""
        self.__cover = None
        self.__current_location = ""
        self.__description = ""
        self.__display_subtext = ""
        self.__emails = ""
        self.__likes = ""
        self.__general_info = ""
        self.is_permanently_closed = ""
        self.is_published = ""
        self.is_unclaimed = ""
        self.is_verified = ""
        self.leadgen_tos_accepted = ""
        self.link = ""
        self.location = ""
        self.name = ""
        self.new_like_count = ""
        self.parent_page = None
        self.phone = ""
        self.single_line_address = ""
        self.store_number = ""
        self.username = ""
        self.website = ""

    @property
    def id(self) -> str:
        """Identificador único da entidade"""
        return self.__id

    @id.setter
    def id(self, val: str):
        self.__id = val

    @property
    def about(self) -> str:
        """Apresentação da página"""
        return self.__about

    @about.setter
    def about(self, val: str):
        self.__about = val

    @property
    def token(self) -> str:
        """Token de acesso da página, se aplicável"""
        return self.__token

    @token.setter
    def token(self, val: str):
        self.__token = val

    @property
    def best_page(self) -> 'Page':
        """Página sobre o mesmo assunto recomendada pela própria rede social"""
        return self.__best_page

    @best_page.setter
    def best_page(self, val: 'Page'):
        self.__best_page = val

    @property
    def category(self) -> str:
        """Categoria principal da página"""
        return self.__category

    @category.setter
    def category(self, val: str):
        self.__category = val

    @property
    def category_list(self) -> str:
        """Todas as categorias da página"""
        return self.__category_list

    @category_list.setter
    def category_list(self, val: str):
        self.__category_list = val

    @property
    def contact_address(self) -> str:
        """Endereço para contato"""
        return self.__contact_address

    @contact_address.setter
    def contact_address(self, val: str):
        self.__contact_address = val

    @property
    def cover(self) -> CoverPhoto:
        """Foto de capa da página"""
        return self.__cover

    @cover.setter
    def cover(self, val: CoverPhoto):
        self.__cover = val

    @property
    def current_location(self) -> str:
        """Localização da página"""
        return self.__current_location
    
    @current_location.setter
    def current_location(self, val: str):
        self.__current_location = val
    
    @property
    def description(self) -> str:
        """Descrição da página"""
        return self.__description
    
    @description.setter
    def description(self, val: str):
        self.__description = val
    
    @property
    def display_subtext(self) -> str:
        """Pequena descrição da página"""
        return self.__display_subtext
    
    @display_subtext.setter
    def display_subtext(self, val: str):
        self.__display_subtext = val
    
    @property
    def emails(self) -> str:
        """E-mails de contato da página"""
        return self.__emails

    @emails.setter
    def emails(self, val: str):
        self.__emails = val

    @property
    def likes(self) -> str:
        """Outras páginas que receberam 'like' dessa página"""
        return self.__likes

    @likes.setter
    def likes(self, val: str):
        self.__likes = val

    @property
    def general_info(self) -> str:
        """Informações gerais"""
        return self.__general_info

    @general_info.setter
    def general_info(self, val: str):
        self.__general_info = val


