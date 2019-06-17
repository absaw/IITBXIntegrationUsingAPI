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
    
    # Function to display all the content of "repoclone" database
    def get(self, request):
        repolist = repoclone.objects.all()
        serializer = repocloneSerializer(repolist, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = repocloneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            clone_data = serializer.data
            Directory1=clone_data['Directory']
            temp=clone_data['Course']
            #Taking course_name as string input and appending with other string to give it a syntax of URL
            new = "https://github.com/saursahu/"
            Course1=new+temp+".git"

            REPO_FOLDER = Directory1
            REMOTE_URL = Course1
            if not os.path.exists(REPO_FOLDER):
                os.makedirs(REPO_FOLDER)
                print(REPO_FOLDER)
            #temp = os.path.basename(REMOTE_URL).split(".")[-2]
            NEW_FOLDER = (REPO_FOLDER+"//"+temp+"")
            os.mkdir(REPO_FOLDER+"//"+temp+"")
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
                repo.update(Status = "Cloned")
            else:
                repo.update(Status = "Failed")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
