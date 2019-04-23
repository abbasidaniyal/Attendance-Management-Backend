from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer,TeacherSerializer


    



class SubjectTeacher(generics.RetrieveAPIView):
    lookup_field = 'subject_teacher'
    queryset = Subject.objects.all()
    serializer_class = TeacherSerializer
