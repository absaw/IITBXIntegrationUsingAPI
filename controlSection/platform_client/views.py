from django.shortcuts import render
import requests
from .forms import platform_form, course_form, course_import
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from rest_framework.response import Response
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import Http404


class ApiError(Exception):
    """A Custom API Error Exception Handling class"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError Occured : Status Code = {} ".format(self.status)
def update_form():
    resp = requests.get('http://127.0.0.1:8000/platform/')
    platList = []
    i=0
    a = resp.json()
    for item in a:
        platList.append([])#Adding empty List for Each Platform
        platList[i].append(item["id"])#Populating the list with id and platform_name
        platList[i].append(item["thirdparty_platform_name"])
        i = i+1
    return platList

def index(request):
    return render(request, 'index.html')
    

def courseForm(request):
    '''
    Function to handle a post request coming from form.html
    '''
    if request.method == 'POST':
        form = course_form(request.POST)

        if form.is_valid():

            form_data = form.cleaned_data#retrieve form content
            print("FORM IS VALID")

            def convert_timestamp(item_date_object):
                #Function to convert datetime entries from django format to json iso format
                if isinstance(item_date_object, (datetime.date, datetime.datetime)):
                    return item_date_object.isoformat()

            json_data = json.dumps(form_data, default=convert_timestamp)#dumps()returns data as string
            json_data = json.loads(json_data)#loads() converts string to json format

            resp = requests.post('http://127.0.0.1:8000/course/', json=json_data)
            #json_data in json format is passed on to backend get_course API
            if resp.status_code != 201:
                raise ApiError(resp.status_code)
            print('\n\nCreated task. ID: {} Course Key : {}\n\n'.format(resp.json()["id"], resp.json()["coursekey"]))#resp consists the tuple which was just added

            return render(request, 'result.html',{"done":True, "form_name":"course"})

        else:
            #condition when post is unsuccessfull, and/or form is invalid
            print("FORM IS NOT VALID")
            return render(request, 'result.html',
                          {'form': form ,
                          'done':False,
                          "form_name":"course"
                          })
    else:
        form = course_form()
        return render(request, 'form_course.html', {
                "form":form,
                "form_name":"course"
            })

def platformForm(request):
    '''
    Function to handle a post request coming from form.html
    '''
    if request.method == 'POST':
        form = platform_form(request.POST)

        if form.is_valid():
            print("FORM IS VALID")
            form_data = form.cleaned_data#retrieve form content

            def convert_timestamp(item_date_object):
                #Function to convert datetime entries from django format to json iso format
                if isinstance(item_date_object, (datetime.date, datetime.datetime)):
                    return item_date_object.isoformat()

            json_data = json.dumps(form_data, default=convert_timestamp)#dumps()returns data as string
            json_data = json.loads(json_data)#loads() converts string to json format

            resp = requests.post('http://127.0.0.1:8000/platform/', json=json_data)#http://10.105.24.250:8000/course/
            #json_data in json format is passed on to backend platform API
            if resp.status_code != 201:
                raise ApiError(resp.status_code)
            print('\n\nCreated task. ID: {} PLATFORM NAME: {} \n\n'.format(resp.json()["id"],resp.json()["thirdparty_platform_name"]))#resp consists the tuple which was just added

            return render(request, 'result.html',
                {"done":True,
                "form_name":"platform"
                })

        else:
            #condition when post is unsuccessfull, and/or form is invalid
            print("FORM IS NOT VALID")
            return render(request, 'result.html',
                          {'form': form ,
                          'done':False,
                          "form_name":"platform"
                          })
    else:
        form = platform_form()
        return render(request, 'form_platform.html', {
                "form":form,
                "form_name":"platform"
            })



def _url(path):
    return 'http://127.0.0.1:8000' + path

# def _url1(path):
#     return 'http://localhost:8000' + path

def present(name,names):

    flag = True
    for i in range(len(names)) :
        if name == names[i]:
            flag = False

    # print(flag)
    return flag


unique_keys=[]
courseNames=[]
platform_ids=[]
platformNames=[]
platformUrls=[]
flag = 0
tmp_keys = []
tmp_urls  = 0
dictionary = dict()
courses = requests.get(_url('/course'))
# unique_keys.clear()
# courseNames.clear()
# platform_ids.clear()
# platformNames.clear()
platforms = requests.get(_url('/platform'))
# print(courses.json())
platforms = platforms.json()
courses = courses.json()
for course in courses:
    # if course['display_name'] not in names:
    if present(course['display_name'],courseNames) :
        unique_keys.append(course['coursekey'])
        courseNames.append(course['display_name'])
        for platform in course['platforms']:
            if platform not in dictionary:
                dictionary[platform]=[]
            dictionary[platform].append(len(courseNames)-1)
for platform in platforms:
    if present(platform['thirdparty_platform_name'],platformNames):
        platformNames.append(platform['thirdparty_platform_name'])
        platform_ids.append(platform['id'])
        platformUrls.append(platform['ServerUrl'])
# pla

@csrf_exempt
# @api_view(['POST',])
def grades_view(request):


    global unique_keys,courseNames,platform_ids,platformNames,dictionary,platformUrls
    global flag, tmp_keys, tmp_urls
    if request.method == 'GET':
        flag=0
        unique_keys=[]
        courseNames=[]
        platform_ids=[]
        platformNames=[]
        platformUrls=[]
        dictionary = dict()
        courses = requests.get(_url('/course'))
        # unique_keys.clear()
        # courseNames.clear()
        # platform_ids.clear()
        # platformNames.clear()
        platforms = requests.get(_url('/platform'))
        # print(courses.json())
        platforms = platforms.json()
        courses = courses.json()
        for course in courses:
            # if course['display_name'] not in names:
            if present(course['display_name'],courseNames) :
                unique_keys.append(course['coursekey'])
                courseNames.append(course['display_name'])
                for platform in course['platforms']:
                    if platform not in dictionary:
                        dictionary[platform]=[]
                    dictionary[platform].append(len(courseNames)-1)
        for platform in platforms:
            if present(platform['thirdparty_platform_name'],platformNames):
                platformNames.append(platform['thirdparty_platform_name'])
                platform_ids.append(platform['id'])
                platformUrls.append(platform['ServerUrl'])
    if request.method == "POST" :
        if 'selectedOptions' in request.POST:
            if not flag:
                # direct to html with appropriate error message
                raise Http404
            try:
                index = request.POST.getlist('courseList',None)[0]
                index = int(index)
                print(tmp_urls)
                objs = requests.get(_url('/api/grade/v0/grades/'+tmp_urls+'/'+tmp_keys[index]))
                objs  = objs.json()
                # print(objs)
                return render(request,'display_grades.html',{'objs':objs})
            except:
                print("except-block")
                objs = requests.get(_url('/api/grade/v0/grades/'+tmp_urls))
                objs  = objs.json()
                return render(request,'display_grades.html',{'objs':objs})
        elif 'allPlatforms' in request.POST:
            objss = requests.get(_url('/api/grade/v0/grades'))
            # objs = objs[0]
            objss  = objss.json()
            # print(objss)
            return render(request,'display_grades_all_platforms.html',{'objss':objss})
    print(platformNames)
    print(platform_ids)
    return render(request,'grade_course_list.html',{'courseNames':courseNames,'platformNames':platformNames})

@csrf_exempt
def grade_ajax_view(request):
    global unique_keys
    global courseNames,platformUrls
    global flag, tmp_keys, tmp_urls
    if request.method=='POST':
        flag=1
        pid = request.POST['pid']
        print(platformNames)
        # print(request.POST['platformNames'])
        print(pid)
        print(type(pid))
        print(platform_ids)
        pid = int(pid)
        tmp_urls = platformUrls[pid]
        pid = platform_ids[pid]
        tmp1=[]
        tmp2=[]
        for i in dictionary[pid]:
            tmp1.append(unique_keys[i])
            tmp2.append(courseNames[i])
        print(tmp1)
        print(tmp2)
        tmp_keys = tmp1
        # courseNames = tmp2
        return render(request,'grade_course_list_ajax.html',{'courseNames':tmp2,'platformNames':platformNames})


def courseImportForm(request):
    '''
    Function to handle a post request coming from form.html
    '''
    if request.method == 'POST':
        form = course_import(request.POST)

        if form.is_valid():
            print("FORM IS VALID")
            form_data = form.cleaned_data#retrieve form content

            json_data = json.dumps(form_data)#dumps()returns data as string
            json_data = json.loads(json_data)#loads() converts string to json format

            resp = requests.post('http://127.0.0.1:8000/course_import/', json=json_data)
            #json_data in json format is passed on to backend of Clone API
            if resp.status_code != 201:
                raise ApiError(resp.status_code)
            print('\n\nCreated task. ID: {}\n\n'.format(resp.json()["id"]))#resp consists the tuple which was just added

            return render(request, 'result.html',
                {"done":True,
                "form_name":"post_import"
                })

        else:
            #condition when post is unsuccessfull, and/or form is invalid
            print("FORM IS NOT VALID")
            return render(request, 'result.html',
                          {'form': form ,
                          'done':False,
                          "form_name":"post_import"
                          })
    else:
        form = course_import()
        return render(request, 'course_import.html', {
                "form":form,
                "form_name":"post_import"
            })
