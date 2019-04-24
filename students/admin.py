from django.contrib import admin
from .models import Teacher,Students,Subject,Batch,Attendance

admin.site.register(Teacher)
admin.site.register(Students) 
admin.site.register(Subject)
admin.site.register(Batch)  
admin.site.register(Attendance) 

# Register your models here.
