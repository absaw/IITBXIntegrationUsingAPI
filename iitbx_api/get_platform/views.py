from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IntegratedPlatforms
from .serializers import IntegratedPlatformsSerializer
from get_course.serializers import CourseOverviewSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


#Lists all models or create a new one
#url at this point : "platform/"
class IntegratedPlatformsList(APIView):
    #@staticmethod to not use self 
    
    def get(self, request):
        platform_meta_data = IntegratedPlatforms.objects.all()
        serializer = IntegratedPlatformsSerializer(platform_meta_data, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
         serializer = IntegratedPlatformsSerializer(data=request.data)
         print("\nData Received By Backend Course API-> \n",request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#url at this point : "platform/<str:id>"
# e.g. "course/IITB"
# This class is used to show a particular course according to the coursekey
class OnePlatform(APIView):

    def get(self, request, id):
        #sep = id.split(',')
        thirdparty_platform_name = id

        platform = IntegratedPlatforms.objects.filter(thirdparty_platform_name = thirdparty_platform_name)
        
        print("\n\nPlatform Requested: ",platform)
        print("\n\n")
        
        serializer = IntegratedPlatformsSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
#url :"/platform/course/<str:id>"
# e.g. "platform/course/IITB"
# This class is used to show all courses hosted on a platform by use of thirdparty_platform_name of the platform
class OnePlatformAllCourses(APIView):

    def get(self, request, id):
        platform_name = id

        try:
            platform = IntegratedPlatforms.objects.get(thirdparty_platform_name=platform_name)
        except ObjectDoesNotExist:
            raise Http404
        except MultipleObjectsReturned:
            # If multiple platforms contain same name it will take the first of them
            platform = IntegratedPlatforms.objects.filter(thirdparty_platform_name=platform_name).first()
            

        platform_courses = platform.courses.all()

        print("\n\n Courses in Platform : ", platform_courses)
        print("\n\n")

        serializer = CourseOverviewSerializer(platform_courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        

        

        



