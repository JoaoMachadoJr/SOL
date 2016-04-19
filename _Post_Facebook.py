__author__ = 'Joao'
import requests
import _User_Facebook
from dateutil.parser import parse
from _Facebook_Classes import *

class Post_Facebook: #Classe para os POSTs das redes sociais
    def __init__(self, id=-1, created_date="", message="", story=""):
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
        self.created_date = created_date
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
        self.message_tags=list()
        self.name=""
        self.object_id=""
        self.parent_id=""
        self.picture=""
        self.place=Place()
        self.privacy = Privacy()
        self.properties=dict()  #Dictonary fields: 'text', 'name', 'href';
        self.shares=0
        self.source=""
        self.status_type="" #enum{mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, approved_friend}
        self.targeting=Targeting()
        self.to=list()
        self.type="" #enum{link, status, photo, video, offer}
        self.updated_time=""
        self.with_tags=list()

    def __str__(self):
        retorno= "POST: [ID="+self.id+"\nCreated_date: "+ self.created_date
        if (self.story!=""):
            retorno+="\nStory: "+self.story.rstrip('\n')
        if(self.message!=""):
            retorno+="\nMessage: "+self.message.rstrip('\n')
        if (self.feed_targeting!=""):
            retorno+="\nFeed_Targeging: "+str(self.feed_targeting).rstrip('\n')
        if (self.created_by!=""):
            retorno+="\nFrom: "+str(self.created_by).rstrip('\n')
        if (self.icon!=""):
            retorno+="\nIcon: "+str(self.icon).rstrip('\n')
        if (self.is_hidden!=""):
            retorno+="\nIs_hidden: "+str(self.is_hidden).rstrip('\n')
        if (self.is_published!=""):
            retorno+="\nIs_published: "+str(self.is_published).rstrip('\n')
        if (self.link!=""):
            retorno+="\nLink: "+str(self.link).rstrip('\n')
        if (self.message_tags!=""):
            retorno+="\nMessage_tags: "+"; ".join(str(u) for u in self.message_tags).rstrip('\n')
        if (self.name!=""):
            retorno+="\nName: "+str(self.name).rstrip('\n')
        if (self.object_id!=""):
            retorno+="\nObject_id: "+str(self.object_id).rstrip('\n')
        if (self.parent_id!=""):
            retorno+="\nParent_id: "+str(self.parent_id).rstrip('\n')
        if (self.picture!=""):
            retorno+="\nPicture: "+str(self.picture).rstrip('\n')
        if (self.place!=""):
            retorno+="\nPlace: "+str(self.place).rstrip('\n')
        if (self.privacy!=""):
            retorno+="\nPrivacy: "+str(self.privacy).rstrip('\n')
        if (self.properties!=""):
            retorno+="\nProperties: "+str(self.properties).rstrip('\n')
        if (self.shares!=""):
            retorno+="\nShares: "+str(self.shares).rstrip('\n')
        if (self.source!=""):
            retorno+="\nSource: "+str(self.source).rstrip('\n')
        if (self.status_type!=""):
            retorno+="\nStatus_type: "+str(self.status_type).rstrip('\n')
        if (self.targeting!=""):
            retorno+="\nTargeting: "+str(self.targeting).rstrip('\n')
        if (self.to!=""):
            retorno+="\nTo: "+"; ".join(str(u) for u in self.to).rstrip('\n')
        if (self.type!=""):
            retorno+="\nType: "+str(self.type).rstrip('\n')
        if (self.updated_time!=""):
            retorno+="\nUpdated_time: "+str(self.updated_time).rstrip('\n')
        if (self.with_tags!=""):
            retorno+="\nWith_tags: "+"; ".join(str(u) for u in self.with_tags).rstrip('\n')
        return retorno+"]\n\n"



    def createListFromData(posts, limit, dateMin="", dateMax=""):
        lista = list() #lista de posts a ser retornada
        while(posts["data"] and len(posts["data"])>0): #Enquanto houver posts a serem lidos:
            for p in posts['data']:
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
                    u = _User_Facebook.User_Facebook()
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
                        u = _User_Facebook.User_Facebook()
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
                        u = _User_Facebook.User_Facebook()
                        u.name=user["name"]
                        u.id=user["id"]
                        post.to.append(u)
                if ("type") in p:
                    post.type=p["type"]
                if ("updated_time") in p:
                    post.updated_time=p["updated_time"]
                if ("with_tags") in p:
                    for user in p["with_tags"]["data"]:
                        u = _User_Facebook.User_Facebook()
                        u.name=user["name"]
                        u.id=user["id"]
                        post.with_tags.append(u)
                #Adicionamos o post à lista
                lista.append(post)
                #Se a lista atingiu o tamanho limite, termina a função. (Se limite=-1, então não há limite)
                if (len(lista)>=limit and limit!=-1):
                    return lista
            #Pega a próxima página de posts
            posts=requests.get(posts["paging"]["next"]).json()
        return lista



