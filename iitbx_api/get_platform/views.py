from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IntegratedPlatforms
from .serializers import IntegratedPlatformsSerializer
from get_course.serializers import CourseOverviewSerializer


#Lists all models or create a new one
#url at this point : "platform/"
class IntegratedPlatformsList(APIView):
    #@staticmethod to not use self 
    
    def get(self, request):
        platform_meta_data = IntegratedPlatforms.objects.all()
        serializer = IntegratedPlatformsSerializer(platform_meta_data, many = True)
        return Response(serializer.data)

    def post(self, request):
         serializer = IntegratedPlatformsSerializer(data=request.data)
         print("\nData Received By Backend Course API-> \n",request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OnePlatformAllCourses(APIView):

    def get(self, request, id):
        platform_name = id
        platform = IntegratedPlatforms.objects.get(thirdparty_platform_name=platform_name)
        platform_courses = platform.courses.all()

        print("\n\n Courses in Platform : ", platform_courses)
        print("\n\n")

        serializer = CourseOverviewSerializer(platform_courses, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        

        

        



