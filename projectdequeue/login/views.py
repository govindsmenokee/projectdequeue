from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

def userlogin(request):
    if request.method=='GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        elif 'e' in request.GET:
            return render_to_response('login_index.html',{'error':'1'}, context_instance=RequestContext(request))
        else:
            return render_to_response('login_index.html',{}, context_instance=RequestContext(request))
    else:
        user=authenticate(username=request.POST['uname'],password=request.POST['passwd'])
        if user is not None and user.is_active:
            login(request,user)
            return HttpResponseRedirect('/welcome')
        else:
            return HttpResponseRedirect('/?e=1')

@login_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    ret={}
    if 'message' in request.GET:
        ret={'message':request.GET['message']}
    ret['c']=user.objects.get(user=request.user)
    return render_to_response('home.html',ret, context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def welcome(request):
	if request.user.is_authenticated():
          return HttpResponseRedirect('/view_film')
	else:
            return HttpResponseRedirect('/?e=1')
