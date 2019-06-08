from django.contrib import admin
from .models import IntegratedPlatforms
from get_course.models import CourseOverview

admin.site.unregister(CourseOverview)
admin.site.register(IntegratedPlatforms)
admin.site.register(CourseOverview)
