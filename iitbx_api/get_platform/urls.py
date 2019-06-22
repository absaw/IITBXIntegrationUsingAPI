from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IntegratedPlatformsList.as_view()),
    path('<str:id>', views.OnePlatform.as_view()),# id : thirdparty_platform_name
    path('course/<str:id>', views.OnePlatformAllCourses.as_view())#id : thirdparty_platform_name
]
