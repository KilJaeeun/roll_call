from django.views.decorators.http import require_POST


from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
# 분야
from django.views.decorators.http import require_POST
from rest_framework.utils import json
# path('floor/list/<int:pk>/', views.floor, name='list'),
# path('floor/ans/<int:pk>/', views.floor_ans, name='ans'),
# path('floor/ans_all/<int:pk>/', views.ans_all, name='ans_all'),

from roll_call.models import *
from roll_call.tests import *
#층 전체 리스트
def floor_list(request):
    context={}
    floor_list=FloorManager.objects.all()
    return render(request, 'roll_call/floor_list.html', context)

def roll_call(request, pk):
    context={}
    context['status']=tests.status
    try:
        context['students']=Student.objects.filter(floor_num=pk)
    except:
        context['students'] =''
    return render(request, 'roll_call/roll_call.html', context)
    #
    # if request.method == 'POST':
    #     category.name = request.POST['name']
    #     category.sex = request.POST['sex']
    #     category.cell_phone = request.POST['cell_phone']
    #     category.test = request.POST['test']
    #     category.test_num = request.POST['test_num']
    #     category.jeon_gwan_bool = request.POST['jeon_gwan_bool']
    #     category.pro_lawyer_bool = request.POST['pro_lawyer_bool']
    #     category.big_law_firm_bool = request.POST['big_law_firm_bool']

def ans(request, pk):
    context={}
    context['status']=tests.status
    try:
        context['students']=Student.objects.filter(floor_num=pk, status='무단외박')
    except:
        context['students'] =''
    return render(request, 'roll_call/roll_call.html', context)

def ans_all(request, pk):
    context = {}
    context['status'] = tests.status
    try:
        context['students'] = Student.objects.filter(status='무단외박')
    except:
        context['students'] = ''
    return render(request, 'ans_call/roll_call.html', context)

