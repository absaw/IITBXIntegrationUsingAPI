from django.shortcuts import render
import requests
from .forms import platform_form, course_form
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder


class ApiError(Exception):
    """A Custom API Error Exception Handling class"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError Occured : Status Code = {} ".format(self.status)

def index(request):
    return render(request, 'index.html')

def get_course_form(request):
    '''
    Function to render empty django form in form.html
    '''
    form = course_form()
    return render(request, 'form_course.html', {
            "form":form,
            "form_name":"course"  
        })

def post_course_form(request):
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
            
            resp = requests.post('http://10.105.24.250:8000/get_course/', json=json_data)
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

def get_platform_form(request):
    '''
    Function to render empty django form in form.html
    '''
    form = platform_form()
    return render(request, 'form_platform.html', {
            "form":form,
            "form_name":"platform"
        })

def post_platform_form(request):
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
            
            resp = requests.post('http://10.105.24.250:8000/get_platform/', json=json_data)#http://10.105.24.250:8000/get_course/
            #json_data in json format is passed on to backend get_platform API
            if resp.status_code != 201:
                raise ApiError(resp.status_code)
            print('\n\nCreated task. ID: {}\n\n'.format(resp.json()["id"]))#resp consists the tuple which was just added

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
        
    


