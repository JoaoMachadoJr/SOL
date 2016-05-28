__author__ = 'Joao'
class Tweet:
     def __init__(self, dictionary=dict()):
         self.annotations=""
         self.contributors=""
         self.coordinates=""
         self.created_at=""
         self.current_user_retweet=""
         self.entities=""
         self.favorite_count=""
         self.favorited=""
         self.filter_level=""
         self.id=""
         self.id_str=""
         self.in_reply_to_screen_name=""
         self.lang=""
         self.place=""
         self.possibly_sensitive=""
         self.quoted_status_id=""
         self.quoted_status_id_str=""
         self.quoted_status=""
         self.scopes=""
         self.retweet_count=""
         self.retweeted=""
         self.retweeted_status=""
         self.source=""
         self.text=""
         self.truncated=""
         self.user=""
         self.withheld_copyright=""
         self.withheld_in_countries=""
         self.withheld_scope=""
         if ("annotations" in dictionary):
             self.annotations=dictionary["annotations"]
         if ("contributors" in dictionary):
             self.contributors=dictionary["contributors"]
         if ("coordinates" in dictionary):
             self.coordinates=dictionary["coordinates"]
         if ("created_at" in dictionary):
             self.created_at=dictionary["created_at"]
         if ("current_user_retweet" in dictionary):
             self.current_user_retweet=dictionary["current_user_retweet"]
         if ("entities" in dictionary):
             self.entities=dictionary["entities"]
         if ("favorite_count" in dictionary):
             self.favorite_count=dictionary["favorite_count"]
         if ("favorited" in dictionary):
             self.favorited=dictionary["favorited"]
         if ("filter_level" in dictionary):
             self.filter_level=dictionary["filter_level"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("in_reply_to_screen_name" in dictionary):
             self.in_reply_to_screen_name=dictionary["in_reply_to_screen_name"]
         if ("lang" in dictionary):
             self.lang=dictionary["lang"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("possibly_sensitive" in dictionary):
             self.possibly_sensitive=dictionary["possibly_sensitive"]
         if ("quoted_status_id" in dictionary):
             self.quoted_status_id=dictionary["quoted_status_id"]
         if ("quoted_status_id_str" in dictionary):
             self.quoted_status_id_str=dictionary["quoted_status_id_str"]
         if ("quoted_status" in dictionary):
             self.quoted_status=dictionary["quoted_status"]
         if ("scopes" in dictionary):
             self.scopes=dictionary["scopes"]
         if ("retweet_count" in dictionary):
             self.retweet_count=dictionary["retweet_count"]
         if ("retweeted" in dictionary):
             self.retweeted=dictionary["retweeted"]
         if ("retweeted_status" in dictionary):
             self.retweeted_status=dictionary["retweeted_status"]
         if ("source" in dictionary):
             self.source=dictionary["source"]
         if ("text" in dictionary):
             self.text=dictionary["text"]
         if ("truncated" in dictionary):
             self.truncated=dictionary["truncated"]
         if ("user" in dictionary):
             self.user=dictionary["user"]
         if ("withheld_copyright" in dictionary):
             self.withheld_copyright=dictionary["withheld_copyright"]
         if ("withheld_in_countries" in dictionary):
             self.withheld_in_countries=dictionary["withheld_in_countries"]
         if ("withheld_scope" in dictionary):
             self.withheld_scope=dictionary["withheld_scope"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "TWEET: "+str(dic)