from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('get_course.urls')),
    path('platform/', include('get_platform.urls')),
    path('api/',include('grades.urls')),
    path('course_import/', include('Clone.urls')),
]
