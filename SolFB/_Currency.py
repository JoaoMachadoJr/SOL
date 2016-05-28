__author__ = 'Joao'
class Currency:
     def __init__(self,dictionary=dict()):
         self.currency_offset=""
         self.usd_exchange=""
         self.usd_exchange_inverse=""
         self.user_currency=""
         if ("currency_offset" in dictionary):
             self.currency_offset=dictionary["currency_offset"]
         if ("usd_exchange" in dictionary):
             self.usd_exchange=dictionary["usd_exchange"]
         if ("usd_exchange_inverse" in dictionary):
             self.usd_exchange_inverse=dictionary["usd_exchange_inverse"]
         if ("user_currency" in dictionary):
             self.user_currency=dictionary["user_currency"]


     def __str__(self):
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "CURRENCY: "+str(dict)
