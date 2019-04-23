from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer,TeacherSerializer,SubjectSerializer
from .models import Students, Teacher,Subject


    

class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class SubjectTeacher(generics.RetrieveAPIView):
    lookup_field = 'subject_teacher'
    queryset = Subject.objects.all()
    serializer_class = TeacherSerializer




class SubjectAttendanceLive(generics.RetrieveUpdateAPIView):
    lookup_field = 'subject_id'
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
