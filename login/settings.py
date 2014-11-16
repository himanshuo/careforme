__author__ = 'himanshu'

home_page = "http://localhost:8000/"

app_id = "1578751839011228"
redirect_uri = home_page + "facebook_login"
app_secret = "7c664f1704dcc0ca389e631d255ca953"
scope="public_profile,user_friends"
facebook_login_url_base = "https://www.facebook.com/dialog/oauth?client_id={}&redirect_uri={}&scope={}".format(app_id,redirect_uri,scope)

facebook_token_url_base = "https://graph.facebook.com/oauth/access_token?client_id={}&redirect_uri={}&client_secret={}".format(app_id,redirect_uri,app_secret)

validation_url_base = "https://graph.facebook.com/debug_token"

facebook_app_token_url = "https://graph.facebook.com/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials".format(app_id,app_secret)

member_page = home_page + "member"


get_user_info_url = "https://graph.facebook.com/v2.2/me?format=json&"

get_user_friends_url = "https://graph.facebook.com/v2.2/me/friends?format=json&"