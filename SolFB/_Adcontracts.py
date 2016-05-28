__author__ = 'Joao'
class Adcontracts:
     def __init__(self, account_id="",dictionary=dict()):
         self.account_id=account_id
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
         print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ADCONTRACTS: "+str(dict)
