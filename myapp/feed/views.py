from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Demographics

# Create your views here.




def home(request):
    if Demographics.objects.all().count() > 0:
        m_c, f_c, o_c = Demographics.objects.all().last().male_count, Demographics.objects.all().last().female_count, Demographics.objects.all().last().other_count
    else:
        m_c, f_c, o_c = 0,0,0

    context = {
        'male_count':m_c,
        'female_count':f_c,
        'other_count':o_c,
        'user_ids':User.objects.all().values_list('id', flat=True)
    }
    return render(request, 'feed/home.html', context)

# def base(request)
