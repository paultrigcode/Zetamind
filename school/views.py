from .models import Teacher,Student,Class,Level
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, QueryDict
from django.forms.models import model_to_dict
from datetime import date, timedelta
from django.db.models import Q
import json

# Create your views here.

@login_required
def teacher_view(request):
    return render(request, 'view_teachers.html')

@login_required
def student_view(request):
    return render(request, 'view_students.html')

@login_required
def student_create(request):
    return render(request, 'student_create.html')

@login_required
def teacher_create(request):
    return render(request, 'teacher_create.html')

def get_teachers(request):
    keyword = request.GET.get('keyword')
    if keyword != None:
        lookups= Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)
        teacher =list(Teacher.objects.filter(lookups).values())
        if recycler == []:
        	return HttpResponse('No house Household details matches the search query,phone_number,customer-number,names, and current point',status=204)
    else:
        teacher = list(Teacher.objects.all().values('id','level__name','first_name','last_name','class_held__name','staff_no'))
    return JsonResponse(teacher,safe=False)


def get_students(request):
    keyword = request.GET.get('keyword')
    if keyword != None:
        lookups= Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword)
        student =list(Student.objects.filter(lookups).values())
        if recycler == []:
        	return HttpResponse('No house Household details matches the search query,phone_number,customer-number,names, and current point',status=204)
    else:
        student = list(Student.objects.all().values('id','first_name','last_name','teacher__first_name','stud_no','teacher__last_name','teacher__staff_no','classs__name'))
    return JsonResponse(student,safe=False)


def get_student_teacher(request,id):
    student = Student.objects.filter(id=id).values('id','first_name','last_name','teacher__first_name','stud_no','teacher__last_name','teacher__staff_no')
    return JsonResponse(student,safe=False)

@login_required
def student_with_teacher_view(request,id):
    # instance=model_to_dict(get_object_or_404(Student,id=id))
    instance = list(Student.objects.filter(id=id).values('id','first_name','last_name','teacher__first_name','stud_no','teacher__last_name','teacher__staff_no','classs__name'))
    return render(request, 'student_with_teacher_view.html',{'instance':instance})

@login_required
def student_per_teacher_view(request,id):
    print(id)
    # instance=model_to_dict(get_object_or_404(Student,teacher__id=id))
    teacher = list(Teacher.objects.filter(id=id).values('id','staff_no','first_name','last_name'))
    instance = list(Student.objects.filter(teacher__id=id).values('id','first_name','last_name','teacher__first_name','stud_no','teacher__last_name','teacher__staff_no','classs__name'))
    print(instance)
    return render(request, 'student_per_teacher_view.html',{'instances':instance,'teacher':teacher})

def teachers(request):
    teachers=Teacher.objects.all().values('id','first_name','last_name','class_held__name','class_held')
    return JsonResponse(list(teachers),safe=False)

def classs(request):
    classs=Class.objects.all().values()
    return JsonResponse(list(classs),safe=False)

def level(request):
    level=Level.objects.all().values()
    return JsonResponse(list(level),safe=False)
def create_student(request):
    data_list = []
    first_name = request.GET.get('first_name')
    if first_name != '':
        data_list.append(first_name.strip())
    else:
        return HttpResponse('first_name cannot be blank',status=500)
    last_name = request.GET.get('last_name')
    if last_name != '':
        data_list.append(last_name.strip())
    else:
        return HttpResponse('last_name cannot be blank',status=500)
    classs = request.GET.get('classs')
    if classs != '':
        classs = Class.objects.get(id=int(classs))
        data_list.append(classs)
    else:
        return HttpResponse('class cannot be blank',status=500)
    teacher = request.GET.get('teacher')
    if teacher != '':
        teacher = Teacher.objects.get(id =int(teacher))
        data_list.append(teacher)
    else:
        return HttpResponse('Teacher cannot be blank',status=500)
    print(data_list)
    if len(data_list) !=4:
        return HttpResponse('Some fields data missing',status=500)
    else:
        create_model = model_to_dict(Student.objects.create(first_name=first_name.strip(),last_name=last_name.strip(),classs= classs,teacher=teacher))
        print(create_model['stud_no'])      # customer_number = 
        return HttpResponse(create_model['stud_no'],content_type='text/plain',status=200)

def create_teacher(request):
    data_list = []
    first_name = request.GET.get('first_name')
    if first_name != '':
        data_list.append(first_name.strip())
    else:
        return HttpResponse('first_name cannot be blank',status=500)
    last_name = request.GET.get('last_name')
    if last_name != '':
        data_list.append(last_name.strip())
    else:
        return HttpResponse('last_name cannot be blank',status=500)
    classs = request.GET.get('classs')
    if classs != '':
        classs = Class.objects.get(id=int(classs))
        data_list.append(classs)
    else:
        return HttpResponse('class cannot be blank',status=500)
    level = request.GET.get('level')
    if level != '':
        level = Level.objects.get(id =int(level))
        data_list.append(level)
    else:
        return HttpResponse('Level cannot be blank',status=500)
    print(data_list)
    if len(data_list) !=4:
        return HttpResponse('Some fields data missing',status=500)
    else:
        create_model = model_to_dict(Teacher.objects.create(first_name=first_name.strip(),last_name=last_name.strip(),class_held= classs,level=level))
        print(create_model['staff_no'])      # customer_number = 
        return HttpResponse(create_model['staff_no'],content_type='text/plain',status=200)