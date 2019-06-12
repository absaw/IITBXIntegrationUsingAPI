from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_course/', include('get_course.urls')),
    path('get_platform/', include('get_platform.urls')),
    path('api/',include('grades.urls')),
    path('repo/', include('Clone.urls')),
]
