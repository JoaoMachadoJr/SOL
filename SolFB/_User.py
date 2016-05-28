from SolFB import _Utility, _Post_Facebook, _Settings

__author__ = 'Joao'

# import pip
# pip.main(['install', 'https://github.com/pythonforfacebook/facebook-sdk/archive/master.zip'])
#import facebook
'''import requests
from dateutil.parser import parse
import SolFB._Post_Facebook as _Post_Facebook
from  SolFB._Utility import Utility as _Utility
from  SolFB._Settings import Settings as _Settings
import SolFB._Age_Range as _Age_Range
import SolFB._Admin_Note as _Admin_Note
import SolFB._Cover_Photo as _Cover_Photo
import SolFB._Currency as _Currency
import SolFB._User_Device as _User_Device
import SolFB._Education_Experience as _Education_Experience
import SolFB._Experience as _Experience
import SolFB._Page as _Page
import SolFB._Page_Label as _Page_Label
import SolFB._Accounts as _Accounts
import SolFB._Achievements as _Achievements
import SolFB._Adaccountgroups as _Adaccountgroups
import SolFB._Adaccounts as _Adaccounts
import SolFB._Adcontracts as _Adcontracts
import SolFB._Group as _Group
import SolFB._Albums as _Albums
import SolFB._Apprequests as _Apprequests
import SolFB._Events as _Events
import SolFB._Live_Videos as _Live_Videos
import SolFB._Photo as _Photo
import SolFB._Video as _Video'''


