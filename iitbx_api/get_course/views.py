from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseOverview
from .serializers import CourseOverviewSerializer
from get_platform.serializers import IntegratedPlatformsSerializer
from get_platform.models import IntegratedPlatforms
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

#Lists all models or create a new one
#url at this point : "course/"
class CourseOverviewList(APIView):
    #@staticmethod to not use self 
    def get(self, request):
        course_meta_data = CourseOverview.objects.all()
        serializer = CourseOverviewSerializer(course_meta_data, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
         serializer = CourseOverviewSerializer(data=request.data)
         print("\nData Received By Backend Course API-> \n",request.data)
         if serializer.is_valid():
             serializer.save()
             # ADDING PLATFORMS TO OUR COURSES
             post_data = request.data# Retrieving the request data
             list_of_platforms = post_data["select_platforms"]# Taking the list of selected platforms

             present_course = post_data['coursekey']# Taking the course key of presently being created course
             course_object = CourseOverview.objects.get(coursekey=present_course)# Making an object for present course

             print("\n\nCourse Object : ", course_object)

             for item in list_of_platforms:
                platform_object = IntegratedPlatforms.objects.get(id=int(item)) # Making object for current selected platform
                print("\n\nPlatform Object\n\n",platform_object)

                group_object = GroupMember.objects.create(platforms=platform_object, courses=course_object)
                # Creating a many to many relation object between platforms and course
                group_object.save() # Saving the made object

             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#url at this point : "course/<str:id>"
# e.g. "course/IITB"
# This class is used to show a particular course according to the coursekey
class OneCourse(APIView):

    def get(self, request, id):
    
        coursekey = id
        course = CourseOverview.objects.filter(coursekey = coursekey)
        print("\n\nCourse Requested: ",course)
        print("\n\n")
        
        serializer = CourseOverviewSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#url at this point : "course/platform/<str:id>"
# e.g. "course/platform/cs101"
# This class is used to show a particular course's all platforms according to the course's coursekey
class OneCourseAllPlatforms(APIView):

    def get(self, request, id):
        #sep = id.split(',')
        coursekey = id
        #thirdparty_platform_name = sep[1]
        try:
            course = CourseOverview.objects.get(coursekey = coursekey)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            # If multiple courses contain same name it will take the first of them
            course = CourseOverview.objects.filter(coursekey = coursekey).first()

        platforms = course.platforms.all()
        print("\n\nPlatforms are ",platforms)
        print("\n\n")
        
        serializer = IntegratedPlatformsSerializer(platforms, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)



   