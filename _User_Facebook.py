__author__ = 'Joao'
import _User
#import pip
#pip.main(['install', 'https://github.com/pythonforfacebook/facebook-sdk/archive/master.zip'])
#import facebook
import requests
import _Post_Facebook
User=_User.User


class User_Facebook(User):
    '''Essa é a classe de usuários para facebook.
    A autenticação é feita por um Token, que deve ser obtido no site do facebook'''


    def __init__(self, token=""):
        '''O construtor pode receber o token de acesso, ou não receber nada
        Caso o construtor já receba o token, ele fará a conexão de uma vez
        Descriçao dos campos: https://developers.facebook.com/docs/graph-api/reference/user/
        toekn (String): Token de acesso
        type (String): Tipo: {user, page, group}
        id (String numérica): ID numérico do usuário njo facebook
        age_range (dictionary: ["min", "max"]): Intervalo de idades que o usuário pode ter, baseado no seu ano de nascimento
        bio (String): Biografia
        birthday (String): Aniversário
        context (dictionary:["id","all_mutual_friends","mutual_friends","mutual_likes","three_degree_mutual_friends"]): Contexto social. Mais informações:https://developers.facebook.com/docs/graph-api/reference/user-context/
        cover (dictionary:["id","cover_id","offset_x","offset_y","source"]): Foto de capa do usuário
        currency (dictionary:["currency_offset","usd_exchange","usd_exchange_inverse","user_currency"]): Informações sobre a moeda do país do usuário
        devices(list): Lista de dispositivos do usuário
        education(list): Lista de instituições onde o usuário estudou
        email(string): Email do usuário
        favorite_athletes(list): Lista de atletas favoritos
        favorite_teams(list): Lista de times favoritos
        first_name(string): Primeiro nome
        gender(string): Gênero
        hometown(page): cidade natal
        inspirational_people(list): Lista de ídolos
        install_type(string); É um ENUM, porém mal documentado
        installed(bool): Informa se um APP especifico está instalado
        interested_in (list): Lista de gêneros nos quais o usuário tem interesse
        is_shared_login (bool): Se é um login compartilhado
        is_verified (bool): Se é um usuário verificado
        labels (list): Algumas etiquetas que o usuário pode ter
        languages (list): Idiomas que o usuário fala
        last_name (String): Sobrenome
        link (String): Link para o feed do usuário
        locale (locale): locale do usuário
        location (page): Local do usuário
        meeting_for(list de string): mal documentado
        middle_name(string): Nome do meio
        name(String): Nome completo
        name_format(String): O formato como o nome deve aparecer
        payment_pricepoints(dictionary["mobile"]): Mal documentado
        political(String): Posição política
        public_key(String): Chave pública de criptografia
        quotes(Sring): Citações favoritas
        relationship_status(String): Status de relacionamento
        religion(String): Religião
        security_settings(dictionary["secure_browsing"])
        significant_other(User): Pessoa marcada como significant_other do usuário (esposo, melhor amigo, namorada, etc)
        sports(list): Lista de esportes de interesse do usuário
        test_group(int): Mal documentado
        third_party_id(string): Id anonimo e irrastreavel
        timezone(float): A zona temnporal do usuário
        updated_time(datetime): ultimo update
        verified(bool): Se o usuário é verificadoThis is distinct from the is_verified field. Someone is considered verified if they take any of the following actions: Register for mobile ,Confirm their account via SMS ,Enter a valid credit card
        video_upload_limits(dictionary["lenght","size"]): Mal documentado
        viewer_can_send_gift(bool): Se está apto a receber um 'gift'
        website(string): Site do usuário
        work(list): Lista de empregos presentes e passados

        '''

        super(User_Facebook,self).__init__()
        self.token = token
        self.type=""
        self.id=""
        self.about=""
        self.age_range=""
        self.bio=""
        self.birthday=""
        self.context=""
        self.cover=""
        self.currency=""
        self.devices=""
        self.education=""
        self.email=""
        self.favorite_athletes=""
        self.favorite_teams=""
        self.first_name=""
        self.gender=""
        self.hometown=""
        self.inspirational_people=""
        self.install_type=""
        self.installed=""
        self.interested_in=""
        self.is_shared_login=""
        self.is_verified=""
        self.labels=""
        self.languages=""
        self.last_name=""
        self.link=""
        self.locale=""
        self.location=""
        self.meeting_for=""
        self.middle_name=""
        self.name=""
        self.name_format=""
        self.payment_pricepoints=""
        self.political=""
        self.public_key=""
        self.quotes=""
        self.relationship_status=""
        self.religion=""
        self.security_settings=""
        self.shared_login_upgrade_required_by=""
        self.significant_other=""
        self.sports=""
        self.test_group=""
        self.third_party_id=""
        self.timezone=""
        self.updated_time=""
        self.verified=""
        self.video_upload_limits=""
        self.viewer_can_send_gift=""
        self.website=""
        self.work=""
        if (token!=""):
            self.connect()



    def connect(self):
        '''Esse método faz a conexão com o sistema do facebook, portanto é necessário
        que usuario.token possua um token válido.'''

        #self.connection = facebook.GraphAPI(access_token=self.token)
        dict_user=requests.get("https://graph.facebook.com/v2.6/me?&fields=id,about,age_range,bio,birthday,context,cover,currency,devices,education,email,favorite_athletes,favorite_teams,first_name,gender,hometown,inspirational_people,install_type,installed,interested_in,is_shared_login,is_verified,languages,last_name,link,locale,location,meeting_for,middle_name,name,name_format,payment_pricepoints,political,public_key,quotes,relationship_status,religion,security_settings,shared_login_upgrade_required_by,significant_other,sports,test_group,third_party_id,timezone,updated_time,verified,video_upload_limits,viewer_can_send_gift,website,work&access_token="+self.token).json()

        if ("id") in dict_user:
             self.id=dict_user["id"]
        if ("about") in dict_user:
             self.about=dict_user["about"]
        if ("admin_notes") in dict_user:
             self.admin_notes=dict_user["admin_notes"]
        if ("age_range") in dict_user:
             self.age_range=dict_user["age_range"]
        if ("bio") in dict_user:
             self.bio=dict_user["bio"]
        if ("birthday") in dict_user:
             self.birthday=dict_user["birthday"]
        if ("context") in dict_user:
             self.context=dict_user["context"]
        if ("cover") in dict_user:
             self.cover=dict_user["cover"]
        if ("currency") in dict_user:
             self.currency=dict_user["currency"]
        if ("devices") in dict_user:
             self.devices=dict_user["devices"]
        if ("education") in dict_user:
             self.education=dict_user["education"]
        if ("email") in dict_user:
             self.email=dict_user["email"]
        if ("favorite_athletes") in dict_user:
             self.favorite_athletes=dict_user["favorite_athletes"]
        if ("favorite_teams") in dict_user:
             self.favorite_teams=dict_user["favorite_teams"]
        if ("first_name") in dict_user:
             self.first_name=dict_user["first_name"]
        if ("gender") in dict_user:
             self.gender=dict_user["gender"]
        if ("hometown") in dict_user:
             self.hometown=dict_user["hometown"]
        if ("inspirational_people") in dict_user:
             self.inspirational_people=dict_user["inspirational_people"]
        if ("install_type") in dict_user:
             self.install_type=dict_user["install_type"]
        if ("installed") in dict_user:
             self.installed=dict_user["installed"]
        if ("interested_in") in dict_user:
             self.interested_in=dict_user["interested_in"]
        if ("is_shared_login") in dict_user:
             self.is_shared_login=dict_user["is_shared_login"]
        if ("is_verified") in dict_user:
             self.is_verified=dict_user["is_verified"]
        if ("labels") in dict_user:
             self.labels=dict_user["labels"]
        if ("languages") in dict_user:
             self.languages=dict_user["languages"]
        if ("last_name") in dict_user:
             self.last_name=dict_user["last_name"]
        if ("link") in dict_user:
             self.link=dict_user["link"]
        if ("locale") in dict_user:
             self.locale=dict_user["locale"]
        if ("location") in dict_user:
             self.location=dict_user["location"]
        if ("meeting_for") in dict_user:
             self.meeting_for=dict_user["meeting_for"]
        if ("middle_name") in dict_user:
             self.middle_name=dict_user["middle_name"]
        if ("name") in dict_user:
             self.name=dict_user["name"]
        if ("name_format") in dict_user:
             self.name_format=dict_user["name_format"]
        if ("payment_pricepoints") in dict_user:
             self.payment_pricepoints=dict_user["payment_pricepoints"]
        if ("political") in dict_user:
             self.political=dict_user["political"]
        if ("public_key") in dict_user:
             self.public_key=dict_user["public_key"]
        if ("quotes") in dict_user:
             self.quotes=dict_user["quotes"]
        if ("relationship_status") in dict_user:
             self.relationship_status=dict_user["relationship_status"]
        if ("religion") in dict_user:
             self.religion=dict_user["religion"]
        if ("security_settings") in dict_user:
             self.security_settings=dict_user["security_settings"]
        if ("shared_login_upgrade_required_by") in dict_user:
             self.shared_login_upgrade_required_by=dict_user["shared_login_upgrade_required_by"]
        if ("significant_other") in dict_user:
             self.significant_other=dict_user["significant_other"]
        if ("sports") in dict_user:
             self.sports=dict_user["sports"]
        if ("test_group") in dict_user:
             self.test_group=dict_user["test_group"]
        if ("third_party_id") in dict_user:
             self.third_party_id=dict_user["third_party_id"]
        if ("timezone") in dict_user:
             self.timezone=dict_user["timezone"]
        if ("updated_time") in dict_user:
             self.updated_time=dict_user["updated_time"]
        if ("verified") in dict_user:
             self.verified=dict_user["verified"]
        if ("video_upload_limits") in dict_user:
             self.video_upload_limits=dict_user["video_upload_limits"]
        if ("viewer_can_send_gift") in dict_user:
             self.viewer_can_send_gift=dict_user["viewer_can_send_gift"]
        if ("website") in dict_user:
             self.website=dict_user["website"]
        if ("work") in dict_user:
             self.work=dict_user["work"]




    def getMyPosts(self, dateMin="", dateMax="", limit=100):
        '''Essa função irá retornar os posts do usuário.
        Os parâmetros são duas datas e um limite, e a função irá retornar os posts publicados entre as datas
        Caso você use a função sem espécificar datas, a função irá retornar 25 posts mais recentes
        A quantidade de posts retornados será de no máximo o limite passado como parametro.
        Para receber um número ilimitado de posts, faça limite=-1'''
        if ((dateMin!="" and dateMax=="") or (dateMax!="" and dateMin=="")):
            raise Exception("ERROR: You should use both DateMin AND DateMax, or use no one")
        posts= requests.get("https://graph.facebook.com/v2.5/me/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&access_token="+self.token).json()
        lista= _Post_Facebook.Post_Facebook.createListFromData(posts, limit,dateMin,dateMax)
        return lista



    def __str__(self):
        return "USER:[name=<"+self.name+">; id=<"+self.id+">; token=<"+self.token+">; Type=<"+self.type+">]"



    def getPostsFromPage(self, id, dateMin="", dateMax="", limit=100):
        meta=requests.get("https://graph.facebook.com/v2.3/"+id+"?metadata=1&access_token="+self.token).json()
        meta=meta["metadata"]["type"]
        if(meta!="page"):
            raise Exception("ERROR: This ID is not from a page")
        posts=requests.get("https://graph.facebook.com/v2.5/"+id+"/posts?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&access_token="+self.token).json()
        lista= _Post_Facebook.Post_Facebook.createListFromData(posts, limit,dateMin,dateMax)
        return lista



    def getPostsFromGroup(self, id, dateMin="", dateMax="", limit=100):
        if (not id.isdigit()):
            id2=requests.get("https://graph.facebook.com/search?q="+id+"&type=group&access_token="+self.token).json()
            id=id2["data"][0]["id"]
        meta=requests.get("https://graph.facebook.com/v2.3/"+id+"?metadata=1&access_token="+self.token).json()
        print(meta)
        meta=meta["metadata"]["type"]
        if(meta!="group"):
            raise Exception("ERROR: This ID is not from a group")
        posts=requests.get("https://graph.facebook.com/v2.5/"+id+"/feed?fields=id,caption,created_time,description,feed_targeting,from,icon,is_hidden,is_published,link,message,message_tags,name,object_id,parent_id,picture,place,privacy,properties,shares,source,status_type,story,targeting,to,type,updated_time,with_tags&access_token="+self.token).json()
        lista= _Post_Facebook.Post_Facebook.createListFromData(posts, limit,dateMin,dateMax)
        return lista

    def longstr(self):
        retorno=""
        if (self.id!=""):
             retorno+="ID: <"+str(self.id)+">\n"
        if (self.about!=""):
             retorno+="ABOUT: <"+str(self.about)+">\n"
        if (self.age_range!=""):
             retorno+="AGE_RANGE: <"+str(self.age_range)+">\n"
        if (self.bio!=""):
             retorno+="BIO: <"+str(self.bio)+">\n"
        if (self.birthday!=""):
             retorno+="BIRTHDAY: <"+str(self.birthday)+">\n"
        if (self.context!=""):
             retorno+="CONTEXT: <"+str(self.context)+">\n"
        if (self.cover!=""):
             retorno+="COVER: <"+str(self.cover)+">\n"
        if (self.currency!=""):
             retorno+="CURRENCY: <"+str(self.currency)+">\n"
        if (self.devices!=""):
             retorno+="DEVICES: <"+str(self.devices)+">\n"
        if (self.education!=""):
             retorno+="EDUCATION: <"+str(self.education)+">\n"
        if (self.email!=""):
             retorno+="EMAIL: <"+str(self.email)+">\n"
        if (self.favorite_athletes!=""):
             retorno+="FAVORITE_ATHLETES: <"+str(self.favorite_athletes)+">\n"
        if (self.favorite_teams!=""):
             retorno+="FAVORITE_TEAMS: <"+str(self.favorite_teams)+">\n"
        if (self.first_name!=""):
             retorno+="FIRST_NAME: <"+str(self.first_name)+">\n"
        if (self.gender!=""):
             retorno+="GENDER: <"+str(self.gender)+">\n"
        if (self.hometown!=""):
             retorno+="HOMETOWN: <"+str(self.hometown)+">\n"
        if (self.inspirational_people!=""):
             retorno+="INSPIRATIONAL_PEOPLE: <"+str(self.inspirational_people)+">\n"
        if (self.install_type!=""):
             retorno+="INSTALL_TYPE: <"+str(self.install_type)+">\n"
        if (self.installed!=""):
             retorno+="INSTALLED: <"+str(self.installed)+">\n"
        if (self.interested_in!=""):
             retorno+="INTERESTED_IN: <"+str(self.interested_in)+">\n"
        if (self.is_shared_login!=""):
             retorno+="IS_SHARED_LOGIN: <"+str(self.is_shared_login)+">\n"
        if (self.is_verified!=""):
             retorno+="IS_VERIFIED: <"+str(self.is_verified)+">\n"
        if (self.labels!=""):
             retorno+="LABELS: <"+str(self.labels)+">\n"
        if (self.languages!=""):
             retorno+="LANGUAGES: <"+str(self.languages)+">\n"
        if (self.last_name!=""):
             retorno+="LAST_NAME: <"+str(self.last_name)+">\n"
        if (self.link!=""):
             retorno+="LINK: <"+str(self.link)+">\n"
        if (self.locale!=""):
             retorno+="LOCALE: <"+str(self.locale)+">\n"
        if (self.location!=""):
             retorno+="LOCATION: <"+str(self.location)+">\n"
        if (self.meeting_for!=""):
             retorno+="MEETING_FOR: <"+str(self.meeting_for)+">\n"
        if (self.middle_name!=""):
             retorno+="MIDDLE_NAME: <"+str(self.middle_name)+">\n"
        if (self.name!=""):
             retorno+="NAME: <"+str(self.name)+">\n"
        if (self.name_format!=""):
             retorno+="NAME_FORMAT: <"+str(self.name_format)+">\n"
        if (self.payment_pricepoints!=""):
             retorno+="PAYMENT_PRICEPOINTS: <"+str(self.payment_pricepoints)+">\n"
        if (self.political!=""):
             retorno+="POLITICAL: <"+str(self.political)+">\n"
        if (self.public_key!=""):
             retorno+="PUBLIC_KEY: <"+str(self.public_key)+">\n"
        if (self.quotes!=""):
             retorno+="QUOTES: <"+str(self.quotes)+">\n"
        if (self.relationship_status!=""):
             retorno+="RELATIONSHIP_STATUS: <"+str(self.relationship_status)+">\n"
        if (self.religion!=""):
             retorno+="RELIGION: <"+str(self.religion)+">\n"
        if (self.security_settings!=""):
             retorno+="SECURITY_SETTINGS: <"+str(self.security_settings)+">\n"
        if (self.shared_login_upgrade_required_by!=""):
             retorno+="SHARED_LOGIN_UPGRADE_REQUIRED_BY: <"+str(self.shared_login_upgrade_required_by)+">\n"
        if (self.significant_other!=""):
             retorno+="SIGNIFICANT_OTHER: <"+str(self.significant_other)+">\n"
        if (self.sports!=""):
             retorno+="SPORTS: <"+str(self.sports)+">\n"
        if (self.test_group!=""):
             retorno+="TEST_GROUP: <"+str(self.test_group)+">\n"
        if (self.third_party_id!=""):
             retorno+="THIRD_PARTY_ID: <"+str(self.third_party_id)+">\n"
        if (self.timezone!=""):
             retorno+="TIMEZONE: <"+str(self.timezone)+">\n"
        if (self.updated_time!=""):
             retorno+="UPDATED_TIME: <"+str(self.updated_time)+">\n"
        if (self.verified!=""):
             retorno+="VERIFIED: <"+str(self.verified)+">\n"
        if (self.video_upload_limits!=""):
             retorno+="VIDEO_UPLOAD_LIMITS: <"+str(self.video_upload_limits)+">\n"
        if (self.viewer_can_send_gift!=""):
             retorno+="VIEWER_CAN_SEND_GIFT: <"+str(self.viewer_can_send_gift)+">\n"
        if (self.website!=""):
             retorno+="WEBSITE: <"+str(self.website)+">\n"
        if (self.work!=""):
             retorno+="WORK: <"+str(self.work)+">\n"
        return retorno

    def getMyFriends(self):
        friends=requests.get("https://graph.facebook.com/v2.6/me/friendlists?&access_token="+self.token).json()
        for f in friends["data"]:
            print(f)
        return