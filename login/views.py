from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect

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
