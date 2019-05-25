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


class StudentSubjects(generics.ListAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
    	id = self.kwargs['student_id']
    	return Students.objects.filter(student_id = id)

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





# @api_view(['POST'])
# def form(request):
#     body = request.data

    
#     if message:
#         try:
#             print(body)
#             # return HttpResponse(request)
#         # except BadHeaderError:
#         #     content = {'Try again': 'Try again'}
#         #     return Response(content, status=status.HTTP_404_BAD_REQUEST)
