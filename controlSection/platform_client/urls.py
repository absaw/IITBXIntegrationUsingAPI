from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='index'),
    path('platformForm/', views.platformForm, name='platformForm'),
    path('courseForm/', views.courseForm, name='courseForm'),
    path('courseImportForm/', views.courseImportForm, name='courseImportForm'),
    path('grades/', views.grades_view, name='grades'), 
]
