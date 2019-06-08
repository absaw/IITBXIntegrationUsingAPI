from django.db import models


class CourseOverview(models.Model,):
    """
    Model for storing and caching basic information about a course.

    This model contains basic course metadata such as an ID, display name,
    image URL, and any other information that would be necessary to display
    a course as part of:
        user dashboard (enrolled courses)
        course catalog (courses to enroll in)
        course about (meta data about the course)
    """
    # Cache entry versioning.
    version = models.IntegerField()

    # Course identification
    # This course_id refer in edx platform for identification of course.
    # The value of coursekey is return value after create course on edx.
    coursekey = models.TextField(max_length=255, null=True)
    # id = CourseKeyField(db_index=True, primary_key=True, max_length=255)
    # _location = UsageKeyField(max_length=255)
    _location = models.TextField(max_length=255, null=True)
    org = models.TextField() # max_length=255, default='outdated_entry')
    display_name = models.TextField()
    display_number_with_default = models.TextField()
    display_org_with_default = models.TextField()
    course_run = models.TextField(max_length=255, null=False)
    # display_run_with_default = TextField(max_length=255, null=False)

    # Start/end dates
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    advertised_start = models.TextField(null=True)
    announcement = models.DateTimeField(null=True)

    # URLs
    # ?
    course_image_url = models.TextField(null=True)
    social_sharing_url = models.TextField(null=True)
    end_of_course_survey_url = models.TextField(null=True)

    # Certification data
    certificates_display_behavior = models.TextField(null=True)
    certificates_show_before_end = models.BooleanField(default=False)
    cert_html_view_enabled = models.BooleanField(default=False)
    has_any_active_web_certificate = models.BooleanField(default=False)
    cert_name_short = models.TextField(null=True)
    cert_name_long = models.TextField(null=True)

    # Grading
    lowest_passing_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    # Access parameters
    days_early_for_beta = models.FloatField(null=True)
    mobile_available = models.BooleanField(default=False)
    visible_to_staff_only = models.BooleanField(default=False)
    _pre_requisite_courses_json = models.TextField(null=True)  # JSON representation of list of CourseKey strings

    # Enrollment details
    enrollment_start = models.DateTimeField(null=True)
    enrollment_end = models.DateTimeField(null=True)
    enrollment_domain = models.TextField(null=True)
    invitation_only = models.BooleanField(default=False)
    max_student_enrollments_allowed = models.IntegerField(null=True)

    # Catalog information
    catalog_visibility = models.TextField(null=True)
    short_description = models.TextField(null=True)
    course_video_url = models.TextField(null=True)
    effort = models.TextField(null=True)
    self_paced = models.BooleanField(default=False)
    marketing_url = models.TextField(null=True)
    eligible_for_financial_aid = models.BooleanField(default=True)

    language = models.TextField(null=True) 

    # Integration information
    created_on_edx = models.BooleanField(default=False)

    # Time Stamp information
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # platforms = ManyToManyField(IntegratedPlatforms, blank=True, related_name='groups', through="GroupMember")
    # bools = ['certificates_show_before_end','cert_html_view_enabled','has_any_active_web_certificate','mobile_available']