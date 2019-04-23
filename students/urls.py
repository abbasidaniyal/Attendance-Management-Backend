from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^subject-teacher/(?P<subject_teacher>\d+)$',
        views.UpdateUserProfile.as_view(), name ='subjects_under_teacher'),
]

