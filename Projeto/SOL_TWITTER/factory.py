#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SOL_TWITTER import user
from SOL_TWITTER import tweet
from SOL_TWITTER import coordinates
from SOL_TWITTER import entities
from SOL_TWITTER import place
from SOL_TWITTER import media


class Factory:
    """
    Essa classe será responsável por criar objetos a partir de dicionários
    """

    @staticmethod
    def casttodictionary(object) -> dict:
        """
        Esse método recebe um objeto qualquer, e retorna um dicionário onde suas chaves são os nomes dos seus atributos,
        e seus valores são os valores dos atributos

        Args:
            object: Um objeto qualquer
        returns:
            Um dicionário
        """
        if object is None:
            return dict()
        elif isinstance(object, dict):
            return object
        else:
            return object.__dict__

    @staticmethod
    def user(dictionary: dict) -> user.User:
        a_user = user.User()
        dictionary=Factory.casttodictionary(dictionary)
        if ("created_at" in dictionary):
            a_user.created_at = dictionary["created_at"]
        if ("description" in dictionary):
            a_user.description = dictionary["description"]
        if ("favourites_count" in dictionary):
            a_user.favourites_count = dictionary["favourites_count"]
        if ("followers_count" in dictionary):
            a_user.followers_count = dictionary["followers_count"]
        if ("friends_count" in dictionary):
            a_user.friends_count = dictionary["friends_count"]
        if ("id" in dictionary):
            a_user.id = dictionary["id"]
        if ("id_str" in dictionary):
            a_user.id_str = dictionary["id_str"]
        if ("lang" in dictionary):
            a_user.lang = dictionary["lang"]
        if ("listed_count" in dictionary):
            a_user.listed_count = dictionary["listed_count"]
        if ("location" in dictionary):
            a_user.location = dictionary["location"]
        if ("name" in dictionary):
            a_user.name = dictionary["name"]
        if ("notifications" in dictionary):
            a_user.notifications = dictionary["notifications"]
        if ("profile_background_image_url" in dictionary):
            a_user.profile_background_image_url = dictionary["profile_background_image_url"]
        if ("profile_banner_url" in dictionary):
            a_user.profile_banner_url = dictionary["profile_banner_url"]
        if ("profile_image_url" in dictionary):
            a_user.profile_image_url = dictionary["profile_image_url"]
        if ("screen_name" in dictionary):
            a_user.screen_name = dictionary["screen_name"]
        if ("show_all_inline_media" in dictionary):
            a_user.show_all_inline_media = dictionary["show_all_inline_media"]
        if ("status" in dictionary):
            a_user.status = Factory.tweet(dictionary=dictionary["status"])
        if ("statuses_count" in dictionary):
            a_user.statuses_count = dictionary["statuses_count"]
        if ("time_zone" in dictionary):
            a_user.time_zone = dictionary["time_zone"]
        if ("url" in dictionary):
            a_user.url = dictionary["url"]
        if ("verified" in dictionary):
            a_user.verified = dictionary["verified"]
        return a_user

    @staticmethod
    def tweet(dictionary: dict) -> tweet.Tweet:
        a_tweet = tweet.Tweet()
        dictionary = Factory.casttodictionary(dictionary)
        if ("coordinates" in dictionary):
            a_tweet.coordinates = Factory.coordinates(dictionary=dictionary["coordinates"])
        if ("created_at" in dictionary):
            a_tweet.created_at = dictionary["created_at"]
        if ("entities" in dictionary):
            a_tweet.entities = Factory.entities(dictionary=dictionary["entities"])
        if ("favorite_count" in dictionary):
            a_tweet.favorite_count = dictionary["favorite_count"]
        if ("favorited" in dictionary):
            a_tweet.favorited = dictionary["favorited"]
        if ("id" in dictionary):
            a_tweet.id = dictionary["id"]
        if ("in_reply_to_screen_name" in dictionary):
            a_tweet.in_reply_to_screen_name = dictionary["in_reply_to_screen_name"]
        if ("lang" in dictionary):
            a_tweet.lang = dictionary["lang"]
        if ("place" in dictionary):
            a_tweet.place = Factory.place(dictionary=dictionary["place"])
        if ("quoted_status" in dictionary):
            a_tweet.quoted_status = Factory.tweet(dictionary=dictionary["quoted_status"])
        if ("retweet_count" in dictionary):
            a_tweet.retweet_count = dictionary["retweet_count"]
        if ("retweeted" in dictionary):
            a_tweet.retweeted = dictionary["retweeted"]
        if ("retweeted_status" in dictionary):
            a_tweet.retweeted_status = Factory.tweet(dictionary=dictionary["retweeted_status"])
        if ("text" in dictionary):
            a_tweet.text = dictionary["text"]
        if ("user" in dictionary):
            a_tweet.user = Factory.user(dictionary=dictionary["user"])
        return a_tweet

    @staticmethod
    def coordinates(dictionary: dict) -> coordinates.Coordinates:
        a_coordinates = coordinates.Coordinates();
        dictionary = Factory.casttodictionary(dictionary)
        if ("coordinates" in dictionary):
            a_coordinates.coordinates = dictionary["coordinates"]
        if ("type" in dictionary):
            a_coordinates.type = dictionary["type"]
        return a_coordinates

    @staticmethod
    def entities(dictionary: dict) -> entities.Entities:
        a_entities = entities.Entities();
        dictionary = Factory.casttodictionary(dictionary)
        if ("hashtags" in dictionary):
            for hash in dictionary["hashtags"]:
                a_entities.hashtags.append(hash["text"])
        if ("media" in dictionary):
            for m in dictionary["media"]:
                a_entities.media.append(Factory.media(dictionary=m))
        if ("urls" in dictionary):
            for url in dictionary["urls"]:
                a_entities.urls.append(url["display_url"])
        if ("user_mentions" in dictionary):
            for mention in dictionary["user_mentions"]:
                a_entities.user_mentions.append(mention["screen_name"])
        return a_entities

    @staticmethod
    def place_attributes(dictionary: dict) -> place.Place_Attributes:
        a_place_attributes = place.Place_Attributes()
        dictionary = Factory.casttodictionary(dictionary)
        if ("street_address" in dictionary):
            a_place_attributes.street_address = dictionary["street_address"]
        if ("locality" in dictionary):
            a_place_attributes.locality = dictionary["locality"]
        if ("region" in dictionary):
            a_place_attributes.region = dictionary["region"]
        if ("iso3" in dictionary):
            a_place_attributes.iso3 = dictionary["iso3"]
        if ("postal_code" in dictionary):
            a_place_attributes.postal_code = dictionary["postal_code"]
        if ("phone" in dictionary):
            a_place_attributes.phone = dictionary["phone"]
        if ("twitter" in dictionary):
            a_place_attributes.twitter = dictionary["twitter"]
        if ("url" in dictionary):
            a_place_attributes.url = dictionary["url"]
        if ("app:id" in dictionary):
            a_place_attributes.app_id = dictionary["app:id"]
        return a_place_attributes

    @staticmethod
    def bounding_box(dictionary: dict) -> place.Bounding_box:
        a_bounding_box = place.Bounding_box()
        dictionary = Factory.casttodictionary(dictionary)
        if ("coordinates" in dictionary):
            a_bounding_box.coordinates = dictionary["coordinates"]
        if ("type" in dictionary):
            a_bounding_box.type = dictionary["type"]
        return a_bounding_box

    @staticmethod
    def place(dictionary: dict) -> place.Place:
        a_place = place.Place();
        dictionary = Factory.casttodictionary(dictionary)
        if ("attributes" in dictionary):
            a_place.attributes = Factory.place_attributes(dictionary=dictionary["attributes"])
        if ("bounding_box" in dictionary):
            a_place.bounding_box = Factory.bounding_box(dictionary=dictionary["bounding_box"])
        if ("country" in dictionary):
            a_place.country = dictionary["country"]
        if ("country_code" in dictionary):
            a_place.country_code = dictionary["country_code"]
        if ("full_name" in dictionary):
            a_place.full_name = dictionary["full_name"]
        if ("id" in dictionary):
            a_place.id = dictionary["id"]
        if ("name" in dictionary):
            a_place.name = dictionary["name"]
        if ("place_type" in dictionary):
            a_place.place_type = dictionary["place_type"]
        if ("url" in dictionary):
            a_place.url = dictionary["url"]
        return a_place

    @staticmethod
    def size(dictionary: dict) -> media.Size:
        a_size = media.Size()
        dictionary = Factory.casttodictionary(dictionary)
        if ("h" in dictionary):
            a_size.h = dictionary["h"]
        if ("resize" in dictionary):
            a_size.resize = dictionary["resize"]
        if ("w" in dictionary):
            a_size.w = dictionary["w"]
        return a_size

    @staticmethod
    def media(dictionary: dict) -> media.Media:
        a_media = media.Media();
        dictionary = Factory.casttodictionary(dictionary)
        if ("display_url" in dictionary):
            a_media.display_url = dictionary["display_url"]
        if ("expanded_url" in dictionary):
            a_media.expanded_url = dictionary["expanded_url"]
        if ("id" in dictionary):
            a_media.id = dictionary["id"]
        if ("media_url" in dictionary):
            a_media.media_url = dictionary["media_url"]
        if ("sizes" in dictionary):
            a_media.sizes = Factory.size(dictionary=dictionary["sizes"])
        if ("source_status_id" in dictionary):
            a_media.source_status_id = dictionary["source_status_id"]
        if ("type" in dictionary):
            a_media.type = dictionary["type"]
        if ("url" in dictionary):
            a_media.url = dictionary["url"]
        return a_media






