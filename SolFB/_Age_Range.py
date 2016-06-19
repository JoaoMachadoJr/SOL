__author__ = 'Joao'
class Age_Range:
     def __init__(self, dictionary=dict()):
         self.max=""
         self.min=""
         if ("max" in dictionary):
             self.max=dictionary["max"]
         if ("min" in dictionary):
             self.min=dictionary["min"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "AGE_RANGE: "+str(dict)
