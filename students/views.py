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
    	id = self.kwargs['id']
    	return Students.objects.filter(id = id)

class AttendanceStudent(generics.RetrieveAPIView):
    lookup_field = 'student_id'
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


@api_view(['POST'])
def createInstance(request):
    sub_id = request.data
    for stud in Students.objects.filter(student_subject=sub_id):
        att = Attendance(student_id_id=stud.id,subject_id_id=sub_id,status="Absent")
        att.save()
    content = {'success': 'success'}
    return Response(content, status=status.HTTP_200_OK)


class AttendancePercentage(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    lookup_fields = ('student_id','subject_id')
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer 



