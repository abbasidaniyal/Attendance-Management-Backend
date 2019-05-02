from django.db import models
from django.contrib.auth.models import User
import datetime

live_choices = (
    ("L","L"),
    ("NL","NL")
    )
groups_choices = (
    ("STAFF", "STAFF"),
    ("STUDENT", "STUDENT")  
)
attendence_choices = (
    ("A", "A"),
    ("P", "P")
)

class Teacher(models.Model):
    # user_teacher = models.ForeignKey(User, verbose_name=("Teacher_Login"), on_delete=models.SET_NULL,default="0",null=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    teacher_id = models.IntegerField(primary_key = True, )

class Batch(models.Model):
    batch_id=models.AutoField(primary_key=True)
    batch_name=models.CharField(max_length=20)


class Subject(models.Model):
    subject_batch = models.ForeignKey(Batch, on_delete=models.CASCADE,null=True) 
    subject_name = models.CharField(max_length = 30)
    subject_id = models.AutoField(primary_key = True)
    is_live = models.CharField(choices = live_choices ,max_length=5,default="NL")
    subject_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE) 



class Students(models.Model):
    # user_student = models.ForeignKey(User, verbose_name=("Student_login"), on_delete=models.SET_NULL,default="0",null=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    student_id = models.IntegerField(primary_key=True)
    date_joined = models.DateField(auto_now = True, auto_now_add = False)
    student_batch = models.ForeignKey(Batch,on_delete=models.CASCADE ,null=True) 
    student_subject = models.ManyToManyField(Subject, verbose_name=("Student studies the subject"))
    students_ip = models.CharField(max_length=30,blank=True,)
    def __str__(self):
        return self.first_name

class Attendance(models.Model):
    attendence_id = models.AutoField(primary_key = True)
    status = models.CharField(max_length = 2, choices = attendence_choices,default="A")
    date = models.DateField( auto_now_add = True)
    student_id = models.ForeignKey(Students, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)

