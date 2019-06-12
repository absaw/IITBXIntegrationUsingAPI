from django.urls import path
from grades import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    path('grade/v0/grades', views.AllStudentsAllCourses.as_view()),
    path('grade/v0/grades/<str:pk>/', views.AllStudentsOneCourse.as_view()),
    path('grade/v0/grades/<str:pk>/<int:pk1>/', views.OneStudentOneCourse.as_view())
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
