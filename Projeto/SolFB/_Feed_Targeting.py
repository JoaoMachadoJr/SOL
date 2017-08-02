__author__ = 'Joao'
class Feed_Targeting:
    def __init__(self, dictionary=None):
        '''
        Intro: https://www.facebook.com/help/352402648173466
        '''
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
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "FEED_TARGETING: "+str(dict)