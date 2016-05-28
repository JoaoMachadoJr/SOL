__author__ = 'Joao'
class User:
     def __init__(self, dictionary=dict()):
         self.contributors_enabled=""
         self.created_at=""
         self.default_profile=""
         self.default_profile_image=""
         self.description=""
         self.entities=""
         self.favourites_count=""
         self.follow_request_sent=""
         self.following=""
         self.followers_count=""
         self.friends_count=""
         self.geo_enabled=""
         self.id=""
         self.id_str=""
         self.is_translator=""
         self.lang=""
         self.listed_count=""
         self.location=""
         self.name=""
         self.notifications=""
         self.profile_background_color=""
         self.profile_background_image_url=""
         self.profile_background_image_url_https=""
         self.profile_background_tile=""
         self.profile_banner_url=""
         self.profile_image_url=""
         self.profile_image_url_https=""
         self.profile_link_color=""
         self.profile_sidebar_border_color=""
         self.profile_sidebar_fill_color=""
         self.profile_text_color=""
         self.profile_use_background_image=""
         self.protected=""
         self.screen_name=""
         self.show_all_inline_media=""
         self.status=""
         self.statuses_count=""
         self.time_zone=""
         self.url=""
         self.utc_offset=""
         self.verified=""
         self.withheld_in_countries=""
         self.withheld_scope=""
         if ("contributors_enabled" in dictionary):
             self.contributors_enabled=dictionary["contributors_enabled"]
         if ("created_at" in dictionary):
             self.created_at=dictionary["created_at"]
         if ("default_profile" in dictionary):
             self.default_profile=dictionary["default_profile"]
         if ("default_profile_image" in dictionary):
             self.default_profile_image=dictionary["default_profile_image"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("entities" in dictionary):
             self.entities=dictionary["entities"]
         if ("favourites_count" in dictionary):
             self.favourites_count=dictionary["favourites_count"]
         if ("follow_request_sent" in dictionary):
             self.follow_request_sent=dictionary["follow_request_sent"]
         if ("following" in dictionary):
             self.following=dictionary["following"]
         if ("followers_count" in dictionary):
             self.followers_count=dictionary["followers_count"]
         if ("friends_count" in dictionary):
             self.friends_count=dictionary["friends_count"]
         if ("geo_enabled" in dictionary):
             self.geo_enabled=dictionary["geo_enabled"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("is_translator" in dictionary):
             self.is_translator=dictionary["is_translator"]
         if ("lang" in dictionary):
             self.lang=dictionary["lang"]
         if ("listed_count" in dictionary):
             self.listed_count=dictionary["listed_count"]
         if ("location" in dictionary):
             self.location=dictionary["location"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("notifications" in dictionary):
             self.notifications=dictionary["notifications"]
         if ("profile_background_color" in dictionary):
             self.profile_background_color=dictionary["profile_background_color"]
         if ("profile_background_image_url" in dictionary):
             self.profile_background_image_url=dictionary["profile_background_image_url"]
         if ("profile_background_image_url_https" in dictionary):
             self.profile_background_image_url_https=dictionary["profile_background_image_url_https"]
         if ("profile_background_tile" in dictionary):
             self.profile_background_tile=dictionary["profile_background_tile"]
         if ("profile_banner_url" in dictionary):
             self.profile_banner_url=dictionary["profile_banner_url"]
         if ("profile_image_url" in dictionary):
             self.profile_image_url=dictionary["profile_image_url"]
         if ("profile_image_url_https" in dictionary):
             self.profile_image_url_https=dictionary["profile_image_url_https"]
         if ("profile_link_color" in dictionary):
             self.profile_link_color=dictionary["profile_link_color"]
         if ("profile_sidebar_border_color" in dictionary):
             self.profile_sidebar_border_color=dictionary["profile_sidebar_border_color"]
         if ("profile_sidebar_fill_color" in dictionary):
             self.profile_sidebar_fill_color=dictionary["profile_sidebar_fill_color"]
         if ("profile_text_color" in dictionary):
             self.profile_text_color=dictionary["profile_text_color"]
         if ("profile_use_background_image" in dictionary):
             self.profile_use_background_image=dictionary["profile_use_background_image"]
         if ("protected" in dictionary):
             self.protected=dictionary["protected"]
         if ("screen_name" in dictionary):
             self.screen_name=dictionary["screen_name"]
         if ("show_all_inline_media" in dictionary):
             self.show_all_inline_media=dictionary["show_all_inline_media"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("statuses_count" in dictionary):
             self.statuses_count=dictionary["statuses_count"]
         if ("time_zone" in dictionary):
             self.time_zone=dictionary["time_zone"]
         if ("url" in dictionary):
             self.url=dictionary["url"]
         if ("utc_offset" in dictionary):
             self.utc_offset=dictionary["utc_offset"]
         if ("verified" in dictionary):
             self.verified=dictionary["verified"]
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
         return "USER: "+str(dic)