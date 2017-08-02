__author__ = 'Joao'
class Adaccounts:
     def __init__(self, id="",dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/user/adaccounts/
         '''
         self.id=id
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
        # print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "ADACCOUNT: "+str(dict)