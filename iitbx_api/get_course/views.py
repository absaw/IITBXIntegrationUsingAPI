from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseOverview, GroupMember
from .serializers import CourseOverviewSerializer
from get_platform.models import IntegratedPlatforms


#Lists all models or create a new one
#url at this point : "get_course/"
class CourseOverviewList(APIView):
    #@staticmethod to not use self 
    def get(self, request):
        course_meta_data = CourseOverview.objects.all()
        serializer = CourseOverviewSerializer(course_meta_data, many = True)
        return Response(serializer.data)

    def post(self, request):
         serializer = CourseOverviewSerializer(data=request.data)
         print("\nData Received By Backend Course API-> \n",request.data)
         if serializer.is_valid():
             serializer.save()

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
    
   