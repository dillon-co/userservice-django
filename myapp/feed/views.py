from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Demographics
import json

# Create your views here.

def demographics_context():
    if Demographics.objects.all().count() > 0:
        m_c, f_c, o_c = Demographics.objects.all().last().male_count, Demographics.objects.all().last().female_count, Demographics.objects.all().last().other_count
    else:
        m_c, f_c, o_c = 0,0,0

    context = {
        'male_count':m_c,
        'female_count':f_c,
        'other_count':o_c,
        'user_ids':list(User.objects.all().values_list('id', flat=True))
    }
    return context


def home(request):
    context = demographics_context()
    return render(request, 'feed/home.html', context)

# def base(request)
def view_demographics(request):
    response = json.dumps([demographics_context()])
    return HttpResponse(response, content_type='text/json')
