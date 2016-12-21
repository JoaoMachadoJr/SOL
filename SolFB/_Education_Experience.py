__author__ = 'Joao'


import SolFB._Experience as _Experience
import SolFB._Page as _Page
import SolFB._FacebookUser as _User

class Education_Experience:
     def __init__(self,id="", dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/education-experience/
         '''
         self.id=id
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
                 self.classes.append(_Experience.Experience(dictionary=dictionary["classes"]))
         if ("concentration" in dictionary):
             for page in dictionary["concentration"]:
                 self.concentration.append(_Page.Page(dictionary=dictionary["concentration"]))
         if ("degree" in dictionary):
             self.degree=_Page.Page(dictionary=dictionary["degree"])
         if ("school" in dictionary):
             self.school=_Page.Page(dictionary=dictionary["school"])
         if ("type" in dictionary):
             self.type=dictionary["type"]
         if ("with" in dictionary):
             for user in dictionary["with"]:
                 self.with_.append(_User.FacebookUser(dictionary=dictionary["with"]))
         if ("year" in dictionary):
             self.year=_Page.Page(dictionary=dictionary["year"])


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "EDUCATION_EXPERIENCE: "+str(dict)
