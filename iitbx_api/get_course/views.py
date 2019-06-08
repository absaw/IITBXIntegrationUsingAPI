from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseOverview
from .serializers import CourseOverviewSerializer


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
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   