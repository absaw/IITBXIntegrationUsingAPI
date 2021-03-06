from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.CourseOverviewList.as_view()),
    path('<str:id>', views.OneCourse.as_view()),# id : coursekey
    path('platform/<str:id>', views.OneCourseAllPlatforms.as_view()) # id : coursekey
]
