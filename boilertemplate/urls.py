"""boilertemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import hello,login,login_view,signup,signup_view,dashboard
from django.contrib.auth.views import LogoutView
from school.views import teacher_view,get_teachers,student_view,get_students,student_with_teacher_view,student_per_teacher_view,student_create,teachers,classs,create_student,create_teacher,teacher_create,level

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login,name='login'),
    path('signup/', signup,name='signup'),
    path('login-view/', login_view,name='login_view'),
    path('signup-view/', signup_view,name='signup_view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('',hello,name='hello'),
    path('dashboard/', dashboard,name='dashboard'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
    path('teacher/view/',teacher_view),
    path('teacher/list/',get_teachers),
    path('student/view/',student_view),
    path('student/list/',get_students),
    path('<int:id>/view/',student_with_teacher_view),
    path('<int:id>/teacher/view/',student_per_teacher_view),
    path('student/create/view/',student_create),
    path('teacher/create/view/',teacher_create),
    path('teachers/',teachers),
    path('class/',classs),
    path('levels/',level),
    path('student/create/',create_student),
    path('teacher/create/',create_teacher)




]
