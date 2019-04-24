from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer,TeacherSerializer,SubjectSerializer,AttendanceSerializer
from .models import Students, Teacher, Subject, Attendance


    
class TeacherRetrieve(generics.RetrieveAPIView):
    lookup_field = 'teacher_id'
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class SubjectTeacher(generics.RetrieveAPIView):
    lookup_field = 'subject_teacher'
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer




class SubjectAttendanceLive(generics.RetrieveUpdateAPIView):
    lookup_field = 'subject_id'
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentSubjects(generics.RetrieveAPIView):
    lookup_field = 'student_id'
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class AttendanceStudent(generics.RetrieveAPIView):
    lookup_field = 'student_id'
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer