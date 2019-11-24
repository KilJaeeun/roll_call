from django.views.decorators.http import require_POST


from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
# 분야
from django.views.decorators.http import require_POST
from rest_framework.utils import json


from roll_call.models import *
from roll_call.tests import *
#층 전체 리스트
def floor_list(request):
    context={}
    context['floor_lists']=FloorManager.objects.all()
    return render(request, 'roll_call/floor_list.html', context)

def roll_call(request, pk):
    context={}
    context['status']=tests.status
    try:
        floor=FloorManager.objects.get(floor_num=pk)
        students=Student.objects.filter(floor_num=floor)
        # students_count=students.count()
        context['students']=Student.objects.filter(floor_num=floor)
        # print(students.count())
    except:
        context['students'] =''
        print('못받음')
    if request.method == 'POST':
        student_status=dict(request.POST)['student_status']

        for e in range(len(student_status)):
            student=students[e]
            # student.ssn=student.ssn
            # student.name=student.name
            student.status=student_status[e]
            # student.ssn=student.ssn
            student.save()
        return HttpResponseRedirect(reverse('roll_call:ans', args=[pk]))
    return render(request, 'roll_call/roll_call.html', context)


def floor_ans(request, pk):
    context={}
    context['status']=tests.status
    context['pk']=pk

    try:
        context['students']=Student.objects.filter(floor_num=pk, status='무단외박')
    except:
        context['students'] =''
    return render(request, 'roll_call/ans.html', context)

def ans_all(request):
    context = {}
    context['status'] = tests.status
    try:
        context['students'] = Student.objects.filter(status='무단외박')
    except:
        context['students'] = ''
    return render(request, 'roll_call/ans_all.html', context)

