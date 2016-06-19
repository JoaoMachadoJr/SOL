__author__ = 'Joao'
import _Media
import _URL
import _User_Mention
import _Hashtags
import _Utils

class Entity:
    def __init__(self, dictionary=dict()):
        dictionary=_Utils.CastToDictionary(dictionary)
        dictionary=_Utils.removeEmptyFields(dictionary)
        self.hashtags = list()
        self.media = list()
        self.urls = list()
        self.user_mentions = list()
        if ("hashtags" in dictionary):
            for hash in dictionary["hashtags"]:
                self.hashtags.append(_Hashtags.Hashtags(dictionary=hash))
        if ("media" in dictionary):
            for m in dictionary["media"]:
                self.media.append(_Media.Media(dictionary=m))
        if ("urls" in dictionary):
            for url in dictionary["urls"]:
                self.urls.append(_URL.URL(dictionary=url))
        if ("user_mentions" in dictionary):
            for mention in dictionary["user_mentions"]:
                self.user_mentions.append(_User_Mention.User_Mention(dictionary=mention))

    def __str__(self):
        dic = self.__dict__
        lista = list()
        for key in dic:
            lista.append(key)
        for key in lista:
            if dic[key] == None or dic[key] == "":
                del dic[key]
        return "ENTITY: " + str(dic)