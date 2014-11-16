from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
import requests
import urlparse
from settings import *
import copy

from django.core.exceptions import ObjectDoesNotExist
from models import *

#invoked when the url pattern is "/"
def home(request):
    #the post request occurs when the form is filled and submitted

    if request.method == 'POST': #redirect to "/bulletin" for post request

        #request.POST <---list
        """
        if request.POST is not None:

            request_email = request.POST['email']
            request_password = request.POST['password']


            try:
                temp = User.objects.filter(login=request_email, password=request_password)
                if len(temp)==1:
                    request.session['user_id'] = request_email


                    return HttpResponseRedirect('/bulletin')
                else:
                    return HttpResponse("email or password is incorrect.")
            except:
                return HttpResponse("email or password is incorrect.")
        """
    #the get request occurs when the page is loaded
    if request.method == "GET":
        template = loader.get_template('login/index.html') #creates a template object from the html file
        context = RequestContext(request, {})




        return HttpResponse(template.render(context)) #return the http response that includes the html page




##########################   login start  ####################################

def facebook_login(request):

    if not (has_code(request) or has_token(request)):
        #get the code!
        state_url_fragment = "&state={}".format("a") #not safe, fix this!
        return HttpResponseRedirect(facebook_login_url_base+state_url_fragment)
    elif not has_token(request):
        #get the token!
        code_url_fragment = "&code={}".format(request.GET["code"])


        r = requests.get(facebook_token_url_base+code_url_fragment)
        print "after getting access token"
        token = urlparse.parse_qs(r.text)['access_token']
        token = token[0]

        if not is_valid(token):

            return HttpResponseRedirect(home_page)
        else:

            #we know that the this user is proper so we now set up our db based on this user. If user already exists, then we can update his stuff.

            user_data = get_user_data(token)
            try:
                #if this works, then there is only 1 thing in db with given fb_id
                User.objects.get(fb_id=user_data['id'])


            except ObjectDoesNotExist:
                #create user
                User(name=user_data['name'], fb_id=user_data['id'], fb_token=str(token)).save()

            #get friends of user
            friends = get_friends_for_user(token)
            friends = friends['data']
            for k in friends:
                try:
                    User.objects.get(fb_id=k['id'])
                except ObjectDoesNotExist:
                    User(name=k['name'], fb_id=k['id']).save()

                try:
                    Friend.objects.get(fb_id=user_data['id'], friend_fb_id = k['id'])
                except ObjectDoesNotExist:
                    Friend(fb_id=user_data['id'], friend_fb_id = k['id']).save()







            request.session['user_id'] = user_data['id']
            return HttpResponseRedirect(member_page)


            # login page -
            # home page  -
    else:
        #proceed to members homepage
        print('already has token')
        pass

def has_code(request):
    return "code" in request.GET

def has_token(request):
    return "token" in request.GET


def is_valid(token):
    print "is valid is the problem..."
    data = get_validation_data(token).json()
    data = data['data']
    return data['is_valid'] is True and str(data['app_id']) == str(app_id)

def get_validation_data(token):
    input_token_fragment = "?input_token={}".format(token)
    request_url = validation_url_base + input_token_fragment + "&access_token=" + str(get_app_access_token())
    #print "requesturl" + request_url
    data = requests.get(request_url)
    return data

def get_app_access_token():
    #print facebook_app_token_url
    r = requests.get(facebook_app_token_url)
    token = urlparse.parse_qs(r.text)['access_token']
    token = token[0]
    return token

def get_user_data(token):
    r = requests.get(get_user_info_url+"access_token="+token)
    return r.json()


def get_friends_for_user(token):
    r=requests.get(get_user_friends_url+"access_token="+token)
    return r.json()

######################   login end     #################################


def member(request):
    template = loader.get_template('login/member.html') #creates a template object from the html file
    print request.session['user_id']
    compliments = Compliment.objects.filter(compliment_for=request.session['user_id'])
    friends = get_friends_for_internal_user(request.session['user_id'])
    for compliment in compliments:
        compliment.compliment_by = str(User.objects.get(fb_id = compliment.compliment_by)).split(':')[0]

    for k in compliments:
        print k.compliment
        print k.compliment_by
        print k.compliment_for

    context = RequestContext(request, {
        'name':"himanshu",
        'compliments':compliments,
        'num_compliments':len(compliments),
        'friends':friends
    })
    return HttpResponse(template.render(context)) #return the http response that includes the html page

def get_friends_for_internal_user(user_id):
    records = Friend.objects.filter(fb_id=user_id)
    print records
    friends_of = {}
    for friendship in records:
        print friendship.friend_fb_id
        print friendship.fb_id
        try:
            friend_record = User.objects.get(fb_id=str(friendship.friend_fb_id))
            print "success sucka"
        except:
            print friendship.friend_fb_id
            print User.objects.filter(fb_id=str(friendship.friend_fb_id))
            #print friend_record
            #friend_record = friend_record[0]
        friends_of[friend_record.fb_id] = friend_record.name

    return friends_of


def save_compliment(request):
    try:
        Compliment(compliment=request.POST['compliment'],compliment_by=request.session['user_id'], compliment_for=request.POST['compliment_for'] ).save()
        return HttpResponseRedirect(member_page)
    except:
        print "duddeeeeeee, it didnt work"
