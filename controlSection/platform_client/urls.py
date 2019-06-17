from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='index'),
    path('get_platform_form/', views.get_platform_form, name='get_platform_form'),
    path('post_platform_form/', views.post_platform_form, name='post_platform_form'),
    path('get_course_form/', views.get_course_form, name='get_course_form'),
    path('post_course_form/', views.post_course_form, name='post_course_form'),
    path('get_course_import/', views.get_course_import, name='get_course_import'),
    path('post_course_import/', views.post_course_import, name='post_course_import'),
    path('grades/', views.grades_view, name='grades'), 
]
