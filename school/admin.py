from django.contrib import admin

# Register your models here.
from .models import Class,Teacher,Student,Level
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Level)
