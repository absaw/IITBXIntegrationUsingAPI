from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='index'),
    path('get_platform_form/', views.get_platform_form, name='get_platform_form'),
    path('post_platform_form/', views.post_platform_form, name='post_platform_form'),
    path('get_course_form/', views.get_course_form, name='get_course_form'),
    path('post_course_form/', views.post_course_form, name='post_course_form'), 
]
