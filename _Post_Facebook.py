__author__ = 'Joao'
import requests
import _User
from dateutil.parser import parse
from _Facebook_Classes import *
import _Settings
import _Utility

class Post_Facebook: #Classe para os POSTs das redes sociais
    def __init__(self, id=-1, created_time="", message="", story="", dictionary=dict()):
        '''self.id é o ID do post. Campo id
        self.data é a data de criação. Campo create_date
        self.message é o texto escrito pelo usuário. Campo message
        self.story é o tipo de ação. Campo story. (exemplo: Fulano compartilhou uma foto de ciclano)
        self.caption é o domínio de um site externo, caso o post contenha um link externo. Ilustração: http://imgur.com/XS4J9Zc
        self.description é um resumo que aparece abaixo do caption quando você compartilha algo externo. Ilustração: http://imgur.com/XS4J9Zc
        self.feed_targeting é sobre uma função onde um post aparece preferencialmente para um publico particular (escolhido por região, idade, interesse, etc). Só se aplica a páginas, e pouquissimas páginas usam
        self.created_by guarda o ID e Nome do criador do POST
        self.icon guarda o ícone que o facebook usa para aquele tipo de post
        self.is_hidden guarda se o post é marcado como hidden
        self.is_published guarda se o post já foi publicado. (Páginas podem criar postagens e não publicar na hora)
        self.link guarda o link para o post. Caso o post seja um compartilhamento de outro post, então o link é para o post original. Caso seja um compartilhamento de link externo, o link será o link externo
        self.message_tags guarda a lista de usuários e páginas que foram marcadas naquele post
        self.name: De acordo com a documentação do facebook, é o 'Nome do Link'
        self.object_id: O ID de qualquer foto ou vídeo anexado ao post
        self.parent_id: Caso o post seja subpost de outro post maior, terá o ID do post maior
        self.picture: Link direto para a imagem anexada ao post.
        self.place: Caso o usuário marque no post algum local, esse campo terá as informações
        self.privacy: Configurações de privacidade para o post
        self.properties: Caso o post tenha um vídeo anexado, contém propriedades do vídeo
        self.shares: Quantidade de compartilhamentos do post
        self.source: Link direto para um vídeo anexado
        self.status_type: Descrição da ação do post, semelhante a Story. enum{mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, approved_friend}
        self.targeting: Caso seu post seja visível apenas a uma região específica
        self.to: Usuários mensionados ou marcados no post
        self.type: tipo de post. enum{link, status, photo, video, offer}
        self.updated_time: Data-Horário que foi criado, ou editado, ou recebeu seu último comentário. Para posts sobre eventos-de-vida (eg: nascer, casar-se, etc) o horário será o do evento
        self.with_tags: Usuários marcados com o marcador 'com'. (Exemplo: Maria postou uma foto COM joão)
        '''
        self.id=id
        self.admin_creator=list()
        self.created_time = created_time
        self.message=message
        self.story = story
        self.caption=""
        self.description=""
        self.feed_targeting=""
        self.created_by=""
        self.icon=""
        self.is_hidden=""
        self.is_published=""
        self.link=""
        self.from_=""
        self.message_tags=list()
        self.name=""
        self.object_id=""
        self.parent_id=""
        self.picture=""
        self.place=Place()
        self.privacy = Privacy()
        self.properties=list()
        self.shares=0
        self.source=""
        self.status_type="" #enum{mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, approved_friend}
        self.targeting=Targeting()
        self.to=list()
        self.type="" #enum{link, status, photo, video, offer}
        self.updated_time=""
        self.with_tags=list()
        if ("id" in dictionary):
             self.id=dictionary["id"]
        if ("admin_creator" in dictionary):
             for i in dictionary["admin_creator"]:
                self.admin_creator.append(_User.User(dictionary=i))
        if ("application" in dictionary):
             self.application=dictionary["application"]
        if ("call_to_action" in dictionary):
             self.call_to_action=dictionary["call_to_action"]
        if ("caption" in dictionary):
             self.caption=dictionary["caption"]
        if ("created_time" in dictionary):
             self.created_time=dictionary["created_time"]
        if ("description" in dictionary):
             self.description=dictionary["description"]
        if ("feed_targeting" in dictionary):
             self.feed_targeting=Feed_Targeting(dictionary=dictionary["feed_targeting"])
        if ("from" in dictionary):
             self.from_=_User.User(dictionary["from"])
        if ("icon" in dictionary):
             self.icon=dictionary["icon"]
        if ("is_hidden" in dictionary):
             self.is_hidden=dictionary["is_hidden"]
        if ("is_published" in dictionary):
             self.is_published=dictionary["is_published"]
        if ("link" in dictionary):
             self.link=dictionary["link"]
        if ("message" in dictionary):
             self.message=dictionary["message"]
        if ("message_tags" in dictionary):
             self.message_tags=dictionary["message_tags"]
        if ("name" in dictionary):
             self.name=dictionary["name"]
        if ("object_id" in dictionary):
             self.object_id=dictionary["object_id"]
        if ("parent_id" in dictionary):
             self.parent_id=dictionary["parent_id"]
        if ("picture" in dictionary):
             self.picture=dictionary["picture"]
        if ("place" in dictionary):
             self.place=dictionary["place"]
        if ("privacy" in dictionary):
             self.privacy=dictionary["privacy"]
        if ("properties" in dictionary):
             for i in dictionary["properties"]:
                self.properties.append(Properties(dictionary=i))
        if ("shares" in dictionary):
             self.shares=dictionary["shares"]
        if ("source" in dictionary):
             self.source=dictionary["source"]
        if ("status_type" in dictionary):
             self.status_type=dictionary["status_type"]
        if ("story" in dictionary):
             self.story=dictionary["story"]
        if ("story_tags" in dictionary):
             self.story_tags=dictionary["story_tags"]
        if ("targeting" in dictionary):
             self.targeting=dictionary["targeting"]
        if ("to" in dictionary):
             for i in dictionary["to"]:
                self.to.append(_User.User(dictionary=i))
        if ("type" in dictionary):
             self.type=dictionary["type"]
        if ("updated_time" in dictionary):
             self.updated_time=dictionary["updated_time"]
        if ("with_tags" in dictionary):
             self.with_tags=dictionary["with_tags"]

    def __str__(self):
        dic=self.__dict__
        lista=list()
        for key in dic:
         lista.append(key)
        for key in lista:
         if dic[key]==None or dic[key]=="":
             del dic[key]
        return "POST: "+str(dic)



    def createListFromData(posts, limit, dateMin="", dateMax=""):
        lista = list() #lista de posts a ser retornada
        while(posts["data"] and len(posts["data"])>0): #Enquanto houver posts a serem lidos:
            print(len(lista))
            for p in posts['data']:
                print(len(lista))
                if (dateMin!="" and parse(p["created_time"]).replace(tzinfo=None)<dateMin):
                    #O facebook ordena os postrs por data decrescente. Então se temos um post cuja data é menor do que DateMin, daquele post em diante não terá nenhum post que iremos querer
                    return lista
                if(dateMax!="" and parse(p["created_time"]).replace(tzinfo=None)>dateMax):
                    #Se o post for de uma data maior do que dateMax, pulamos pro próximo post
                    continue
                post = Post_Facebook(id=p["id"], created_date=p["created_time"])
                #construimos um objeto da classe post, e adicionamos nele todos os campos que o facebook fornecer, verificando campo a campo se ele existe
                if ("message" in p):
                    post.message=p["message"]
                if ("story" in p):
                    post.story=p["story"]
                if ("caption" in p):
                    post.caption=p["caption"]
                if ("description") in p:
                    post.description=p["description"]
                if ("feed_targeting") in p:
                    post.feed_targeting=Feed_Targeting(p["feed_targeting"])
                if ("from") in p:
                    u = _User.User()
                    u.name=p["from"]["name"]
                    u.id=p["from"]["id"]
                    post.created_by=u
                if ("icon") in p:
                    post.icon=p["icon"]
                if ("is_hidden") in p:
                    post.is_hidden=p["is_hidden"]
                if ("is_published") in p:
                    post.is_published=p["is_published"]
                if ("link") in p:
                    post.link=p["link"]
                if ("message_tags") in p:
                    for m in p["message_tags"]:
                        u = _User.User()
                        if ("name") in m:
                            u.name=m["name"]
                        if ("id") in m:
                            u.id=m["id"]
                        if ("type") in m:
                            u.type=m["type"]
                        post.message_tags.append(u)
                if ("name") in p:
                    post.name=p["name"]
                if ("object_id") in p:
                    post.object_id=p["object_id"]
                if ("parent_id") in p:
                    post.parent_id=p["parent_id"]
                if ("picture") in p:
                    post.picture=p["picture"]
                if ("place") in p:
                    post.place = Place(p["place"])
                if ("privacy") in p:
                    post.privacy=Privacy(p["privacy"])
                if ("properties") in p:
                    post.properties=p["properties"]
                if ("shares") in p:
                    post.shares=p["shares"]["count"]
                if ("source") in p:
                    post.source=p["source"]
                if ("status_type") in p:
                    post.status_type=p["status_type"]
                if ("targeting") in p:
                    post.targeting=Targeting(p["targeting"])
                if ("to") in p:
                    for user in p["to"]["data"]:
                        u = _User.User()
                        u.name=user["name"]
                        u.id=user["id"]
                        post.to.append(u)
                if ("type") in p:
                    post.type=p["type"]
                if ("updated_time") in p:
                    post.updated_time=p["updated_time"]
                if ("with_tags") in p:
                    for user in p["with_tags"]["data"]:
                        u = _User.User()
                        u.name=user["name"]
                        u.id=user["id"]
                        post.with_tags.append(u)
                #Adicionamos o post à lista
                lista.append(post)
                #Se a lista atingiu o tamanho limite, termina a função. (Se limite=-1, então não há limite)
                if (len(lista)>=limit and limit!=-1):
                    return lista
            #Pega a próxima página de posts
            i=0
            while (i<100):
                try:
                    posts=requests.get(posts["paging"]["next"],timeout=(10, 10)).json()
                    break
                except:
                    print("erro "+str(i))
                    i=i+1

            print(len(lista))
        return lista



    def getLikes(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(_User.User(dictionary=a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def getLikesCount(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"?fields=likes.summary(true)&access_token="+token, timeout=timeout).json()
         return r["likes"]["summary"]["total_count"]


    def postLike(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         r=requests.post("https://graph.facebook.com/v2.6/"+self.id+"/likes?&access_token="+token, timeout=timeout).json()
         return str(r)

    def getReactions(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/reactions?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(a)
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def getAttachments(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token
         #print("token="+str(token))
         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Attachments?&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Story_Attachment(a))
             if ("paging" in r and "next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def getComments(self,token=None, timeout=(5,5), maxRetries=50):
         if (token==None):
            token=_Settings.token

         r=_Utility.prepareRequest(maxRetries=maxRetries).get("https://graph.facebook.com/v2.6/"+self.id+"/Comments?fields=id,attachment,can_comment,can_remove,can_like,comment_count,created_time,from,like_count,message,message_tags,object,parent,user_likes,is_hidden&access_token="+token, timeout=timeout).json()
         lista=list()
         while ("data" in r and len(r["data"])>0):
             for a in r["data"]:
                 lista.append(Comment(a))
             if ("next" in r["paging"]):
                 r=_Utility.prepareRequest(maxRetries=maxRetries).get(r["paging"]["next"], timeout=timeout).json()
             else:
                 break
         return lista

    def postComment(self, message, token=None, Localpath=None, FileURL=None):
         if (token==None):
            token=_Settings.token
         if (Localpath==None and FileURL==None):
             params={"message":message}
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/comments?&access_token="+token
             s=requests.post(graphurl, params=params).json()
         if (Localpath!=None and FileURL!=None):
             raise Exception("You cannot use a LocalPath and a URL at same time. Use only one of them")
         if (Localpath!=None and FileURL==None):

             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/comments?&access_token="+token
             files={'file':open(Localpath,'rb')}
             params={"message":message}
             s=requests.post(graphurl, files=files,params=params).json()

             return s
         if (Localpath==None and FileURL!=None):
             graphurl="https://graph.facebook.com/v2.6/"+self.id+"/comments?&access_token="+token
             params={"message":message}
             params["attachment_url"]=FileURL
             return requests.post(graphurl,params=params).json()


