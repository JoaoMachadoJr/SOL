__author__ = 'Joao'
import _Post_Facebook
import _User
import _User_Facebook
import requests
from  Utility import *
User_Facebook=_User_Facebook.User_Facebook


u = User_Facebook("CAACxxfv6ORIBAPip9leRDpWkrOEOmZAZA9rlwEanVuAexUxv4VhAXIqB0uEHQ1uhEU5IxaNpVKwWqq8E8aWI8tsSMFQLKpVzoZBCBM2Bo0wTNrGEeLIV2x2pNlGqa3lKtVkwbzdbVPtOiXsHz9SlWVViZCXxbtHbofdfkFG6TbbR5Yd6X9pazIvkTLYT2un0tYJXuxmKygZDZD")
u.connect()
print(u.name+" , "+u.id)
print(u.longstr())
#print(u.connection.get_object("granpk"))
#d=date("01/01/2001")





#r=u.getPostsFromGroup("ccpuro","","",-1)
#for i in r:
#    print(str(i).replace("\n","  "))





