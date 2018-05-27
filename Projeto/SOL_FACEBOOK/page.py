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
        self.__is_permanently_closed = ""
        self.__link = ""
        self.__location = ""
        self.__name = ""
        self.__new_like_count = ""
        self.__parent_page = None
        self.__phone = ""
        self.__single_line_address = ""
        self.__username = ""
        self.__website = ""

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

    @property
    def is_permanently_closed(self) -> str:
        """Informações sobre a Page ter sido encerrada."""
        return self.__is_permanently_closed

    @is_permanently_closed.setter
    def is_permanently_closed(self, val: str):
        self.__is_permanently_closed = val

    @property
    def link(self) -> str:
        """Endereço eletrônico para a página"""
        return self.__link

    @link.setter
    def link(self, val: str):
        self.__link = val

    @property
    def location(self) -> str:
        """Localização geográfica da página"""
        return self.__location

    @location.setter
    def location(self, val: str):
        self.__location = val

    @property
    def name(self) -> str:
        """Nome da página"""
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def new_like_count(self) -> str:
        """Quantidade de curtidas recebidas recentemente"""
        return self.__new_like_count

    @new_like_count.setter
    def new_like_count(self, val: str):
        self.__new_like_count = val

    @property
    def parent_page(self) -> 'Page':
        """Página principal. Preenchido apenas em páginas derivadas de outras."""
        return self.__parent_page

    @parent_page.setter
    def parent_page(self, val: 'Page'):
        self.__parent_page = val

    @property
    def phone(self) -> str:
        """Telefone de contato da página"""
        return self.__phone

    @phone.setter
    def phone(self, val: str):
        self.__phone = val

    @property
    def single_line_address(self) -> str:
        """Endereço físico da página"""
        return self.__single_line_address

    @single_line_address.setter
    def single_line_address(self, val: str):
        self.__single_line_address = val

    @property
    def username(self) -> str:
        """Um apelido para a página."""
        return self.__username
    
    @username.setter
    def username(self, val: str):
        self.__username = val
    
    @property
    def website(self) -> str:
        """Site externo relacionado à página"""
        return self.__website

    @website.setter
    def website(self, val: str):
        self.__website = val


