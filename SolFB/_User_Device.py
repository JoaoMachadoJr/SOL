__author__ = 'Joao'
class User_Device:
     def __init__(self, dictionary=dict()):
         self.hardware=""
         self.os=""
         if ("hardware" in dictionary):
             self.hardware=dictionary["hardware"]
         if ("os" in dictionary):
             self.os=dictionary["os"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "USER_DEVICE: "+str(dict)
