import requests
class ApiError(Exception):
    """A Custom API Error Exception Handling class"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError Occured : Status Code = {} ".format(self.status)

def get(platform_key=None):
    
    resp = requests.get('http://127.0.0.1:8000/get_platform/')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError(resp.status_code)
    
    if platform_key is None:

        for item in resp.json():
            print('{}'.format(item))#item consists one tuple of the table

    else:
        for item in resp.json():
            if platform_key is item["id"]:
                print('{}'.format(item))#select * from resp.json() where id = course_key
            else:
                print("ID not found: Status Code : 404")

def post(request):
    resp = requests.post('http://127.0.0.1:8000/get_platform/', json=request)
    if resp.status_code != 201:
        raise ApiError(resp.status_code)
    print('Created task. ID: {}, Platform Name: {}'.format(resp.json()["id"],resp.json()["thirdparty_platform_name"]))#resp consists the tuple which was just added

def input():
    course = { 
        "version": None,
        "coursekey": None
        # "_location": None,
        # "org": None,
        # "display_name": None,
        # "display_number_with_default": None,
        # "display_org_with_default": None,
        # "course_run": None,
        # "start": None,
        # "end": None,
        # "advertised_start": None,
        # "announcement": None,
        # "course_image_url": None,
        # "social_sharing_url": None,
        # "end_of_course_survey_url": None,
        # "certificates_display_behavior": None,
        # "certificates_show_before_end": None,
        # "cert_html_view_enabled": None,
        # "has_any_active_web_certificate": None,
        # "cert_name_short": None,
        # "cert_name_long": None,
        # "lowest_passing_grade": None,
        # "days_early_for_beta": None,
        # "mobile_available": None,
        # "visible_to_staff_only": None,
        # "_pre_requisite_courses_json": None,
        # "enrollment_start": None,
        # "enrollment_end": None,
        # "enrollment_domain": None,
        # "invitation_only": None,
        # "max_student_enrollments_allowed": None,
        # "catalog_visibility": None,
        # "short_description": None,
        # "course_video_url": None,
        # "effort": None,
        # "self_paced": None,
        # "marketing_url": None,
        # "eligible_for_financial_aid": None,
        # "language": None,
        # "created_on_edx": None,
        # "created": None,
        # "updated": None
    }

    for x in course:
        course[x]=input("Enter Value for {}->".format(x))




# def get(course_key):
#     resp = requests.get('http://127.0.0.1:8000/')
#     if resp.status_code != 200:
#         # This means something went wrong.
#         raise ApiError('GET / {}'.format(resp.status_code))
#     for item in resp.json():
#         if course_key is item["id"]:
#             print('{}'.format(item))#select * from resp.json() where id = course_key