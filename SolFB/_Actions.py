__author__ = 'Joao'
import requests

#Variaveis globais

class Actions:
    global token
    token=""

    def debugToken(token):
        r=requests.get("https://graph.facebook.com/v2.6/debug_token?input_token="+token+"&access_token="+token).json()
        return r

    def me(token, asDict = False):
        '''Esse método faz a conexão com o sistema do facebook, portanto é necessário
        que usuario.token possua um token válido.'''

        import requests
        from SolFB import _FacebookUser
        dict_user = requests.get(
            "https://graph.facebook.com/v2.6/me?&fields=id,about,age_range,bio,birthday,context,cover,currency,devices,education,email,favorite_athletes,favorite_teams,first_name,gender,hometown,inspirational_people,install_type,installed,interested_in,is_shared_login,is_verified,languages,last_name,link,locale,location,meeting_for,middle_name,name,name_format,payment_pricepoints,political,public_key,quotes,relationship_status,religion,security_settings,shared_login_upgrade_required_by,significant_other,sports,test_group,third_party_id,timezone,updated_time,verified,video_upload_limits,viewer_can_send_gift,website,work&access_token=" + str(
                token)).json()
        if asDict:
            return dict_user
        return _FacebookUser.AuthenticatedFacebookUser(dictionary=dict_user)