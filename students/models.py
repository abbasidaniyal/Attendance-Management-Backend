from django.db import models
import uuid
from django.db import models
import datetime

groups_choices = (
    ("STAFF", "STAFF"),
    ("STUDENT", "STUDENT")
)


class Teacher(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    teacher_id = models.IntegerField(primary_key = True, unique = True)


class Subject(models.Model):
    subject_name = models.CharField(max_length = 30)
    subject_id = models.AutoField(primary_key = True)
    subject_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE) 

class Batch(models.Model):
    batch_id=models.AutoField(primary_key=True)
    batch_name=models.CharField(max_length=20)


class Students(models.Model):

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 254)
    password = models.CharField(max_length = 50)
    student_id = models.BigIntegerField(unique=True)
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid1, editable = False)
    date_joined = models.DateField(auto_now = True, auto_now_add = False)



class Attendance(models.Model):
    attendence_id = models.AutoField(primary_key = True)
    status = models.CharField(max_length = 2)
    date = models.DateField(auto_now = True, auto_now_add = False)
    student_id = models.ForeignKey(Students, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)


