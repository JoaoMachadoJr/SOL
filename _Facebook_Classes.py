__author__ = 'Joao'
import _User_Facebook
import requests
import _Settings
import os
import _Post_Facebook

class Feed_Targeting:
    def __init__(self, dictionary=None):
        self.age_max=""
        self.age_min=""
        self.genders=""
        self.geo_locations=""
        self.locales=""
        self.education_statuses=""
        self.fan_of=""
        self.relationship_statuses=""
        if (dictionary!=None):
            if "age_max" in dictionary:
                self.age_max=dictionary["age_max"]
            if "age_min" in dictionary:
                self.age_min=dictionary["age_min"]
            if "genders" in dictionary:
                self.genders=dictionary["genders"]
            if "geo_locations" in dictionary:
                self.geo_locations=dictionary["geo_locations"]
            if "locales" in dictionary:
                self.locales=dictionary["locales"]
            if "education_statuses" in dictionary:
                self.education_statuses=dictionary["education_statuses"]
            if "fan_of" in dictionary:
                self.fan_of=dictionary["fan_of"]
            if "relationship_statuses" in dictionary:
                self.relationship_statuses=dictionary["relationship_statuses"]

    def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "FEED_TARGETING: "+str(dic)

class Place:
    def __init__(self, dictionary=dict()):
        self.name=""
        self.latitude=""
        self.longitude=""
        self.id=""
        if "name" in dictionary:
            self.name=dictionary["name"]
        if "location" in dictionary:
            self.latitude=dictionary["location"]["latitude"]
            self.longitude=dictionary["location"]["longitude"]
        if "id" in dictionary:
            self.id=dictionary["id"]
    def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "PLACE: "+str(dic)

class Privacy:
    def __init__(self, dictionary=dict()):
        self.allow=""
        self.deny=""
        self.value=""
        self.friends=list()
        self.description=""
        self.properties=""
        if "allow" in dictionary:
            self.allow=dictionary["allow"]
        if "deny" in dictionary:
            self.deny=dictionary["deny"]
        if "value" in dictionary:
            self.value=dictionary["value"]
        if "friends" in dictionary:
            self.friends=dictionary["friends"]
        if "description" in dictionary:
            self.description=dictionary["description"]


    def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "PRIVACY: "+str(dic)

class Targeting:
    def __init__(self, dictionary=dict()):
        self.countries=list()
        self.locales=list()
        self.regions=""
        self.cities=list()
        self.description=""
        self.properties=""
        if "countries" in dictionary:
            self.countries=dictionary["countries"]
        if "locales" in dictionary:
            self.locales=dictionary["locales"]
        if "regions" in dictionary:
            self.value=dictionary["value"]
        if "cities" in dictionary:
            self.friends=dictionary["friends"]


    def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "TARGETING: "+str(dic)

class Accounts:
    def __init__(self, dictionary=""):
        self.name=""
        self.perms=list()
        self.id=""
        self.access_token=""
        self.category=""
        if (dictionary!=""):
            self.id=dictionary["id"]
            self.perms=dictionary["perms"]
            self.name=dictionary["name"]
            self.access_token=dictionary["access_token"]
            self.category=dictionary["category"]

    def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ACCOUNTS: "+str(dic)
class Achievements:
    def __init__(self, dictionary=dict()):
        self.id=""
        self.application=""
        self.data=""
        self.end_time=""
        self.from_=""
        self.image=""
        self.is_explicitly_shared=""
        self.message=""
        self.message_tags=""
        self.no_feed_story=""
        self.photos=""
        self.place=""
        self.publish_time=""
        self.ref=""
        self.start_time=""
        self.tags=""
        self.type=""
        if ("id" in dictionary):
            self.id=dictionary["id"]
        if ("application" in dictionary):
            self.application=dictionary["application"]
        if ("data" in dictionary):
            self.data="data"
        if ("end_time" in dictionary):
            self.end_time=dictionary["end_time"]
        if ("from" in dictionary):
            self.from_=_User_Facebook.User_Facebook(dictionary=dictionary["from"])
        if ("image" in dictionary):
            self.image=dictionary["image"]
        if ("is_explicitly_shared" in dictionary):
            self.is_explicitly_shared=dictionary["is_explicitly_shared"]
        if ("message" in dictionary):
            self.message=dictionary["message"]
        if ("message_tags" in dictionary):
            self.message_tags=dictionary["message_tags"]
        if ("no_feed_story" in dictionary):
            self.no_feed_story=dictionary["no_feed_story"]
        if ("photos" in dictionary):
            self.photos=dictionary["photos"]
        if ("place" in dictionary):
            self.place=Place(dictionary["place"])
        if ("publish_time" in dictionary):
            self.publish_time=dictionary["publish_time"]
        if ("ref" in dictionary):
            self.ref=dictionary["ref"]
        if ("start_time" in dictionary):
            self.start_time=dictionary["start_time"]
        if ("tags" in dictionary):
            self.tags=dictionary["tags"]
        if ("type" in dictionary):
            self.type=dictionary["type"]

    def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ARCHIEVEMENT: "+str(dic)

    def getComments(self,token=None):
         if (token==None):
            token=_Settings.token

         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_hide,can_like,can_reply_privately,comment_count,created_time,from,like_count,message,message_tags,object,parent,private_reply_conversation,user_likes,message,is_hidden&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Comment(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

    def getLikes(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista


    def postComment(self, message, token):
        if (token==None):
            token=_Settings.token
        r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/comments?message=\""+message+"\"&access_token="+token).json()

class Adaccountgroups:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.account_group_id=""
         self.accounts=""
         self.name=""
         self.status=""
         self.users=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("account_group_id" in dictionary):
             self.account_group_id=dictionary["account_group_id"]
         if ("accounts" in dictionary):
             self.accounts=dictionary["accounts"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("users" in dictionary):
             self.users=dictionary["users"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ADACCOUNTGROUP: "+str(dic)

class Adaccounts:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.account_groups=""
         self.account_id=""
         self.account_status=""
         self.age=""
         self.agency_client_declaration=""
         self.amount_spent=""
         self.balance=""
         self.business=""
         self.business_city=""
         self.business_country_code=""
         self.business_name=""
         self.business_state=""
         self.business_street=""
         self.business_street2=""
         self.business_zip=""
         self.can_create_brand_lift_study=""
         self.capabilities=""
         self.created_time=""
         self.currency=""
         self.end_advertiser_name=""
         self.failed_delivery_checks=""
         self.funding_source=""
         self.funding_source_details=""
         self.has_migrated_permissions=""
         self.end_advertiser=""
         self.disable_reason=""
         self.io_number=""
         self.is_notifications_enabled=""
         self.is_personal=""
         self.is_prepay_account=""
         self.is_tax_id_required=""
         self.last_used_time=""
         self.line_numbers=""
         self.media_agency=""
         self.min_campaign_group_spend_cap=""
         self.min_daily_budget=""
         self.name=""
         self.offsite_pixels_tos_accepted=""
         self.owner=""
         self.owner_business=""
         self.partner=""
         self.rf_spec=""
         self.spend_cap=""
         self.tax_id=""
         self.tax_id_status=""
         self.tax_id_type=""
         self.timezone_id=""
         self.timezone_name=""
         self.timezone_offset_hours_utc=""
         self.tos_accepted=""
         self.user_role=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("account_groups" in dictionary):
             self.account_groups=dictionary["account_groups"]
         if ("account_id" in dictionary):
             self.account_id=dictionary["account_id"]
         if ("account_status" in dictionary):
             self.account_status=dictionary["account_status"]
         if ("age" in dictionary):
             self.age=dictionary["age"]
         if ("agency_client_declaration" in dictionary):
             self.agency_client_declaration=dictionary["agency_client_declaration"]
         if ("amount_spent" in dictionary):
             self.amount_spent=dictionary["amount_spent"]
         if ("balance" in dictionary):
             self.balance=dictionary["balance"]
         if ("business" in dictionary):
             self.business=dictionary["business"]
         if ("business_city" in dictionary):
             self.business_city=dictionary["business_city"]
         if ("business_country_code" in dictionary):
             self.business_country_code=dictionary["business_country_code"]
         if ("business_name" in dictionary):
             self.business_name=dictionary["business_name"]
         if ("business_state" in dictionary):
             self.business_state=dictionary["business_state"]
         if ("business_street" in dictionary):
             self.business_street=dictionary["business_street"]
         if ("business_street2" in dictionary):
             self.business_street2=dictionary["business_street2"]
         if ("business_zip" in dictionary):
             self.business_zip=dictionary["business_zip"]
         if ("can_create_brand_lift_study" in dictionary):
             self.can_create_brand_lift_study=dictionary["can_create_brand_lift_study"]
         if ("capabilities" in dictionary):
             self.capabilities=dictionary["capabilities"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("currency" in dictionary):
             self.currency=dictionary["currency"]
         if ("end_advertiser_name" in dictionary):
             self.end_advertiser_name=dictionary["end_advertiser_name"]
         if ("failed_delivery_checks" in dictionary):
             self.failed_delivery_checks=dictionary["failed_delivery_checks"]
         if ("funding_source" in dictionary):
             self.funding_source=dictionary["funding_source"]
         if ("funding_source_details" in dictionary):
             self.funding_source_details=dictionary["funding_source_details"]
         if ("has_migrated_permissions" in dictionary):
             self.has_migrated_permissions=dictionary["has_migrated_permissions"]
         if ("end_advertiser" in dictionary):
             self.end_advertiser=dictionary["end_advertiser"]
         if ("disable_reason" in dictionary):
             self.disable_reason=dictionary["disable_reason"]
         if ("io_number" in dictionary):
             self.io_number=dictionary["io_number"]
         if ("is_notifications_enabled" in dictionary):
             self.is_notifications_enabled=dictionary["is_notifications_enabled"]
         if ("is_personal" in dictionary):
             self.is_personal=dictionary["is_personal"]
         if ("is_prepay_account" in dictionary):
             self.is_prepay_account=dictionary["is_prepay_account"]
         if ("is_tax_id_required" in dictionary):
             self.is_tax_id_required=dictionary["is_tax_id_required"]
         if ("last_used_time" in dictionary):
             self.last_used_time=dictionary["last_used_time"]
         if ("line_numbers" in dictionary):
             self.line_numbers=dictionary["line_numbers"]
         if ("media_agency" in dictionary):
             self.media_agency=dictionary["media_agency"]
         if ("min_campaign_group_spend_cap" in dictionary):
             self.min_campaign_group_spend_cap=dictionary["min_campaign_group_spend_cap"]
         if ("min_daily_budget" in dictionary):
             self.min_daily_budget=dictionary["min_daily_budget"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("offsite_pixels_tos_accepted" in dictionary):
             self.offsite_pixels_tos_accepted=dictionary["offsite_pixels_tos_accepted"]
         if ("owner" in dictionary):
             self.owner=dictionary["owner"]
         if ("owner_business" in dictionary):
             self.owner_business=dictionary["owner_business"]
         if ("partner" in dictionary):
             self.partner=dictionary["partner"]
         if ("rf_spec" in dictionary):
             self.rf_spec=dictionary["rf_spec"]
         if ("spend_cap" in dictionary):
             self.spend_cap=dictionary["spend_cap"]
         if ("tax_id" in dictionary):
             self.tax_id=dictionary["tax_id"]
         if ("tax_id_status" in dictionary):
             self.tax_id_status=dictionary["tax_id_status"]
         if ("tax_id_type" in dictionary):
             self.tax_id_type=dictionary["tax_id_type"]
         if ("timezone_id" in dictionary):
             self.timezone_id=dictionary["timezone_id"]
         if ("timezone_name" in dictionary):
             self.timezone_name=dictionary["timezone_name"]
         if ("timezone_offset_hours_utc" in dictionary):
             self.timezone_offset_hours_utc=dictionary["timezone_offset_hours_utc"]
         if ("tos_accepted" in dictionary):
             self.tos_accepted=dictionary["tos_accepted"]
         if ("user_role" in dictionary):
             self.user_role=dictionary["user_role"]
     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ADACCOUNTS: "+str(dic)

class Adcontracts:
     def __init__(self, dictionary=dict()):
         self.account_id=""
         self.account_mgr_fbid=""
         self.account_mgr_name=""
         self.adops_person_name=""
         self.advertiser_name=""
         self.agency_name=""
         self.campaign_name=""
         self.created_by=""
         self.created_date=""
         self.io_number=""
         self.io_type=""
         self.last_updated_by=""
         self.last_updated_date=""
         self.max_end_date=""
         self.mdc_fbid=""
         self.min_start_date=""
         self.salesrep_fbid=""
         self.salesrep_name=""
         self.status=""
         self.subvertical=""
         self.thirdparty_billed=""
         self.thirdparty_password=""
         self.thirdparty_uid=""
         self.thirdparty_url=""
         self.version=""
         self.vertical=""
         if ("account_id" in dictionary):
             self.account_id=dictionary["account_id"]
         if ("account_mgr_fbid" in dictionary):
             self.account_mgr_fbid=dictionary["account_mgr_fbid"]
         if ("account_mgr_name" in dictionary):
             self.account_mgr_name=dictionary["account_mgr_name"]
         if ("adops_person_name" in dictionary):
             self.adops_person_name=dictionary["adops_person_name"]
         if ("advertiser_name" in dictionary):
             self.advertiser_name=dictionary["advertiser_name"]
         if ("agency_name" in dictionary):
             self.agency_name=dictionary["agency_name"]
         if ("campaign_name" in dictionary):
             self.campaign_name=dictionary["campaign_name"]
         if ("created_by" in dictionary):
             self.created_by=dictionary["created_by"]
         if ("created_date" in dictionary):
             self.created_date=dictionary["created_date"]
         if ("io_number" in dictionary):
             self.io_number=dictionary["io_number"]
         if ("io_type" in dictionary):
             self.io_type=dictionary["io_type"]
         if ("last_updated_by" in dictionary):
             self.last_updated_by=dictionary["last_updated_by"]
         if ("last_updated_date" in dictionary):
             self.last_updated_date=dictionary["last_updated_date"]
         if ("max_end_date" in dictionary):
             self.max_end_date=dictionary["max_end_date"]
         if ("mdc_fbid" in dictionary):
             self.mdc_fbid=dictionary["mdc_fbid"]
         if ("min_start_date" in dictionary):
             self.min_start_date=dictionary["min_start_date"]
         if ("salesrep_fbid" in dictionary):
             self.salesrep_fbid=dictionary["salesrep_fbid"]
         if ("salesrep_name" in dictionary):
             self.salesrep_name=dictionary["salesrep_name"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("subvertical" in dictionary):
             self.subvertical=dictionary["subvertical"]
         if ("thirdparty_billed" in dictionary):
             self.thirdparty_billed=dictionary["thirdparty_billed"]
         if ("thirdparty_password" in dictionary):
             self.thirdparty_password=dictionary["thirdparty_password"]
         if ("thirdparty_uid" in dictionary):
             self.thirdparty_uid=dictionary["thirdparty_uid"]
         if ("thirdparty_url" in dictionary):
             self.thirdparty_url=dictionary["thirdparty_url"]
         if ("version" in dictionary):
             self.version=dictionary["version"]
         if ("vertical" in dictionary):
             self.vertical=dictionary["vertical"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ADCONTRACTS: "+str(dic)

class Group:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.cover=""
         self.description=""
         self.email=""
         self.icon=""
         self.link=""
         self.member_request_count=""
         self.name=""
         self.owner=""
         self.parent=""
         self.privacy=""
         self.updated_time=""
         self.cover_url=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("cover" in dictionary):
             self.cover=Cover_Photo(dictionary["cover"])
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("email" in dictionary):
             self.email=dictionary["email"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("member_request_count" in dictionary):
             self.member_request_count=dictionary["member_request_count"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("owner" in dictionary):
             self.owner=dictionary["owner"]
         if ("parent" in dictionary):
             self.parent=dictionary["parent"]
         if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("cover_url" in dictionary):
             self.cover_url=dictionary["cover_url"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "GROUP: "+str(dic)

     def getAdmins(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/admins?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getDocs(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/docs?fields=id,from,subject,message,icon,created_time,updated_time,revision,can_edit,can_delete&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Group_Doc(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getEvents(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/docs?fields=id,can_guests_invite,cover,description,end_time,guest_list_enabled,is_page_owned,is_viewer_admin,name,owner,parent_group,start_time,ticket_uri,timezone,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Events(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getAlbums(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/albums?fields=id,can_upload,count,cover_photo,created_time,description,event,from,link,location,name,place,privacy,type,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Albums(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getFiles(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/files?fields=id,from,group,download_link,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getPosts(self, token=None, dateMin="", dateMax="", limit=100):
         if (token==None):
             token=_Settings.token
         i=0
         while (i<100):
                     try:
                          r=requests.get("https://graph.facebook.com/v2.5/"+self.id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=100&access_token="+token,timeout=(5,5)).json()
                          break
                     except:
                          i=i+1
         lista=list()
         while ("data" in r and len(r["data"])>0):

             for a in r["data"]:
                 lista.append(_Post_Facebook.Post_Facebook(a))
             if ("next" in r["paging"]):

                 i=0
                 while (i<100):

                     try:
                         r=requests.get(r["paging"]["next"], timeout=(5,5)).json()
                         break
                     except:
                         i=i+1

             else:
                 break
         return lista

     def postPost (self,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?message="+message+"&access_token="+str(token)
         s=requests.post(url).json()
         return s

     def getMembers(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/members?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getPhotos(self, token=None):
         if (token==None):
             token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Photos?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Photo(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def postPhoto(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"message":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)
         return s

     def getVideos(self, token=None):
         if (token==None):
             token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Videos?fields=id,created_time,description,embed_html,format,from,icon,picture,privacy,source,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Video(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista



     def postVideo(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token


         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"description":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)

         return s

class Photo:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.album=""
         self.backdated_time=""
         self.backdated_time_granularity=""
         self.can_delete=""
         self.can_tag=""
         self.created_time=""
         self.from_=""
         self.height=""
         self.icon=""
         self.images=""
         self.link=""
         self.name=""
         self.name_tags=""
         self.page_story_id=""
         self.picture=""
         self.place=""
         self.updated_time=""
         self.width=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("album" in dictionary):
             self.album=dictionary["album"]
         if ("backdated_time" in dictionary):
             self.backdated_time=dictionary["backdated_time"]
         if ("backdated_time_granularity" in dictionary):
             self.backdated_time_granularity=dictionary["backdated_time_granularity"]
         if ("can_delete" in dictionary):
             self.can_delete=dictionary["can_delete"]
         if ("can_tag" in dictionary):
             self.can_tag=dictionary["can_tag"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("height" in dictionary):
             self.height=dictionary["height"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("images" in dictionary):
             self.images=dictionary["images"]
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("name_tags" in dictionary):
             self.name_tags=dictionary["name_tags"]
         if ("page_story_id" in dictionary):
             self.page_story_id=dictionary["page_story_id"]
         if ("picture" in dictionary):
             self.picture=dictionary["picture"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("width" in dictionary):
             self.width=dictionary["width"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "PHOTO: "+str(dic)

     def getInfo(self, token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token).json()
         c=Photo(dictionary=r)
         return c;

     def delete(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token+"&method=delete").json()
         return str(r)

class Albums:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.can_upload=""
         self.count=""
         self.cover_photo=""
         self.created_time=""
         self.description=""
         self.event=""
         self.from_=""
         self.link=""
         self.location=""
         self.name=""
         self.place=""
         self.privacy=""
         self.type=""
         self.updated_time=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("can_upload" in dictionary):
             self.can_upload=dictionary["can_upload"]
         if ("count" in dictionary):
             self.count=dictionary["count"]
         if ("cover_photo" in dictionary):
             self.cover_photo=Photo(dictionary["cover_photo"])
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("event" in dictionary):
             self.event=Events(dictionary=dictionary["event"])
         if ("from" in dictionary):
             self.from_=_User_Facebook.User_Facebook(dictionary= dictionary["from"])
         if ("link" in dictionary):
             self.link=dictionary["link"]
         if ("location" in dictionary):
             self.location=dictionary["location"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
         if ("type" in dictionary):
             self.type=dictionary["type"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "ALBUMS: "+str(dic)

     def getPhotos(self, token=None):
         if (token==None):
             token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Photos?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Photo(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def postPhoto(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token


         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"message":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)
         return s

     def getLikes(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista
     def getComments(self,token=None):
         if (token==None):
            token=_Settings.token

         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Comment(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def postLike(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         return str(r)

     def postComment(self, message, token):
        if (token==None):
            token=_Settings.token
        r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/comments?message=\""+message+"\"&access_token="+token).json()


class Apprequests:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.action_type=""
         self.application=""
         self.created_time=""
         self.data=""
         self.from_=""
         self.message=""
         self.object=""
         self.to=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("action_type" in dictionary):
             self.action_type=dictionary["action_type"]
         if ("application" in dictionary):
             self.application=dictionary["application"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("data" in dictionary):
             self.data=dictionary["data"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("object" in dictionary):
             self.object=dictionary["object"]
         if ("to" in dictionary):
             self.to=dictionary["to"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "APREQUESTS: "+str(dic)

class Page:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.about=""
         self.access_token=""
         self.ad_campaign=""
         self.affiliation=""
         self.app_id=""
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
             self.best_page=Page(dictionary["best_page"])
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
             self.cover=Cover_Photo(dictionary["cover"])
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
             self.featured_video=Video(dictionary["featured_video"])
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
             self.parent_page=Page(dictionary["parent_page"])
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


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "PAGE: "+str(dic)


     def getAdminNotes(self,Pagetoken=None):
         if (Pagetoken==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (Pagetoken==None):
            Pagetoken=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/admin_notes?&access_token="+Pagetoken).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getAlbums(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/albums?fields=id,can_upload,count,cover_photo,created_time,description,event,from,link,location,name,place,privacy,type,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Albums(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def postAlbum(self,token=None, name="MyAlbum", message=""):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         params={"message":message,"name":name}
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/albums?access_token="+token,params=params).json()
         return r

     def getBlocked(self,token=None):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/blocked?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getEvents(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/events?fields=id,can_guests_invite,cover,description,end_time,guest_list_enabled,is_page_owned,is_viewer_admin,name,owner,parent_group,start_time,ticket_uri,timezone,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Events(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getFeatured_Videos_Collection(self,token=None):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/featured_videos_collection?fields=backdated_time,backdated_time_granularity,id,created_time,description,embed_html,format,from,icon,is_instagram_eligible,length,permalink_url,picture,place,privacy,source,status,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Video(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getGlobal_Brand_Children(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Global_Brand_Children?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Page(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getInstagram_Accounts(self,token=None):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Instagram_Accounts?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getInstant_Articles(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Instant_Articles?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getLabels(self,token=None):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/labels?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getLikedPages(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/likes?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getLive_videos(self,token=None):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/live_videos?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Live_Videos(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getLife_Events(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/milestones?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Life_Event(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getPhotos(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Photo(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def postPhoto(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"message":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)
         return s

     def getPicture(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Picture?fields=height,is_silhouette,url,width&redirect=0&type=large&access_token="+token).json()
         return r["data"]["url"]

     def getPlace_Topics(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/place_topics?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getRoles(self,token=None):
         if (token==None and (self.access_token=="" or self.access_token==None)):
             raise Exception("This action requires a page token")
         if (token==None):
            token=self.access_token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/roles?access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getVideos(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/videos?fields=backdated_time,backdated_time_granularity,id,created_time,description,embed_html,format,from,icon,is_instagram_eligible,length,permalink_url,picture,place,privacy,source,status,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Video(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getPosts(self, token=None, dateMin="", dateMax="", limit=100):
         if (token==None):
             token=_Settings.token
         i=0
         while (i<100):
                     try:
                          r=requests.get("https://graph.facebook.com/v2.5/"+self.id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=100&access_token="+token,timeout=(5,5)).json()
                          break
                     except:
                          i=i+1
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Post_Facebook.Post_Facebook(a))
             if ("next" in r["paging"]):
                 i=0
                 while (i<100):
                     try:
                         r=requests.get(r["paging"]["next"], timeout=(5,5)).json()
                         break
                     except:
                         i=i+1
             else:
                 break
         return lista

     def postPost (self,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?message="+message+"&access_token="+str(token)
         s=requests.post(url).json()
         return s

     def postVideo(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"description":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)

         return s





class Events:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.can_guests_invite=""
         self.cover=""
         self.description=""
         self.end_time=""
         self.guest_list_enabled=""
         self.is_page_owned=""
         self.is_viewer_admin=""
         self.name=""
         self.owner=""
         self.parent_group=""
         self.start_time=""
         self.ticket_uri=""
         self.timezone=""
         self.updated_time=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("can_guests_invite" in dictionary):
             self.can_guests_invite=dictionary["can_guests_invite"]
         if ("cover" in dictionary):
             self.cover=Cover_Photo(dictionary["cover"])
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("end_time" in dictionary):
             self.end_time=dictionary["end_time"]
         if ("guest_list_enabled" in dictionary):
             self.guest_list_enabled=dictionary["guest_list_enabled"]
         if ("is_page_owned" in dictionary):
             self.is_page_owned=dictionary["is_page_owned"]
         if ("is_viewer_admin" in dictionary):
             self.is_viewer_admin=dictionary["is_viewer_admin"]
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("owner" in dictionary):
             self.owner=dictionary["owner"]
         if ("parent_group" in dictionary):
             self.parent_group=Group(dictionary["parent_group"])
         if ("start_time" in dictionary):
             self.start_time=dictionary["start_time"]
         if ("ticket_uri" in dictionary):
             self.ticket_uri=dictionary["ticket_uri"]
         if ("timezone" in dictionary):
             self.timezone=dictionary["timezone"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "EVENT: "+str(dic)


     def getAdmins(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/admins?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getAttending(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Attending?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getDeclined(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/declined?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getInterested(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/interested?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getLive_Videos(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/live_videos?fields=id,broadcast_start_time,creation_time,description,from,is_reference_only,live_views,permalink_url,seconds_left,status,title,total_views,video&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Live_Videos(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getMaybe(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/maybe?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getNoReply(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/noreply?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getRoles(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/noles?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getPicture(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Picture?fields=height,is_silhouette,url,width&redirect=0&type=large&access_token="+token).json()
         return r["data"]["url"]

     def getComments(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Comment(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getPhotos(self, token=None):
         if (token==None):
             token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Photos?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Photo(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getVideos(self, token=None):
         if (token==None):
             token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Videos?fields=backdated_time,backdated_time_granularity,id,created_time,description,embed_html,format,from,icon,is_instagram_eligible,length,permalink_url,picture,place,privacy,source,status,updated_time&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Video(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista



     def postVideo(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token


         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"description":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)

         return s

     def postPhoto(self, path,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         random_string = _Settings.Utility.randomword(50)
         extension=os.path.splitext(path)[1]
         file= _Settings.copyfile(path,random_string+extension)
         url="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(token)
         files={'file':open(path,'rb')}
         params={"message":message}
         s=requests.post(url, files=files,params=params).json()
         os.remove(file)
         return s

     def postPost (self,message=" ", token=None):
         if (token==None):
             token=_Settings.token
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?message="+message+"&access_token="+str(token)
         s=requests.post(url).json()
         return s

     def getPosts(self, token=None, dateMin="", dateMax="", limit=100):
         if (token==None):
             token=_Settings.token
         i=0
         while (i<100):
                     try:
                          r=requests.get("https://graph.facebook.com/v2.5/"+self.id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=100&access_token="+token,timeout=(5,5)).json()
                          break
                     except:
                          i=i+1
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_Post_Facebook.Post_Facebook(a))
             if ("next" in r["paging"]):
                 i=0
                 while (i<100):
                     try:
                         r=requests.get(r["paging"]["next"], timeout=(5,5)).json()
                         break
                     except:
                         i=i+1
             else:
                 break
         return lista

class Live_Videos:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.broadcast_start_time=""
         self.creation_time=""
         self.description=""
         self.from_=""
         self.is_reference_only=""
         self.live_views=""
         self.permalink_url=""
         self.seconds_left=""
         self.status=""
         self.title=""
         self.total_views=""
         self.video=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("broadcast_start_time" in dictionary):
             self.broadcast_start_time=dictionary["broadcast_start_time"]
         if ("creation_time" in dictionary):
             self.creation_time=dictionary["creation_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("is_reference_only" in dictionary):
             self.is_reference_only=dictionary["is_reference_only"]
         if ("live_views" in dictionary):
             self.live_views=dictionary["live_views"]
         if ("permalink_url" in dictionary):
             self.permalink_url=dictionary["permalink_url"]
         if ("seconds_left" in dictionary):
             self.seconds_left=dictionary["seconds_left"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("title" in dictionary):
             self.title=dictionary["title"]
         if ("total_views" in dictionary):
             self.total_views=dictionary["total_views"]
         if ("video" in dictionary):
             self.video=Video(dictionary["video"])


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "LIVE_VIDEO: "+str(dic)

     def getLikes(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista
     def getComments(self,token=None):
         if (token==None):
            token=_Settings.token

         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Comment(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

class Message:
     def __init__(self, dictionary=dict()):
         self.created_time=""
         self.from_=""
         self.id=""
         self.message=""
         self.subject=""
         self.tags=""
         self.to=""
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("subject" in dictionary):
             self.subject=dictionary["subject"]
         if ("tags" in dictionary):
             self.tags=dictionary["tags"]
         if ("to" in dictionary):
             self.to=dictionary["to"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "MESSAGE: "+str(dic)

class Thread:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.comments=list()
         self.to=""
         self.unread=""
         self.unseen=""
         self.updated_time=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("comments" in dictionary):
             self.comments=dictionary["comments"]
         if ("to" in dictionary):
             self.to=dictionary["to"]
         if ("unread" in dictionary):
             self.unread=dictionary["unread"]
         if ("unseen" in dictionary):
             self.unseen=dictionary["unseen"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "THREAD: "+str(dic)

class Comment:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.attachment=""
         self.can_comment=""
         self.can_remove=""
         self.can_hide=""
         self.can_like=""
         self.can_reply_privately=""
         self.comment_count=""
         self.created_time=""
         self.from_=""
         self.like_count=""
         self.message=""
         self.message_tags=""
         self.object=""
         self.parent=""
         self.private_reply_conversation=""
         self.user_likes=""
         self.message=""
         self.is_hidden=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("attachment" in dictionary):
             self.attachment=Story_Attachment(dictionary["attachment"])
         if ("can_comment" in dictionary):
             self.can_comment=dictionary["can_comment"]
         if ("can_remove" in dictionary):
             self.can_remove=dictionary["can_remove"]
         if ("can_hide" in dictionary):
             self.can_hide=dictionary["can_hide"]
         if ("can_like" in dictionary):
             self.can_like=dictionary["can_like"]
         if ("can_reply_privately" in dictionary):
             self.can_reply_privately=dictionary["can_reply_privately"]
         if ("comment_count" in dictionary):
             self.comment_count=dictionary["comment_count"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("from" in dictionary):
             self.from_=_User_Facebook.User_Facebook(dictionary=dictionary["from"])
         if ("like_count" in dictionary):
             self.like_count=dictionary["like_count"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("message_tags" in dictionary):
             self.message_tags=dictionary["message_tags"]
         if ("object" in dictionary):
             self.object=dictionary["object"]
         if ("parent" in dictionary):
             self.parent=dictionary["parent"]
         if ("private_reply_conversation" in dictionary):
             self.private_reply_conversation=dictionary["private_reply_conversation"]
         if ("user_likes" in dictionary):
             self.user_likes=dictionary["user_likes"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("is_hidden" in dictionary):
             self.is_hidden=dictionary["is_hidden"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "COMMENT: "+str(dic)

     def getInfo(self, token=None):
         if (token==None):
            token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token).json()
         c=Comment(dictionary=r)
         return c;

     def getLikes(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def postLike(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         return str(r)

     def deleteLike(self,token=None):
         if (token==None):
            token=_Settings.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token+"&method=delete").json()
         return str(r)

     def update(self,message=None, token=None):
         if (token==None):
            token=_Settings.token
         if message==None:
             message=self.message
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"?message="+message+"&access_token="+token).json()
         return str(r)

     def delete(self,token=None):
         if (token==None):
            token=_Settings.token
         self.update(message=" ",token=token)
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"?&access_token="+token+"&method=delete").json()
         return str(r)

class Story_Attachment:
     def __init__(self, dictionary=dict()):
         self.description=""
         self.description_tags=""
         self.media=""
         self.target=""
         self.title=""
         self.type=""
         self.url=""
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("description_tags" in dictionary):
             self.description_tags=dictionary["description_tags"]
         if ("media" in dictionary):
             self.media=dictionary["media"]
         if ("target" in dictionary):
             self.target=dictionary["target"]
         if ("title" in dictionary):
             self.title=dictionary["title"]
         if ("type" in dictionary):
             self.type=dictionary["type"]
         if ("url" in dictionary):
             self.url=dictionary["url"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "STORY_ATTACHMENT: "+str(dic)

class Education_Experience:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.classes=list()
         self.concentration=list()
         self.degree=""
         self.school=""
         self.type=""
         self.with_=list()
         self.year=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("classes" in dictionary):
             for experience in dictionary["classes"]:
                 self.classes.append(Experience(dictionary=dictionary["classes"]))
         if ("concentration" in dictionary):
             for page in dictionary["concentration"]:
                 self.concentration.append(Page(dictionary=dictionary["concentration"]))
         if ("degree" in dictionary):
             self.degree=Page(dictionary["degree"])
         if ("school" in dictionary):
             self.school=Page(dictionary["school"])
         if ("type" in dictionary):
             self.type=dictionary["type"]
         if ("with" in dictionary):
             for user in dictionary["with"]:
                 self.with_.append(_User_Facebook.User_Facebook(dictionary=dictionary["with"]))
         if ("year" in dictionary):
             self.year=Page(dictionary["year"])


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "EDUCATION_EXPERIENCE: "+str(dic)

class Experience:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.description=""
         self.from_=""
         self.name=""
         self.with_=list()
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("from" in dictionary):
             self.from_=_User_Facebook.User_Facebook(dictionary= dictionary["from"])
         if ("name" in dictionary):
             self.name=dictionary["name"]
         if ("with" in dictionary):
             for user in dictionary["with"]:
                self.with_.append(_User_Facebook.User_Facebook(dictionary=dictionary["with"]))


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "EXPERIENCE: "+str(dic)

class Cover_Photo:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.cover_id=""
         self.offset_x=""
         self.offset_y=""
         self.source=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("cover_id" in dictionary):
             self.cover_id=dictionary["cover_id"]
         if ("offset_x" in dictionary):
             self.offset_x=dictionary["offset_x"]
         if ("offset_y" in dictionary):
             self.offset_y=dictionary["offset_y"]
         if ("source" in dictionary):
             self.source=dictionary["source"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "COVER_PHOTO: "+str(dic)

class Video:
     def __init__(self, dictionary=dict()):
         self.backdated_time=""
         self.backdated_time_granularity=""
         self.id=""
         self.created_time=""
         self.description=""
         self.embed_html=""
         self.format=""
         self.from_=""
         self.icon=""
         self.is_instagram_eligible=""
         self.length=""
         self.permalink_url=""
         self.picture=""
         self.place=""
         self.privacy=""
         self.source=""
         self.status=""
         self.updated_time=""
         if ("backdated_time" in dictionary):
             self.backdated_time=dictionary["backdated_time"]
         if ("backdated_time_granularity" in dictionary):
             self.backdated_time_granularity=dictionary["backdated_time_granularity"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("embed_html" in dictionary):
             self.embed_html=dictionary["embed_html"]
         if ("format" in dictionary):
             self.format=dictionary["format"]
         if ("from" in dictionary):
             self.from_=dictionary["from"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("is_instagram_eligible" in dictionary):
             self.is_instagram_eligible=dictionary["is_instagram_eligible"]
         if ("length" in dictionary):
             self.length=dictionary["length"]
         if ("permalink_url" in dictionary):
             self.permalink_url=dictionary["permalink_url"]
         if ("picture" in dictionary):
             self.picture=dictionary["picture"]
         if ("place" in dictionary):
             self.place=dictionary["place"]
         if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
         if ("source" in dictionary):
             self.source=dictionary["source"]
         if ("status" in dictionary):
             self.status=dictionary["status"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "VIDEO: "+str(dic)

class Group_Doc:
     def __init__(self, dictionary=dict()):
         self.id=""
         self.from_=""
         self.subject=""
         self.message=""
         self.icon=""
         self.created_time=""
         self.updated_time=""
         self.revision=""
         self.can_edit=""
         self.can_delete=""
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("from" in dictionary):
             self.from_=_User_Facebook.User_Facebook(dictionary["from"])
         if ("subject" in dictionary):
             self.subject=dictionary["subject"]
         if ("message" in dictionary):
             self.message=dictionary["message"]
         if ("icon" in dictionary):
             self.icon=dictionary["icon"]
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
         if ("revision" in dictionary):
             self.revision=dictionary["revision"]
         if ("can_edit" in dictionary):
             self.can_edit=dictionary["can_edit"]
         if ("can_delete" in dictionary):
             self.can_delete=dictionary["can_delete"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "GROUP_DOC: "+str(dic)
     def getGroup_Doc(self):
         r=requests.get("https://graph.facebook.com/v2.6/me/Group_Doc?&access_token="+self.token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Group_Doc(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

class Life_Event:
     def __init__(self, dictionary=dict()):
         self.created_time=""
         self.description=""
         self.end_time=""
         self.from_=""
         self.id=""
         self.is_hidden=""
         self.start_time=""
         self.title=""
         self.updated_time=""
         if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("end_time" in dictionary):
             self.end_time=dictionary["end_time"]
         if ("from" in dictionary):
             self.from_=Page(dictionary["from"])
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("is_hidden" in dictionary):
             self.is_hidden=dictionary["is_hidden"]
         if ("start_time" in dictionary):
             self.start_time=dictionary["start_time"]
         if ("title" in dictionary):
             self.title=dictionary["title"]
         if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]


     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "LIFE_EVENT: "+str(dic)

     def getPhotos(self, token=None):
         if (token==None):
             token=_Settings.token
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Photos?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Photo(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

     def getLikes(self,token=None):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User_Facebook.User_Facebook(dictionary=a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista
     def getComments(self,token=None):
         if (token==None):
            token=_Settings.token

         r=requests.get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Comment(a))
             if ("next" in r["paging"]):
                 r=requests.get(r["paging"]["next"]).json()
             else:
                 break
         return lista

