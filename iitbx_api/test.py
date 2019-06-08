# a = 'Abhi'
# s = input("Enter age {}- >".format(a))
# print('{} is you age {}'.format(s,a))
# print(type(s))

def boolify(s):
    if s != 'True' or 'true' or 'False' or 'false'
        return s
    if s == 'True' or 'true':
        return True
    if s == 'False' or 'false':
        return False
        
    raise ValueError("huh?")

def autoconvert(s):
    for fn in (int, float, boolify):
        try:
            return fn(s)
        except ValueError as e:
            pass
            print("Exception occured in except of autoconvert() :", e)
    return s

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
    course[x]= autoconvert(course[x])

print(course)

