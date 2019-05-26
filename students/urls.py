from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^subject-teacher/(?P<subject_teacher>\d+)$',
        views.SubjectTeacher.as_view(), name ='subjects_under_teacher'),
    url(r'^attendance-status/(?P<subject_id>\d+)$',
        views.SubjectAttendanceLive.as_view(),name='subject_status'),
    path('teacher-list/',views.TeacherList.as_view(),name='teachers_list'),
    url(r'^student-subject/(?P<id>\d+)$',
        views.StudentSubjects.as_view(),name='student_subject_list'),
    url(r'^which-teacher/(?P<teacher_id>\d+)$',
        views.TeacherRetrieve.as_view(),name='which_teacher'),
    path('attendance/',views.createInstance, name='attendance'),
    path('attendance-of-student/<int:student_id>/of-subject/<int:subject_id>/',views.AttendancePercentage.as_view(),name='attendance_percentage'),
    path('attendance-of-subject-all/<int:student_id>/',views.AttendanceStudent.as_view(),name='attendance-list-of-students'),
        
]

