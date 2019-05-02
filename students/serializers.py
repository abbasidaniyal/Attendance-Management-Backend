from rest_framework import serializers
from .models import Students,Subject,Teacher,Attendance



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_name','subject_id','is_live','subject_teacher')


class StudentSerializer(serializers.ModelSerializer):
    student_subject = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Students
        fields = ('first_name','last_name','student_subject','students_ip')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name','last_name','teacher_id')


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('status','student_id_att','subject_id_att','date')