class User():

    '''Essa é a classe de usuários para facebook.
    A autenticação é feita por um Token, que deve ser obtido no site do facebook'''


    def __init__(self, token="", dictionary=dict(),id=""):
        '''O construtor pode receber o token de acesso, ou não receber nada
        Caso o construtor já receba o token, ele fará a conexão de uma vez
        Descriçao dos campos: https://developers.facebook.com/docs/graph-api/reference/user/
        toekn (String): Token de acesso
        type (String): Tipo: {user, page, group}
        id (String numérica): ID numérico do usuário njo facebook
        age_range (dictionary: ["min", "max"]): Intervalo de idades que o usuário pode ter, baseado no seu ano de nascimento
        bio (String): Biografia
        birthday (String): Aniversário
        context (dictionary:["id","all_mutual_friends","mutual_friends","mutual_likes","three_degree_mutual_friends"]): Contexto social. Mais informações:https://developers.facebook.com/docs/graph-api/reference/user-context/
        cover (dictionary:["id","cover_id","offset_x","offset_y","source"]): Foto de capa do usuário
        currency (dictionary:["currency_offset","usd_exchange","usd_exchange_inverse","user_currency"]): Informações sobre a moeda do país do usuário
        devices(list): Lista de dispositivos do usuário
        education(list): Lista de instituições onde o usuário estudou
        email(string): Email do usuário
        favorite_athletes(list): Lista de atletas favoritos
        favorite_teams(list): Lista de times favoritos
        first_name(string): Primeiro nome
        gender(string): Gênero
        hometown(page): cidade natal
        inspirational_people(list): Lista de ídolos
        install_type(string); É um ENUM, porém mal documentado
        installed(bool): Informa se um APP especifico está instalado
        interested_in (list): Lista de gêneros nos quais o usuário tem interesse
        is_shared_login (bool): Se é um login compartilhado
        is_verified (bool): Se é um usuário verificado
        labels (list): Algumas etiquetas que o usuário pode ter
        languages (list): Idiomas que o usuário fala
        last_name (String): Sobrenome
        link (String): Link para o feed do usuário
        locale (locale): locale do usuário
        location (page): Local do usuário
        meeting_for(list de string): mal documentado
        middle_name(string): Nome do meio
        name(String): Nome completo
        name_format(String): O formato como o nome deve aparecer
        payment_pricepoints(dictionary["mobile"]): Mal documentado
        political(String): Posição política
        public_key(String): Chave pública de criptografia
        quotes(Sring): Citações favoritas
        relationship_status(String): Status de relacionamento
        religion(String): Religião
        security_settings(dictionary["secure_browsing"])
        significant_other(User): Pessoa marcada como significant_other do usuário (esposo, melhor amigo, namorada, etc)
        sports(list): Lista de esportes de interesse do usuário
        test_group(int): Mal documentado
        third_party_id(string): Id anonimo e irrastreavel
        timezone(float): A zona temnporal do usuário
        updated_time(datetime): ultimo update
        verified(bool): Se o usuário é verificadoThis is distinct from the is_verified field. Someone is considered verified if they take any of the following actions: Register for mobile ,Confirm their account via SMS ,Enter a valid credit card
        video_upload_limits(dictionary["lenght","size"]): Mal documentado
        viewer_can_send_gift(bool): Se está apto a receber um 'gift'
        website(string): Site do usuário
        work(list): Lista de empregos presentes e passados

        '''

        import SolFB._Age_Range as _Age_Range
        import SolFB._Admin_Note as _Admin_Note
        import SolFB._Cover_Photo as _Cover_Photo
        import SolFB._Currency as _Currency
        import SolFB._User_Device as _User_Device
        import SolFB._Education_Experience as _Education_Experience
        import SolFB._Experience as _Experience
        import SolFB._Page as _Page
        import SolFB._Page_Label as _Page_Label

        super(User, self).__init__()
        self.token = token
        self.type = ""
        self.admin_notes=list()
        self.id = ""
        self.about = ""
        self.age_range = _Age_Range.Age_Range()
        self.bio = ""
        self.birthday = ""
        self.cover = ""
        self.currency = ""
        self.devices = list()
        self.education = list()
        self.email = ""
        self.favorite_athletes = list()
        self.favorite_teams = list()
        self.first_name = ""
        self.gender = ""
        self.hometown = ""
        self.inspirational_people = list()
        self.install_type = ""
        self.installed = ""
        self.interested_in = list()
        self.is_shared_login = ""
        self.is_verified = ""
        self.labels = list()
        self.languages = list()
        self.last_name = ""
        self.link = ""
        self.locale = ""
        self.location = ""
        self.meeting_for = ""
        self.middle_name = ""
        self.name = ""
        self.name_format = ""
        self.political = ""
        self.public_key = ""
        self.quotes = ""
        self.relationship_status = ""
        self.religion = ""
        self.shared_login_upgrade_required_by = ""
        self.significant_other = ""
        self.sports = list()
        self.test_group = ""
        self.third_party_id = ""
        self.timezone = ""
        self.updated_time = ""
        self.verified = ""
        self.viewer_can_send_gift = ""
        self.website = ""
        self.work = list()
        dict_user=dictionary
        if (token != ""):
            dict_user=self.connect()

        if ("id") in dict_user:
            self.id = dict_user["id"]
        if ("about") in dict_user:
            self.about = dict_user["about"]
        if ("admin_notes") in dict_user:
            for i in dict_user["admin_notes"]:
                self.admin_notes.append(_Admin_Note.Admin_Note(dictionary=i))
        if ("age_range") in dict_user and "max" in dict_user["age_range"]:
            self.age_range.max = dict_user["age_range"]["max"]
        if ("age_range") in dict_user and "min" in dict_user["age_range"]:
            self.age_range.min = dict_user["age_range"]["min"]
        if ("bio") in dict_user:
            self.bio = dict_user["bio"]
        if ("birthday") in dict_user:
            self.birthday = dict_user["birthday"]
        if ("cover") in dict_user:
            self.cover = _Cover_Photo.Cover_Photo(dictionary=dict_user["cover"])
        if ("currency") in dict_user:
            self.currency = _Currency.Currency(dict_user["currency"])
        if ("devices") in dict_user:
            for i in dict_user["devices"]:
                self.devices.append(_User_Device.User_Device(dictionary=i))
        if ("education") in dict_user:
            for i in dict_user["education"]:
                self.education.append(_Education_Experience.Education_Experience(dictionary=i))
        if ("email") in dict_user:
            self.email = dict_user["email"]
        if ("favorite_athletes") in dict_user:
            for i in dict_user["favorite_athletes"]:
                self.favorite_athletes.append(_Experience.Experience(dictionary=i))
        if ("favorite_teams") in dict_user:
             for i in dict_user["favorite_teams"]:
                self.favorite_teams.append(_Experience.Experience(dictionary=i))
        if ("first_name") in dict_user:
            self.first_name = dict_user["first_name"]
        if ("gender") in dict_user:
            self.gender = dict_user["gender"]
        if ("hometown") in dict_user:
            self.hometown = _Page.Page(dictionary=dict_user["hometown"])
        if ("inspirational_people") in dict_user:
            for i in dict_user["inspirational_people"]:
                self.inspirational_people.append(_Experience.Experience(dictionary=i))
        if ("install_type") in dict_user:
            self.install_type = dict_user["install_type"]
        if ("installed") in dict_user:
            self.installed = dict_user["installed"]
        if ("interested_in") in dict_user:
            self.interested_in = dict_user["interested_in"]
        if ("is_shared_login") in dict_user:
            self.is_shared_login = dict_user["is_shared_login"]
        if ("is_verified") in dict_user:
            self.is_verified = dict_user["is_verified"]
        if ("labels") in dict_user:
            for i in dict_user["labels"]:
                self.labels.append(_Page_Label.Page_Label(dictionary=i))
        if ("languages") in dict_user:
            for i in dict_user["languages"]:
                self.languages.append(_Experience.Experience(dictionary=i))
        if ("last_name") in dict_user:
            self.last_name = dict_user["last_name"]
        if ("link") in dict_user:
            self.link = dict_user["link"]
        if ("locale") in dict_user:
            self.locale = dict_user["locale"]
        if ("location") in dict_user:
            self.location = _Page.Page(dictionary=dict_user["location"])
        if ("meeting_for") in dict_user:
            self.meeting_for = dict_user["meeting_for"]
        if ("middle_name") in dict_user:
            self.middle_name = dict_user["middle_name"]
        if ("name") in dict_user:
            self.name = dict_user["name"]
        if ("name_format") in dict_user:
            self.name_format = dict_user["name_format"]
        if ("political") in dict_user:
            self.political = dict_user["political"]
        if ("public_key") in dict_user:
            self.public_key = dict_user["public_key"]
        if ("quotes") in dict_user:
            self.quotes = dict_user["quotes"]
        if ("relationship_status") in dict_user:
            self.relationship_status = dict_user["relationship_status"]
        if ("religion") in dict_user:
            self.religion = dict_user["religion"]
        if ("shared_login_upgrade_required_by") in dict_user:
            self.shared_login_upgrade_required_by = dict_user["shared_login_upgrade_required_by"]
        if ("significant_other") in dict_user:
            self.significant_other = User(dictionary=dict_user["significant_other"])
        if ("sports") in dict_user:
            for i in dict_user["sports"]:
                self.sports.append(_Experience.Experience(dictionary=i))
        if ("test_group") in dict_user:
            self.test_group = dict_user["test_group"]
        if ("third_party_id") in dict_user:
            self.third_party_id = dict_user["third_party_id"]
        if ("timezone") in dict_user:
            self.timezone = dict_user["timezone"]
        if ("updated_time") in dict_user:
            self.updated_time = dict_user["updated_time"]
        if ("verified") in dict_user:
            self.verified = dict_user["verified"]
        if ("video_upload_limits") in dict_user:
            self.video_upload_limits = dict_user["video_upload_limits"]
        if ("viewer_can_send_gift") in dict_user:
            self.viewer_can_send_gift = dict_user["viewer_can_send_gift"]
        if ("website") in dict_user:
            self.website = dict_user["website"]
        if ("relationship") in dict_user:
            self.relationship = dict_user["relationship"]
        if ("work") in dict_user:
            for i in dict_user["work"]:
                self.work.append(_Experience.Experience(dictionary=i))


    def connect(self):
        '''Esse método faz a conexão com o sistema do facebook, portanto é necessário
        que usuario.token possua um token válido.'''

        import requests
        _Settings.Settings.token=self.token

        dict_user = requests.get(
            "https://graph.facebook.com/v2.6/me?&fields=id,about,age_range,bio,birthday,context,cover,currency,devices,education,email,favorite_athletes,favorite_teams,first_name,gender,hometown,inspirational_people,install_type,installed,interested_in,is_shared_login,is_verified,languages,last_name,link,locale,location,meeting_for,middle_name,name,name_format,payment_pricepoints,political,public_key,quotes,relationship_status,religion,security_settings,shared_login_upgrade_required_by,significant_other,sports,test_group,third_party_id,timezone,updated_time,verified,video_upload_limits,viewer_can_send_gift,website,work&access_token=" + str(
                self.token)).json()
        return dict_user




    def getMyPosts(self, dateMin="", dateMax="", limit=100, timeout=(5,5), maxRetries=50):
        '''Essa função irá retornar os posts do usuário.
        Os parâmetros são duas datas e um limite, e a função irá retornar os posts publicados entre as datas
        Caso você use a função sem espécificar datas, a função irá retornar 25 posts mais recentes
        A quantidade de posts retornados será de no máximo o limite passado como parametro.
        Para receber um número ilimitado de posts, faça limite=-1'''
        from dateutil.parser import parse

        token=self.token
        params={}
        if (token == None):
            token = _Settings.token
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


    def __str__(self):
     dic=self.__dict__
     lista=list()
     for key in dic:
         lista.append(key)
     for key in lista:
         if dic[key]==None or dic[key]=="" or dic[key]==list():
             del dic[key]
     for key in dic:
         dic[key]=str(dic[key])
     return "USER: "+str(dic)


    def longstr(self):
        retorno = ""
        if (self.id != ""):
            retorno += "ID: <" + str(self.id) + ">\n"
        if (self.about != ""):
            retorno += "ABOUT: <" + str(self.about) + ">\n"
        if (self.age_range != ""):
            retorno += "AGE_RANGE: <" + str(self.age_range) + ">\n"
        if (self.bio != ""):
            retorno += "BIO: <" + str(self.bio) + ">\n"
        if (self.birthday != ""):
            retorno += "BIRTHDAY: <" + str(self.birthday) + ">\n"
        if (self.context != ""):
            retorno += "CONTEXT: <" + str(self.context) + ">\n"
        if (self.cover != ""):
            retorno += "COVER: <" + str(self.cover) + ">\n"
        if (self.currency != ""):
            retorno += "CURRENCY: <" + str(self.currency) + ">\n"
        if (self.devices != ""):
            retorno += "DEVICES: <" + str(self.devices) + ">\n"
        if (self.education != ""):
            retorno += "EDUCATION: <" + str(self.education) + ">\n"
        if (self.email != ""):
            retorno += "EMAIL: <" + str(self.email) + ">\n"
        if (self.favorite_athletes != ""):
            retorno += "FAVORITE_ATHLETES: <" + str(self.favorite_athletes) + ">\n"
        if (self.favorite_teams != ""):
            retorno += "FAVORITE_TEAMS: <" + str(self.favorite_teams) + ">\n"
        if (self.first_name != ""):
            retorno += "FIRST_NAME: <" + str(self.first_name) + ">\n"
        if (self.gender != ""):
            retorno += "GENDER: <" + str(self.gender) + ">\n"
        if (self.hometown != ""):
            retorno += "HOMETOWN: <" + str(self.hometown) + ">\n"
        if (self.inspirational_people != ""):
            retorno += "INSPIRATIONAL_PEOPLE: <" + str(self.inspirational_people) + ">\n"
        if (self.install_type != ""):
            retorno += "INSTALL_TYPE: <" + str(self.install_type) + ">\n"
        if (self.installed != ""):
            retorno += "INSTALLED: <" + str(self.installed) + ">\n"
        if (self.interested_in != ""):
            retorno += "INTERESTED_IN: <" + str(self.interested_in) + ">\n"
        if (self.is_shared_login != ""):
            retorno += "IS_SHARED_LOGIN: <" + str(self.is_shared_login) + ">\n"
        if (self.is_verified != ""):
            retorno += "IS_VERIFIED: <" + str(self.is_verified) + ">\n"
        if (self.labels != ""):
            retorno += "LABELS: <" + str(self.labels) + ">\n"
        if (self.languages != ""):
            retorno += "LANGUAGES: <" + str(self.languages) + ">\n"
        if (self.last_name != ""):
            retorno += "LAST_NAME: <" + str(self.last_name) + ">\n"
        if (self.link != ""):
            retorno += "LINK: <" + str(self.link) + ">\n"
        if (self.locale != ""):
            retorno += "LOCALE: <" + str(self.locale) + ">\n"
        if (self.location != ""):
            retorno += "LOCATION: <" + str(self.location) + ">\n"
        if (self.meeting_for != ""):
            retorno += "MEETING_FOR: <" + str(self.meeting_for) + ">\n"
        if (self.middle_name != ""):
            retorno += "MIDDLE_NAME: <" + str(self.middle_name) + ">\n"
        if (self.name != ""):
            retorno += "NAME: <" + str(self.name) + ">\n"
        if (self.name_format != ""):
            retorno += "NAME_FORMAT: <" + str(self.name_format) + ">\n"
        if (self.payment_pricepoints != ""):
            retorno += "PAYMENT_PRICEPOINTS: <" + str(self.payment_pricepoints) + ">\n"
        if (self.political != ""):
            retorno += "POLITICAL: <" + str(self.political) + ">\n"
        if (self.public_key != ""):
            retorno += "PUBLIC_KEY: <" + str(self.public_key) + ">\n"
        if (self.quotes != ""):
            retorno += "QUOTES: <" + str(self.quotes) + ">\n"
        if (self.relationship_status != ""):
            retorno += "RELATIONSHIP_STATUS: <" + str(self.relationship_status) + ">\n"
        if (self.religion != ""):
            retorno += "RELIGION: <" + str(self.religion) + ">\n"
        if (self.security_settings != ""):
            retorno += "SECURITY_SETTINGS: <" + str(self.security_settings) + ">\n"
        if (self.shared_login_upgrade_required_by != ""):
            retorno += "SHARED_LOGIN_UPGRADE_REQUIRED_BY: <" + str(self.shared_login_upgrade_required_by) + ">\n"
        if (self.significant_other != ""):
            retorno += "SIGNIFICANT_OTHER: <" + str(self.significant_other) + ">\n"
        if (self.sports != ""):
            retorno += "SPORTS: <" + str(self.sports) + ">\n"
        if (self.test_group != ""):
            retorno += "TEST_GROUP: <" + str(self.test_group) + ">\n"
        if (self.third_party_id != ""):
            retorno += "THIRD_PARTY_ID: <" + str(self.third_party_id) + ">\n"
        if (self.timezone != ""):
            retorno += "TIMEZONE: <" + str(self.timezone) + ">\n"
        if (self.updated_time != ""):
            retorno += "UPDATED_TIME: <" + str(self.updated_time) + ">\n"
        if (self.verified != ""):
            retorno += "VERIFIED: <" + str(self.verified) + ">\n"
        if (self.video_upload_limits != ""):
            retorno += "VIDEO_UPLOAD_LIMITS: <" + str(self.video_upload_limits) + ">\n"
        if (self.viewer_can_send_gift != ""):
            retorno += "VIEWER_CAN_SEND_GIFT: <" + str(self.viewer_can_send_gift) + ">\n"
        if (self.website != ""):
            retorno += "WEBSITE: <" + str(self.website) + ">\n"
        if (self.work != ""):
            retorno += "WORK: <" + str(self.work) + ">\n"
        return retorno


    def _getMyFriends(self):
        import requests
        friends = requests.get("https://graph.facebook.com/v2.6/me/friendlists?&access_token=" + self.token).json()
        for f in friends["data"]:
            print(f)
        return


    def getAccounts(self, timeout=(5,5), maxRetries=50,business_id=None):
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


    def getAdaccountgroups(self, timeout=(5,5), maxRetries=50):
        import SolFB._Adaccountgroups as _Adaccountgroups
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/Adaccountgroups?&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Adaccountgroups.Adaccountgroups(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getAdaccounts(self, timeout=(5,5), maxRetries=50):
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


    def _getAdcontracts(self, timeout=(5,5), maxRetries=50):
        import SolFB._Adcontracts as _Adcontracts
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Adcontracts?fields=account_id,account_mgr_fbid,account_mgr_name,adops_person_name,advertiser_name,agency_name,campaign_name,created_by,created_date,io_number,io_type,last_updated_by,last_updated_date,max_end_date,mdc_fbid,min_start_date,salesrep_fbid,salesrep_name,status,subvertical,thirdparty_billed,thirdparty_password,thirdparty_uid,thirdparty_url,version,vertical&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Adcontracts.Adcontracts(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getAdmined_Groups(self, timeout=(5,5), maxRetries=50):
        import SolFB._Group as _Group
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Admined_Groups?fields=id,cover,description,email,icon,link,member_request_count,name,owner,parent,privacy,updated_time,cover_url&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        print(r)
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(_Group.Group(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getAlbums(self, timeout=(5,5), maxRetries=50):
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

         if (self.token==None):
            self.token= _Settings.token
         params={"message":message,"name":name}
         print(params)
         r= _Utility.prepareRequest(maxRetries=maxRetries).post("https://graph.facebook.com/v2.6/me/albums?access_token="+self.token,params=params, timeout=timeout).json()
         return r


    def getApprequests(self, timeout=(5,5), maxRetries=50):
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

        #response is enum{attending, created, declined, maybe, not_replied}
        #new field: rsvp_status
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
        #New Field: Relationship
        r = _Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/me/Family?fields=id,name,relationship&access_token=" + self.token, timeout=timeout).json()
        lista = list()
        print(r)
        while ("data" in r and len(r["data"]) > 0):
            for a in r["data"]:
                lista.append(User(dictionary=a))
            if ("next" in r["paging"]):
                r = _Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
            else:
                break
        return lista


    def getGames(self, timeout=(5,5), maxRetries=50):
        #new field: created_time
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
        #new fields: administrator,unread
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
        #new field: created_time
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
         import requests
         params={"message":message}
         url="https://graph.facebook.com/v2.6/me/feed?&access_token="+str(self.token)
         s=requests.post(url,params=params).json()
         return s


    def getLive_Videos(self, timeout=(5,5), maxRetries=50):
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
        #new field: created_time
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
        #new field: created_time
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
        r = _Utility.prepareRequest(maxRetries=maxRetries).get(
            "https://graph.facebook.com/v2.6/me/Picture?fields=height,is_silhouette,url,width&redirect=0&access_token=" + self.token, timeout=timeout).json()
        print(r)
        return r["data"]["url"]


    def getTelevision(self, timeout=(5,5), maxRetries=50):
        #new field: created_time
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
         import requests
         if (token==None):
             token= _Settings.token
         params={"message":message}
         url="https://graph.facebook.com/v2.6/"+self.id+"/feed?&access_token="+self.token
         s=requests.post(url,params=params).json()
         return s



