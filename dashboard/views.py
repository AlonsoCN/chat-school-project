# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from dashboard.models import Section
from firebase_token_generator import create_token
from s3k_school.config import FIREBASE_SECRET


@login_required
def dashboard_view(request):
    section = Section.objects.get(user_section__user=request.user)
    display_name = 'Padre de ' + request.user.first_name + ' ' + request.user.last_name
    token = __get_firebase_token(request)
    data = {
        'grade': section.grade,
        'section': section.name,
        'username': request.user.username,
        'token': token,
        'display_name': display_name
    }
    return render_to_response('index.html', context_instance=RequestContext(request, data))

def __get_firebase_token(request):
    auth_payload = {"uid": str(request.user.id)}
    return create_token(FIREBASE_SECRET, auth_payload)