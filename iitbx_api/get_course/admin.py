from django.contrib import admin
from .models import CourseOverview, GroupMember

admin.site.register(CourseOverview)
admin.site.register(GroupMember)