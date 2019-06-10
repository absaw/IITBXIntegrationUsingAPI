from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IntegratedPlatforms
from .serializers import IntegratedPlatformsSerializer


#Lists all models or create a new one
#url at this point : "get_platform/"
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
    
   

