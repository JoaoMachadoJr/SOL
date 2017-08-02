__author__ = 'Joao'
import SolFB._Post_Facebook as _Post_Facebook
from  SolFB._Utility import Utility as _Utility
from  SolFB import _Actions
import requests
from dateutil.parser import parse
import SolFB._Cover_Photo as _Cover_Photo
import SolFB._Albums as _Albums
import SolFB._Events as _Events
import SolFB._Live_Videos as _Live_Videos
import SolFB._Photo as _Photo
import SolFB._Video as _Video
import SolFB._Life_Event as _Life_Event


class Page:
     def __init__(self, id="",dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/
         '''
         self.id=id
         self.about=""
         self.access_token=""
         self.ad_campaign=""
         self.affiliation=""
         self.app_id=""
         self.access_token=""
         self.app_links=""
         self.artists_we_like=""
         self.attire=""
         self.awards=""
         self.band_interests=""
         self.band_members=""
         self.best_page=""
         self.bio=""
         self.birthday=""
         self.booking_agent=""
         self.built=""
         self.business=""
         self.can_checkin=""
         self.can_post=""
         self.category=""
         self.category_list=""
         self.checkins=""
         self.company_overview=""
         self.contact_address=""
         self.country_page_likes=""
         self.cover=""
         self.culinary_team=""
         self.current_location=""
         self.description=""
         self.description_html=""
         self.directed_by=""
         self.display_subtext=""
         self.emails=""
         self.features=""
         self.featured_video=""
         self.food_styles=""
         self.founded=""
         self.general_info=""
         self.general_manager=""
         self.genre=""
         self.global_brand_page_name=""
         self.global_brand_root_id=""
         self.has_added_app=""
         self.hometown=""
         self.hours=""
         self.influences=""
         self.is_community_page=""
         self.is_permanently_closed=""
         self.is_published=""
         self.is_unclaimed=""
         self.is_verified=""
         self.last_used_time=""
         self.leadgen_tos_accepted=""
         self.link=""
         self.location=""
         self.members=""
         self.mission=""
         self.mpg=""
         self.name=""
         self.network=""
         self.new_like_count=""
         self.offer_eligible=""
         self.owner_business=""
         self.parent_page=""
         self.parking=""
         self.payment_options=""
         self.personal_info=""
         self.personal_interests=""
         self.pharma_safety_info=""
         self.phone=""
         self.place_type=""
         self.plot_outline=""
         self.press_contact=""
         self.price_range=""
         self.produced_by=""
         self.products=""
         self.promotion_eligible=""
         self.promotion_ineligible_reason=""
         self.public_transit=""
         self.record_label=""
         self.release_date=""
         self.restaurant_services=""
         self.restaurant_specialties=""
         self.schedule=""
         self.screenplay_by=""
         self.season=""
         self.single_line_address=""
         self.starring=""
         self.store_number=""
         self.studio=""
         self.talking_about_count=""
         self.unread_message_count=""
         self.unread_notif_count=""
         self.unseen_message_count=""
         self.username=""
         self.voip_info=""
         self.website=""
         self.were_here_count=""
         self.written_by=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("about" in dictionary):
             self.about=dictionary["about"]
         if ("access_token" in dictionary):
             self.access_token=dictionary["access_token"]
         if ("ad_campaign" in dictionary):
             self.ad_campaign=dictionary["ad_campaign"]
         if ("affiliation" in dictionary):
             self.affiliation=dictionary["affiliation"]
         if ("app_id" in dictionary):
             self.app_id=dictionary["app_id"]
         if ("app_links" in dictionary):
             self.app_links=dictionary["app_links"]
         if ("artists_we_like" in dictionary):
             self.artists_we_like=dictionary["artists_we_like"]
         if ("attire" in dictionary):
             self.attire=dictionary["attire"]
         if ("awards" in dictionary):
             self.awards=dictionary["awards"]
         if ("band_interests" in dictionary):
             self.band_interests=dictionary["band_interests"]
         if ("band_members" in dictionary):
             self.band_members=dictionary["band_members"]
         if ("best_page" in dictionary):
             self.best_page=Page(dictionary=dictionary["best_page"])
         if ("bio" in dictionary):
             self.bio=dictionary["bio"]
         if ("birthday" in dictionary):
             self.birthday=dictionary["birthday"]
         if ("booking_agent" in dictionary):
             self.booking_agent=dictionary["booking_agent"]
         if ("built" in dictionary):
             self.built=dictionary["built"]
         if ("business" in dictionary):
             self.business=dictionary["business"]
         if ("can_checkin" in dictionary):
             self.can_checkin=dictionary["can_checkin"]
         if ("can_post" in dictionary):
             self.can_post=dictionary["can_post"]
         if ("category" in dictionary):
             self.category=dictionary["category"]
         if ("category_list" in dictionary):
             self.category_list=dictionary["category_list"]
         if ("checkins" in dictionary):
             self.checkins=dictionary["checkins"]
         if ("company_overview" in dictionary):
             self.company_overview=dictionary["company_overview"]
         if ("contact_address" in dictionary):
             self.contact_address=dictionary["contact_address"]
         if ("country_page_likes" in dictionary):
             self.country_page_likes=dictionary["country_page_likes"]
         if ("cover" in dictionary):
             self.cover=_Cover_Photo.Cover_Photo(dictionary=dictionary["cover"])
         if ("culinary_team" in dictionary):
             self.culinary_team=dictionary["culinary_team"]
         if ("current_location" in dictionary):
             self.current_location=dictionary["current_location"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("description_html" in dictionary):
             self.description_html=dictionary["description_html"]
         if ("directed_by" in dictionary):
             self.directed_by=dictionary["directed_by"]
         if ("display_subtext" in dictionary):
             self.display_subtext=dictionary["display_subtext"]
         if ("emails" in dictionary):
             self.emails=dictionary["emails"]
         if ("features" in dictionary):
             self.features=dictionary["features"]
         if ("featured_video" in dictionary):
             self.featured_video=_Video.Video(dictionary=dictionary["featured_video"])
         if ("food_styles" in dictionary):
             self.food_styles=dictionary["food_styles"]
         if ("founded" in dictionary):
             self.founded=dictionary["founded"]
         if ("general_info" in dictionary):
             self.general_info=dictionary["general_info"]
         if ("general_manager" in dictionary):
             self.general_manager=dictionary["general_manager"]
         if ("genre" in dictionary):
             self.genre=dictionary["genre"]
         if ("global_brand_page_name" in dictionary):
             self.global_brand_page_name=dictionary["global_brand_page_name"]
         if ("global_brand_root_id" in dictionary):
             self.global_brand_root_id=dictionary["global_brand_root_id"]
         if ("has_added_app" in dictionary):
             self.has_added_app=dictionary["has_added_app"]
         if ("hometown" in dictionary):
             self.hometown=dictionary["hometown"]
         if ("hours" in dictionary):
             self.hours=dictionary["hours"]
         if ("influences" in dictionary):
             self.influences=dictionary["influences"]
         if ("is_community_page" in dictionary):
             self.is_community_page=dictionary["is_community_page"]
         if ("is_permanently_closed" in dictionary):
             self.is_permanently_closed=dictionary["is_permanently_closed"]
         if ("is_published" in dictionary):
             self.is_published=dictionary["is_published"]
         if ("is_unclaimed" in dictionary):
             self.is_unclaimed=dictionary["is_unclaimed"]
         if ("is_verified" in dictionary):
             self.is_verified=dictionary["is_verified"]
         if ("last_used_time" in dictionary):
             self.last_used_time=dictionary["last_used_time"]
         if ("leadgen_tos_accepted" in dictionary):
             self.leadgen_tos_accepted=dictionary["leadgen_tos_accepted"]
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("location" in dictionary):
             self.location=dictionary["location"]
         if ("members" in dictionary):
             self.members=dictionary["members"]
         if ("mission" in dictionary):
             self.mission=dictionary["mission"]
         if ("mpg" in dictionary):
             self.mpg=dictionary["mpg"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("network" in dictionary):
             self.network=dictionary["network"]
         if ("new_like_count" in dictionary):
             self.new_like_count=dictionary["new_like_count"]
         if ("offer_eligible" in dictionary):
             self.offer_eligible=dictionary["offer_eligible"]
         if ("owner_business" in dictionary):
             self.owner_business=dictionary["owner_business"]
         if ("parent_page" in dictionary):
             self.parent_page=Page(dictionary=dictionary["parent_page"])
         if ("parking" in dictionary):
             self.parking=dictionary["parking"]
         if ("payment_options" in dictionary):
             self.payment_options=dictionary["payment_options"]
         if ("personal_info" in dictionary):
             self.personal_info=dictionary["personal_info"]
         if ("personal_interests" in dictionary):
             self.personal_interests=dictionary["personal_interests"]
         if ("pharma_safety_info" in dictionary):
             self.pharma_safety_info=dictionary["pharma_safety_info"]
         if ("phone" in dictionary):
             self.phone=dictionary["phone"]
         if ("place_type" in dictionary):
             self.place_type=dictionary["place_type"]
         if ("plot_outline" in dictionary):
             self.plot_outline=dictionary["plot_outline"]
         if ("press_contact" in dictionary):
             self.press_contact=dictionary["press_contact"]
         if ("price_range" in dictionary):
             self.price_range=dictionary["price_range"]
         if ("produced_by" in dictionary):
             self.produced_by=dictionary["produced_by"]
         if ("products" in dictionary):
             self.products=dictionary["products"]
         if ("promotion_eligible" in dictionary):
             self.promotion_eligible=dictionary["promotion_eligible"]
         if ("promotion_ineligible_reason" in dictionary):
             self.promotion_ineligible_reason=dictionary["promotion_ineligible_reason"]
         if ("public_transit" in dictionary):
             self.public_transit=dictionary["public_transit"]
         if ("record_label" in dictionary):
             self.record_label=dictionary["record_label"]
         if ("release_date" in dictionary):
             self.release_date=dictionary["release_date"]
         if ("restaurant_services" in dictionary):
             self.restaurant_services=dictionary["restaurant_services"]
         if ("restaurant_specialties" in dictionary):
             self.restaurant_specialties=dictionary["restaurant_specialties"]
         if ("schedule" in dictionary):
             self.schedule=dictionary["schedule"]
         if ("screenplay_by" in dictionary):
             self.screenplay_by=dictionary["screenplay_by"]
         if ("season" in dictionary):
             self.season=dictionary["season"]
         if ("single_line_address" in dictionary):
             self.single_line_address=dictionary["single_line_address"]
         if ("starring" in dictionary):
             self.starring=dictionary["starring"]
         if ("store_number" in dictionary):
             self.store_number=dictionary["store_number"]
         if ("studio" in dictionary):
             self.studio=dictionary["studio"]
         if ("talking_about_count" in dictionary):
             self.talking_about_count=dictionary["talking_about_count"]
         if ("unread_message_count" in dictionary):
             self.unread_message_count=dictionary["unread_message_count"]
         if ("unread_notif_count" in dictionary):
             self.unread_notif_count=dictionary["unread_notif_count"]
         if ("unseen_message_count" in dictionary):
             self.unseen_message_count=dictionary["unseen_message_count"]
         if ("username" in dictionary):
             self.username=dictionary["username"]
         if ("voip_info" in dictionary):
             self.voip_info=dictionary["voip_info"]
         if ("website" in dictionary):
             self.website=dictionary["website"]
         if ("were_here_count" in dictionary):
             self.were_here_count=dictionary["were_here_count"]
         if ("written_by" in dictionary):
             self.written_by=dictionary["written_by"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]

     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "PAGE: "+str(dict)


     def getAdmin_Notes(self,Pagetoken=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/admin_notes/
         '''
         if (Pagetoken==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (Pagetoken==None):
            Pagetoken=self.access_token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/admin_notes?&access_token="+Pagetoken, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getAlbums(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/albums/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/albums?fields=id,can_upload,count,cover_photo,created_time,description,event,from,link,location,name,place,privacy,type,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Albums.Albums(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def postAlbum(self,token=None, name="MyAlbum", message="", timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/albums/
         '''
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         params={"message":message,"name":name}
         r=_Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/"+self.id+"/albums?access_token="+token,params=params, timeout=timeout).json()
         return r

     def getBlocked(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/blocked/
         '''
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/blocked?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getLikesCount(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/insights/
         '''
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/insights/page_fans/lifetime?&access_token="+token, timeout=timeout).json()
         return r["data"][0]["values"][0]["value"]

     def getEvents(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/events/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/events?fields=id,can_guests_invite,cover,description,end_time,guest_list_enabled,is_page_owned,is_viewer_admin,name,owner,parent_group,start_time,ticket_uri,timezone,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Events.Events(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista


     def getGlobal_Brand_Children(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/global_brand_children/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Global_Brand_Children?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Page(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getInstagram_Accounts(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/instagram_accounts/
         '''
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Instagram_Accounts?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista


     def getLikedPages(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/likes/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/likes?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getLive_videos(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/live_videos/
         '''
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/live_videos?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Live_Videos.Live_Videos(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getLife_Events(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/milestones/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/milestones?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Life_Event.Life_Event(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getPhotos(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/photos/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Photo.Photo(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def postPhoto(self, token=None, Localpath=None, FileURL=None,message=" "):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/photos/
         '''
         if (token==None):
             token=_Actions.Actions.token
         if (Localpath==None and FileURL==None):
             raise Exception("You should use a LocalPath or a URL")
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
             files={'file':open(Localpath,'rb')}
             params={"description":message}
             s=requests.post(graphurl, files=files,params=params).json()
             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
             params={"description":message}
             params["file_url"]=FileURL
             return requests.post(graphurl,params=params).json()


     def getPicture(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/picture/
         '''
         if (token==None):
            token=_Actions.Actions.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Picture?fields=height,is_silhouette,url,width&redirect=0&type=large&access_token="+token, timeout=timeout).json()
         return r["data"]["url"]

     def getRoles(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/page/roles
         '''
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/roles?access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getVideos(self,token=None, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/videos/
         '''
         if (token==None):
            token=_Actions.Actions.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/videos?fields=backdated_time,backdated_time_granularity,id,created_time,description,embed_html,format,from,icon,is_instagram_eligible,length,permalink_url,picture,place,privacy,source,status,updated_time&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Video.Video(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

     def getPosts(self, token=None, dateMin="", dateMax="", limit=100, timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/page/feed
         '''
         if (token==None):
             token=_Actions.Actions.token

         params={}
         if (token == None):
            token = _Actions.Actions.token
         if (dateMin!="" and dateMax!="" and dateMin > dateMax):
            raise Exception("Cannot use dateMin > dateMax")
         if (dateMax != ""):
            params["until"]=dateMax

         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.5/"+self.id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=100&access_token="+token, timeout=timeout).json()
        # print(r)
         lista = list()
         while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                post=_Post_Facebook.Post_Facebook(dictionary=a)
                if ((len(lista)==limit) or (dateMin!="" and parse(post.created_time).replace(tzinfo=None)<dateMin)):
                    return lista
                lista.append(post)
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
         return lista

     def postPost (self,message=" ", token=None):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/v2.8/page/feed
         '''
         if (token==None):
             token=_Actions.Actions.token
         params={"message":message}
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?&access_token="+str(token)
         s=requests.post(url,params=params).json()
         return s

     def postVideo(self,message=" ", token=None, Localpath=None, FileURL=None):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/page/videos/
         '''
         if (token==None):
             token=_Actions.Actions.token
         if (Localpath==None and FileURL==None):
             raise Exception("You should use a LocalPath or a URL")
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):


             graphurl="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
             files={'file':open(Localpath,'rb')}
             params={"description":message}
             s=requests.post(graphurl, files=files,params=params).json()

             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
             params={"description":message}
             params["file_url"]=FileURL
             return requests.post(graphurl,params=params).json()
