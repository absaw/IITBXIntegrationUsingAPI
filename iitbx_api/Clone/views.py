"""from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import repoclone
from .serializers import repocloneSerializer
# Create your views here

class repolist(APIView): 
    def get(self, request):
        repolist = repoclone.objects.all()
        serializer = repocloneSerializer(repolist, many = True)
        return Response(serializer.data)

    def post(self, request):
         serializer = repocloneSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import repoclone
from .serializers import repocloneSerializer

import os.path
from git import *
import git, os
from urllib.parse import urlparse

class repolist(APIView):
    def get(self, request):
        repolist = repoclone.objects.all()
        serializer = repocloneSerializer(repolist, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = repocloneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            clone_data = serializer.data
            directory1=clone_data['directory']
            url1=clone_data['url']


            REPO_FOLDER = directory1
            REMOTE_URL = url1
            if not os.path.exists(REPO_FOLDER):
                os.makedirs(REPO_FOLDER)
                print(REPO_FOLDER)
            temp = os.path.basename(REMOTE_URL).split(".")[-2]
            NEW_FOLDER = (REPO_FOLDER+"\\"+temp+"")
            os.mkdir(REPO_FOLDER+"\\"+temp+"")
            print(NEW_FOLDER)

            new_path = os.path.join(NEW_FOLDER)
            DIR_NAME = new_path
             

            def git_clone():  
                try:
                    
                    repo = git.Repo.init(DIR_NAME)
                    print(repo)
                    origin = repo.create_remote('origin', REMOTE_URL)
                    origin.fetch()
                    origin.pull(origin.refs[0].remote_head)
                    return True
                except:
                    return False    
            repo = repoclone.objects.filter(id = clone_data['id'])
            if git_clone():
                repo.update(status = "cloned")
            else:
                repo.update(status = "failed")
            return Response(repo, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)