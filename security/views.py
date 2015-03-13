# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def login_view(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                data = {'msg': 'Ingrese credenciales correctas'}
                return render_to_response('login.html',
                                          context_instance= RequestContext(request, data))
        else:
            return render_to_response('login.html',
                                      context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('login')