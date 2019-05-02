from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer,TeacherSerializer,SubjectSerializer,AttendanceSerializer
from .models import Students, Teacher, Subject, Attendance
from django.shortcuts import render
from rest_framework import viewsets, status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import smtplib
import json
import datetime
from django.shortcuts import get_list_or_404, get_object_or_404

    
class TeacherRetrieve(generics.RetrieveAPIView):
    lookup_field = 'teacher_id'
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class SubjectTeacher(generics.ListAPIView):
    # queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    def get_queryset(self):
        id = self.kwargs['subject_teacher']
        return Subject.objects.filter(subject_teacher=id)
    




class SubjectAttendanceLive(generics.RetrieveUpdateAPIView):
    lookup_field = 'subject_id'
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create_attendance(self):
        stud = Students.objects.filter(student_subject=self.kwargs['subject_id'])
        for inst in stud:
            att_student_id = inst.student_id
            att_subject_id = inst.subject_id
            att_date = datetime.date.today()
            attendance_create = Attendance(student_id = att_student_id,
                                            student_subject=att_subject_id,
                                            date=att_date,
                                            )
            attendance_create.save()

        
    
# student = SubjectAttendanceLive()
# p = Subject()
# student.CreateAttendance(p.subject_id

        ## student models main se student ids where subject_id present
        ## attendance instance student ids subject id and date today status absent
        ## instance save
        # stud_id = Students.objects.filter()
# class Attendance(models.Model):
#     attendence_id = models.AutoField(primary_key = True)
#     status = models.CharField(max_length = 2, choices = attendence_choices)
#     date = models.DateField(auto_now = True, auto_now_add = True)
#     student_id = models.ForeignKey(Students, on_delete = models.CASCADE)
#     subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)


    # CreateAttendance(subject_id)
class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class StudentSubjects(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
    	id = self.kwargs['student_id']
    	return Students.objects.filter(student_id = id)

class AttendanceStudent(generics.RetrieveAPIView):
    lookup_field = 'student_id_att'
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendancePercentage(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    lookup_fields = ('student_id_att','subject_id_att')
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer 



