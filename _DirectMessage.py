__author__ = 'Joao'
import _Utils
import _Entity
import _User
import _Access
class DirectMessage:
     def __init__(self,id=None, dictionary=dict()):
         dictionary=_Utils.CastToDictionary(dictionary)
         dictionary=_Utils.removeEmptyFields(dictionary)
         self.recipient_screen_name=""
         self._api=""
         self.id=id
         self.recipient=""
         self.recipient_id=""
         self.entities=""
         self.recipient_id_str=""
         self.sender_screen_name=""
         self.id_str=""
         self.sender_id=""
         self.text=""
         self.created_at=""
         self.sender=""
         self.sender_id_str=""
         if ("recipient_screen_name" in dictionary):
             self.recipient_screen_name=dictionary["recipient_screen_name"]
         if ("id" in dictionary):
             self.id=dictionary["id"]
         if ("recipient" in dictionary):
             self.recipient=_User.User(dictionary=dictionary["recipient"])
         if ("recipient_id" in dictionary):
             self.recipient_id=dictionary["recipient_id"]
         if ("entities" in dictionary):
             self.entities=_Entity.Entity(dictionary=dictionary["entities"])
         if ("recipient_id_str" in dictionary):
             self.recipient_id_str=dictionary["recipient_id_str"]
         if ("sender_screen_name" in dictionary):
             self.sender_screen_name=dictionary["sender_screen_name"]
         if ("id_str" in dictionary):
             self.id_str=dictionary["id_str"]
         if ("sender_id" in dictionary):
             self.sender_id=dictionary["sender_id"]
         if ("text" in dictionary):
             self.text=dictionary["text"]
         if ("created_at" in dictionary):
             self.created_at=dictionary["created_at"]
         if ("sender" in dictionary):
             self.sender=_User.User(dictionary=dictionary["sender"])
         if ("sender_id_str" in dictionary):
             self.sender_id_str=dictionary["sender_id_str"]

     def postDestroy(self, Access : _Access.StrongAccess = None):
         return _User.User().postDestroyDirectMessage(id=self.id,Access=Access)

     def __str__(self):
         dic=self.__dict__
         lista=list()
         for key in dic:
             lista.append(key)
         for key in lista:
             if dic[key]==None or dic[key]=="":
                 del dic[key]
         return "DIRECTMESSAGE: "+str(dic)