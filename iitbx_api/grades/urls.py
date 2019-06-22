from django.urls import path
from grades import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    path('grade/v0/grades', views.AllPlatforms.as_view()),
    path('grade/v0/grades/<str:pk>/', views.AllCourses.as_view()),
    path('grade/v0/grades/<str:pk>/<str:pk1>/', views.AllStudents.as_view()),
    path('grade/v0/grades/<str:pk>/<str:pk1>/<int:pk2>/', views.OneStudent.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
