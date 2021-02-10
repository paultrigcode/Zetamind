from django.db import models

# Create your models here.


def increment_staff_number():
    last_staff_no = Teacher.objects.all().order_by('id').last()
    if not last_staff_no:
       return "Staff001" 
    staff_no = last_staff_no.staff_no
    staff_number_int = int(staff_no.split('Staff')[-1])
    new_staff_number_int = f"{staff_number_int + 1:03}"
    new_staff_no = 'Staff' + str(new_staff_number_int)
    return new_staff_no

def increment_stud_number():
    last_stud_no = Student.objects.all().order_by('id').last()
    if not last_stud_no:
       return "Stud001" 
    stud_no = last_stud_no.stud_no
    stud_number_int = int(stud_no.split('Stud')[-1])
    new_stud_number_int = f"{stud_number_int + 1:03}"
    new_stud_no = 'Stud' + str(new_stud_number_int)
    return new_stud_no




class Class(models.Model):
	name = models.CharField(max_length= 5)
	def __str__(self):
		return self.name

class Level(models.Model):
	name =models.CharField(max_length=30)
	def __str__(self):
		return self.name

class Teacher(models.Model):
	staff_no = models.CharField(max_length=100,default=increment_staff_number)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	level = models.ForeignKey(Level,on_delete=models.DO_NOTHING)
	class_held = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
	def __str__(self):
		return str(self.first_name)+str(self.last_name)

class Student(models.Model):
	stud_no = models.CharField(max_length=100,default=increment_stud_number)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	classs = models.ForeignKey(Class,blank=True,null=True, on_delete=models.DO_NOTHING)
	teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
	def __str__(self):
		return str(self.first_name)+str(self.last_name)
