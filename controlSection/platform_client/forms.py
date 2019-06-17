from django import forms
import requests
class platform_form(forms.Form):
    """
    Form for collecting basic information about an external learning platforms.

    This model contains basic platform metadata such as an ID, name,
    URL, and any other information that would be necessary to
    a courses as part of there system.
    """

    # External Lerning platform information
    org = forms.CharField(required=True)
    thirdparty_platform_name = forms.CharField(required=True)
    
    # URLs
    ServerUrl = forms.CharField(required=True)
    
    # Enrollment details
    integrationstart = forms.DateTimeField(required=True, initial="2006-10-25 14:30:59")
    integrationend = forms.DateTimeField(required=True, initial="2006-11-25 14:30:59")
    #Date Time Format : 2006-10-25 14:30:59

    # Status details
    isactive = forms.BooleanField(required=False)#Originally True
    #isactive = True
    # about
    short_description = forms.CharField(required=False)

class course_form(forms.Form):
    """
    Form for collecting basic information about a course.

    This model contains basic course metadata such as an ID, display name,
    image URL, and any other information that would be necessary to display
    a course as part of:
        user dashboard (enrolled courses)
        course catalog (courses to enroll in)
        course about (meta data about the course)
    """
    # Cache entry versioning.
    version = forms.IntegerField()

    # Course identification
    # This course_id refer in edx platform for identification of course.
    # The value of coursekey is return value after create course on edx.
    coursekey = forms.CharField(max_length=255, required=True)
    # id = CourseKeyField(db_index=True, primary_key=True, max_length=255)
    # _location = UsageKeyField(max_length=255)
    _location = forms.CharField(max_length=255, required=False)
    org = forms.CharField() # max_length=255, initial='outdated_entry')
    display_name = forms.CharField()
    display_number_with_default = forms.CharField()
    display_org_with_default = forms.CharField()
    course_run = forms.CharField(max_length=255, required=True)
    # display_run_with_default = CharField(max_length=255, required=True)

    # Start/end dates
    start = forms.DateTimeField(required=False, initial="2006-10-25 14:30:59")
    end = forms.DateTimeField(required=False, initial="2006-11-25 14:30:59")
    advertised_start = forms.CharField(required=False)
    announcement = forms.DateTimeField(required=False, initial="2006-10-25 14:30:59")

    # URLs
    # ?
    course_image_url = forms.CharField(required=False)
    social_sharing_url = forms.CharField(required=False)
    end_of_course_survey_url = forms.CharField(required=False)

    # Certification data
    certificates_display_behavior = forms.CharField(required=False)
    certificates_show_before_end = forms.BooleanField(initial=False, required=False)
    cert_html_view_enabled = forms.BooleanField(initial=False, required=False)
    has_any_active_web_certificate = forms.BooleanField(initial=False, required=False)
    cert_name_short = forms.CharField(required=False)
    cert_name_long = forms.CharField(required=False)

    # Grading
    lowest_passing_grade = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    # Access parameters
    days_early_for_beta = forms.FloatField(required=False)
    mobile_available = forms.BooleanField(initial=False, required=False)
    visible_to_staff_only = forms.BooleanField(initial=False, required=False)
    _pre_requisite_courses_json = forms.CharField(required=False)  # JSON representation of list of CourseKey strings

    # Enrollment details
    enrollment_start = forms.DateTimeField(required=False, initial="2006-10-25 14:30:59")
    enrollment_end = forms.DateTimeField(required=False, initial="2006-11-25 14:30:59")
    enrollment_domain = forms.CharField(required=False)
    invitation_only = forms.BooleanField(initial=False, required=False)
    max_student_enrollments_allowed = forms.IntegerField(required=False)

    # Catalog information
    catalog_visibility = forms.CharField(required=False)
    short_description = forms.CharField(required=False)
    course_video_url = forms.CharField(required=False)
    effort = forms.CharField(required=False)
    self_paced = forms.BooleanField(initial=False, required=False)
    marketing_url = forms.CharField(required=False)
    eligible_for_financial_aid = forms.BooleanField(initial=True, required=False)

    language = forms.CharField(required=False) 

    # Integration information
    created_on_edx = forms.BooleanField(initial=False, required=False)

    # Time Stamp information
    created = forms.DateTimeField(initial="2006-10-25 14:30:59")
    updated = forms.DateTimeField(initial="2006-11-25 14:30:59")
    #created = forms.DateTimeField(auto_now=True)
    #updated = forms.DateTimeField(auto_now_add=True)    
    
    resp = requests.get('http://127.0.0.1:8000/get_platform/')
    platList = []
    i=0
    a = resp.json()
    for item in a:
        platList.append([])#Adding empty List for Each Platform
        platList[i].append(item["id"])#Populating the list with id and platform_name
        platList[i].append(item["thirdparty_platform_name"])
        i = i+1
    
    #platList = tuple(platList)
    '''
    def __init__(self):
        self.resp = requests.get('http://127.0.0.1:8000/get_platform/')
        self.platList = []
        self.i=0
        self.a = self.resp.json()
        for item in self.a:
            self.platList.append([])#Adding empty List for Each Platform
            self.platList[self.i].append(item["id"])#Populating the list with id and platform_name
            self.platList[self.i].append(item["thirdparty_platform_name"])
            self.i = self.i+1
    '''
    

    select_platforms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], required=False)
    
    
    def __init__(self, *args, **kwargs):
        super(course_form, self).__init__(*args, **kwargs)
        self.resp = requests.get('http://127.0.0.1:8000/get_platform/')
        self.platList = []
        self.i=0
        self.a = self.resp.json()
        for item in self.a:
            self.platList.append([])#Adding empty List for Each Platform
            self.platList[self.i].append(item["id"])#Populating the list with id and platform_name
            self.platList[self.i].append(item["thirdparty_platform_name"])
            self.i = self.i+1
        self.fields['select_platforms'] = forms.MultipleChoiceField(choices=self.platList, widget=forms.CheckboxSelectMultiple)



class course_import(forms.Form):
    """
    Form that take Course URL and directory as input.

    This model clone the course project into the given directory.
    """

    # Course name 
    Course = forms.CharField(required=True)
    # directory where we want to clone the project.
    Directory = forms.CharField(required=True)
