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