__author__ = 'Joao'
from SolFB import _FacebookUser
from SolFB import _Actions
from SolFB import _Utility
from SolFB import _Post_Facebook

class AuthenticatedFacebookUser(_FacebookUser.FacebookUser):

    def __init__(self,token):
        dict = _Actions.Actions.me(token,True)
        _FacebookUser.FacebookUser.__init__(self,dict)
        self.token=token

    def getMyPosts(self, dateMin="", dateMax="", limit=100, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/feed
        Essa função irá retornar os posts do usuário.
        Os parâmetros são duas datas e um limite, e a função irá retornar os posts publicados entre as datas
        Caso você use a função sem espécificar datas, a função irá retornar 25 posts mais recentes
        A quantidade de posts retornados será de no máximo o limite passado como parametro.
        Para receber um número ilimitado de posts, faça limite=-1'''
        from dateutil.parser import parse

        token=self.token
        params={}
        if (token == None):
            token = _Actions.token
        if (dateMin!="" and dateMax!="" and dateMin > dateMax):
            raise Exception("Cannot use dateMin > dateMax")
        if (dateMax != ""):
            params["until"]=dateMax
        r = _Utility.prepareRequest(maxRetries).get("https://graph.facebook.com/v2.5/" + self.id + "/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&limit=1000&access_token=" + token,timeout=timeout, params=params).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                post= _Post_Facebook.Post_Facebook(dictionary=a)
                if ((len(lista)==limit) or (dateMin!="" and parse(post.created_time).replace(tzinfo=None)<dateMin)):
                    return lista
                lista.append(post)
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def _getMyFriends(self):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/friendlists/
        '''
        import requests
        friends = requests.get("https://graph.facebook.com/v2.6/me/friendlists?&access_token=" + self.token).json()
        lista = list()
        for f in friends["data"]:
            lista.append(f)
        return lista

    def getAccounts(self, timeout=(5,5), maxRetries=50,business_id=None):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/accounts/
        '''
        import SolFB._Accounts as _Accounts
        params={}
        if (business_id!=None):
            params["business_id"]=business_id
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/accounts?&access_token=" + self.token,params=params, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Accounts.Accounts(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def getAchievements(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/achievements/
        '''
        import SolFB._Achievements as _Achievements
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/achievements?&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Achievements.Achievements(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def getAdaccounts(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/adaccounts/
        '''
        import SolFB._Adaccounts as _Adaccounts
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Adaccounts?fields=id,account_groups,account_id,account_status,age,agency_client_declaration,amount_spent,balance,business,business_city,business_country_code,business_name,business_state,business_street,business_street2,business_zip,can_create_brand_lift_study,capabilities,created_time,currency,end_advertiser_name,failed_delivery_checks,funding_source,funding_source_details,has_migrated_permissions,end_advertiser,disable_reason,io_number,is_notifications_enabled,is_personal,is_prepay_account,is_tax_id_required,last_used_time,line_numbers,media_agency,min_campaign_group_spend_cap,min_daily_budget,name,offsite_pixels_tos_accepted,owner,owner_business,partner,rf_spec,spend_cap,tax_id,tax_id_status,tax_id_type,timezone_id,timezone_name,timezone_offset_hours_utc,tos_accepted,user_role&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Adaccounts.Adaccounts(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getAlbums(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/albums/
        '''
        import SolFB._Albums as _Albums
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Albums?fields=id,can_upload,count,cover_photo,created_time,description,event,from,link,location,name,place,privacy,type,updated_time&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Albums.Albums(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def postAlbum(self, name="MyAlbum", message="", timeout=(5,5), maxRetries=50):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/user/albums/
         '''
         if (self.token==None):
            self.token= _Actions.token
         params={"message":message,"name":name}
         print(params)
         r= _Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/me/albums?access_token="+self.token,params=params, timeout=timeout).json()
         return r

    def getApprequests(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/apprequests/
        '''
        import SolFB._Apprequests as _Apprequests
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Apprequests?fields=id,action_type,application,created_time,data,from,message,object,to&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Apprequests.Apprequests(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def getBooks(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/books/
        '''
        import SolFB._Page as _Page
        #new field: created_time
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Books?fields=created_time,id,about,affiliation,app_id,app_links,artists_we_like,attire,awards,band_interests,band_members,best_page,bio,birthday,booking_agent,built,can_checkin,can_post,category,category_list,checkins,company_overview,contact_address,country_page_likes,cover,culinary_team,current_location,description,description_html,directed_by,display_subtext,emails,features,food_styles,founded,general_info,general_manager,genre,global_brand_page_name,global_brand_root_id,has_added_app,hometown,hours,influences,is_community_page,is_permanently_closed,is_published,is_unclaimed,is_verified,last_used_time,leadgen_tos_accepted,link,location,members,mission,mpg,name,network,new_like_count,offer_eligible,owner_business,parent_page,parking,payment_options,personal_info,personal_interests,pharma_safety_info,phone,place_type,plot_outline,press_contact,price_range,produced_by,products,public_transit,record_label,release_date,restaurant_services,restaurant_specialties,schedule,screenplay_by,season,single_line_address,starring,store_number,studio,talking_about_count,unread_message_count,unread_notif_count,unseen_message_count,username,voip_info,website,were_here_count,written_by&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        print(r)
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Page.Page(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def getEvents(self, replyType=None, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/events/
        '''
        import SolFB._Events as _Events
        params={}
        if (replyType!=None):
            params={"type":replyType}
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Events?fields=rsvp_status,id,can_guests_invite,cover,description,end_time,guest_list_enabled,is_page_owned,is_viewer_admin,name,owner,parent_group,start_time,ticket_uri,timezone,updated_time&access_token=" + self.token, timeout=timeout, params=params).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Events.Events(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def getFamily(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/family
        '''
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/Family?fields=id,name,relationship&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        print(r)
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_FacebookUser.FacebookUser(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def getGames(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/games/
        '''
        import SolFB._Page as _Page
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Books?fields=created_time,id,about,affiliation,app_id,app_links,artists_we_like,attire,awards,band_interests,band_members,best_page,bio,birthday,booking_agent,built,can_checkin,can_post,category,category_list,checkins,company_overview,contact_address,country_page_likes,cover,culinary_team,current_location,description,description_html,directed_by,display_subtext,emails,features,food_styles,founded,general_info,general_manager,genre,global_brand_page_name,global_brand_root_id,has_added_app,hometown,hours,influences,is_community_page,is_permanently_closed,is_published,is_unclaimed,is_verified,last_used_time,leadgen_tos_accepted,link,location,members,mission,mpg,name,network,new_like_count,offer_eligible,owner_business,parent_page,parking,payment_options,personal_info,personal_interests,pharma_safety_info,phone,place_type,plot_outline,press_contact,price_range,produced_by,products,public_transit,record_label,release_date,restaurant_services,restaurant_specialties,schedule,screenplay_by,season,single_line_address,starring,store_number,studio,talking_about_count,unread_message_count,unread_notif_count,unseen_message_count,username,voip_info,website,were_here_count,written_by&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Page.Page(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getGroups(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/groups/
        '''
        import SolFB._Group as _Group
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.2/me/Groups?fields=administrator,unread,id,cover,description,email,icon,link,member_request_count,name,owner,parent,privacy,updated_time,cover_url&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Group.Group(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getLikes(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/likes/
        '''
        import SolFB._Page as _Page
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/Likes?fields=id,name,created_time&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Page.Page(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def postPost (self,message=" ", ):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/user/feed
         '''
         import requests
         params={"message":message}
         url="https://graph.facebook.com/v2.6/me/feed?&access_token="+str(self.token)
         s=requests.post(url,params=params).json()
         return s


    def getLive_Videos(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/live_videos/
        '''
        import SolFB._Live_Videos as _Live_Videos
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Live_Videos?fields=id,broadcast_start_time,creation_time,description,from,is_reference_only,live_views,permalink_url,seconds_left,status,title,total_views,video&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Live_Videos.Live_Videos(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getMovies(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/movies/
        '''
        import SolFB._Page as _Page
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Books?fields=created_time,id,about,affiliation,app_id,app_links,artists_we_like,attire,awards,band_interests,band_members,best_page,bio,birthday,booking_agent,built,can_checkin,can_post,category,category_list,checkins,company_overview,contact_address,country_page_likes,cover,culinary_team,current_location,description,description_html,directed_by,display_subtext,emails,features,food_styles,founded,general_info,general_manager,genre,global_brand_page_name,global_brand_root_id,has_added_app,hometown,hours,influences,is_community_page,is_permanently_closed,is_published,is_unclaimed,is_verified,last_used_time,leadgen_tos_accepted,link,location,members,mission,mpg,name,network,new_like_count,offer_eligible,owner_business,parent_page,parking,payment_options,personal_info,personal_interests,pharma_safety_info,phone,place_type,plot_outline,press_contact,price_range,produced_by,products,public_transit,record_label,release_date,restaurant_services,restaurant_specialties,schedule,screenplay_by,season,single_line_address,starring,store_number,studio,talking_about_count,unread_message_count,unread_notif_count,unseen_message_count,username,voip_info,website,were_here_count,written_by&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Page.Page(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getMusic(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/music/
        '''
        import SolFB._Page as _Page
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Books?fields=created_time,id,about,affiliation,app_id,app_links,artists_we_like,attire,awards,band_interests,band_members,best_page,bio,birthday,booking_agent,built,can_checkin,can_post,category,category_list,checkins,company_overview,contact_address,country_page_likes,cover,culinary_team,current_location,description,description_html,directed_by,display_subtext,emails,features,food_styles,founded,general_info,general_manager,genre,global_brand_page_name,global_brand_root_id,has_added_app,hometown,hours,influences,is_community_page,is_permanently_closed,is_published,is_unclaimed,is_verified,last_used_time,leadgen_tos_accepted,link,location,members,mission,mpg,name,network,new_like_count,offer_eligible,owner_business,parent_page,parking,payment_options,personal_info,personal_interests,pharma_safety_info,phone,place_type,plot_outline,press_contact,price_range,produced_by,products,public_transit,record_label,release_date,restaurant_services,restaurant_specialties,schedule,screenplay_by,season,single_line_address,starring,store_number,studio,talking_about_count,unread_message_count,unread_notif_count,unseen_message_count,username,voip_info,website,were_here_count,written_by&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Page.Page(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getPermissions(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/permissions/
        '''
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/Permissions?&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(a)
            if ("paging" in r and "next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getPhotos(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/photos/
        '''
        import SolFB._Photo as _Photo
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Photos?fields=id,album,backdated_time,backdated_time_granularity,can_delete,can_tag,created_time,from,height,icon,images,link,name,name_tags,page_story_id,picture,place,updated_time,width&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Photo.Photo(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getPicture(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/picture/
        '''
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Picture?fields=height,is_silhouette,url,width&redirect=0&access_token=" + self.token, timeout=timeout).json()
        print(r)
        return r["data"]["url"]


    def getTelevision(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/television/
        '''
        import SolFB._Page as _Page
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Television?fields=created_time,id,about,affiliation,app_id,app_links,artists_we_like,attire,awards,band_interests,band_members,best_page,bio,birthday,booking_agent,built,can_checkin,can_post,category,category_list,checkins,company_overview,contact_address,country_page_likes,cover,culinary_team,current_location,description,description_html,directed_by,display_subtext,emails,features,food_styles,founded,general_info,general_manager,genre,global_brand_page_name,global_brand_root_id,has_added_app,hometown,hours,influences,is_community_page,is_permanently_closed,is_published,is_unclaimed,is_verified,last_used_time,leadgen_tos_accepted,link,location,members,mission,mpg,name,network,new_like_count,offer_eligible,owner_business,parent_page,parking,payment_options,personal_info,personal_interests,pharma_safety_info,phone,place_type,plot_outline,press_contact,price_range,produced_by,products,public_transit,record_label,release_date,restaurant_services,restaurant_specialties,schedule,screenplay_by,season,single_line_address,starring,store_number,studio,talking_about_count,unread_message_count,unread_notif_count,unseen_message_count,username,voip_info,website,were_here_count,written_by&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Page.Page(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getVideo_Broadcasts(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/video_broadcasts/
        '''
        import SolFB._Live_Videos as _Live_Videos
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Video_Broadcasts?fields=id,broadcast_start_time,creation_time,description,from,is_reference_only,live_views,permalink_url,seconds_left,status,title,total_views,video&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Live_Videos.Live_Videos(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getVideos(self, timeout=(5,5), maxRetries=50):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/videos/
        '''
        import SolFB._Video as _Video
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Videos?fields=backdated_time,backdated_time_granularity,id,created_time,description,embed_html,format,from,icon,is_instagram_eligible,length,permalink_url,picture,place,privacy,source,status,updated_time&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Video.Video(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista

    def postVideo(self, Localpath=None, FileURL=None,message=" "):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/user/videos/
         '''
         import requests
         if (Localpath==None and FileURL==None):
             raise Exception("You should use a LocalPath or a URL")
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):


             graphurl="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+self.token
             files={'file':open(Localpath,'rb')}
             params={"description":message}
             s=requests.post(graphurl, files=files,params=params).json()

             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph-video.facebook.com/"+self.id+"/videos?access_token="+self.token
             params={"description":message}
             params["file_url"]=FileURL
             return requests.post(graphurl,params=params).json()

    def postPhoto(self, Localpath=None, FileURL=None,message=" "):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/user/photos/
         '''
         import requests
         if (Localpath==None and FileURL==None):
             raise Exception("You should use a LocalPath or a URL")
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(self.token)
             files={'file':open(Localpath,'rb')}
             params={"description":message}
             s=requests.post(graphurl, files=files,params=params).json()
             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/photos?access_token="+str(self.token)
             params={"description":message}
             params["file_url"]=FileURL
             return requests.post(graphurl,params=params).json()

    def postPost (self,message=" ", token=None):
         '''
         https://developers.facebook.com/docs/graph-api/reference/user/feed
         '''
         import requests
         if (token==None):
             token= _Actions.token
         params={"message":message}
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?&access_token="+self.token
         s=requests.post(url,params=params).json()
         return s