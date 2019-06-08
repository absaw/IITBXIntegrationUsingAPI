from django.db import models
# import sys
# sys.path.insert(0,'/home/user/Desktop/codes2/course/course/get_course')
# #/home/user/Desktop/codes2/course/course/db.sqlite3
# #from home.user.Desktop.codes2.course.course.get_course.models import CourseOverview
# import models as m
#from get_course.models import CourseOverview

# from m import CourseOverview
class IntegratedPlatforms(models.Model):
    """
    Model for storing and caching basic information about a external learning platforms.

    This model contains basic platform metadata such as an ID, name,
    URL, and any other information that would be necessary to
    a courses as part of there system.
    """

    # External Lerning platform information
    org = models.TextField()
    thirdparty_platform_name = models.TextField(null=True)
    
    # URLs
    ServerUrl = models.TextField()
    
    # Enrollment details
    integrationstart = models.DateTimeField(null=True)
    integrationend = models.DateTimeField(null=True)

    # Status details
    isactive = models.BooleanField(default=False)

    # about
    short_description = models.TextField(null=True)

    #courses = models.ManyToManyField(CourseOverview, blank=True, related_name='platforms', through="CoursePlatform")
    #courses = models.ManyToManyField(CourseOverview)
    
