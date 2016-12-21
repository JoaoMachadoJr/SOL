from SolFB import _Utility, _Post_Facebook, _Actions

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
import SolFB._Adaccounts as _Adaccounts
import SolFB._Adcontracts as _Adcontracts
import SolFB._Group as _Group
import SolFB._Albums as _Albums
import SolFB._Apprequests as _Apprequests
import SolFB._Events as _Events
import SolFB._Live_Videos as _Live_Videos
import SolFB._Photo as _Photo
import SolFB._Video as _Video'''


class FacebookUser:

    '''Essa é a classe de usuários para facebook.
    A autenticação é feita por um Token, que deve ser obtido no site do facebook'''


    def __init__(self, dictionary=dict(),id=""):
        '''
        Reference: https://developers.facebook.com/docs/graph-api/reference/user/
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
            self.significant_other = FacebookUser(dictionary=dict_user["significant_other"])
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






