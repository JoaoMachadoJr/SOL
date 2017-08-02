__author__ = 'Joao'
class Story_Attachment:

     def __init__(self, dictionary=dict()):
         '''
         Reference: https://developers.facebook.com/docs/graph-api/reference/story-attachment/
         '''
         self.description=""
         self.description_tags=""
         self.media=""
         self.target=""
         self.title=""
         self.type=""
         self.url=""
         if ("description" in dictionary):
             self.description=dictionary["description"]
         if ("description_tags" in dictionary):
             self.description_tags=dictionary["description_tags"]
         if ("media" in dictionary):
             self.media=dictionary["media"]
         if ("target" in dictionary):
             self.target=dictionary["target"]
         if ("title" in dictionary):
             self.title=dictionary["title"]
         if ("type" in dictionary):
             self.type=dictionary["type"]
         if ("url" in dictionary):
             self.url=dictionary["url"]


     def __str__(self):
         #print(self.__dict__)
         dic=self.__dict__
         dict={}

         for key in dic:
             if not(dic[key]==None or dic[key]==""):
                 dict[key]=dic[key]
         return "STORY_ATTACHMENT: "+str(dict)
