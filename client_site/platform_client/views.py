from django.shortcuts import render
import requests
from .forms import platform_form
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder


class ApiError(Exception):
    """A Custom API Error Exception Handling class"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError Occured : Status Code = {} ".format(self.status)

def get_form(request):
    '''
    Function to render empty django form in form.html
    '''
    form = platform_form()
    return render(request, 'form.html', {
            "form":form
        })

def post_form(request):
    '''
    Function to handle a post request coming from form.html
    '''
    if request.method == 'POST':
        form = platform_form(request.POST)

        if form.is_valid():
            
            form_data = form.cleaned_data#retrieve form content 

            def convert_timestamp(item_date_object):
                #Function to convert datetime entries from django format to json iso format
                if isinstance(item_date_object, (datetime.date, datetime.datetime)):
                    return item_date_object.isoformat()

            json_data = json.dumps(form_data, default=convert_timestamp)#dumps()returns data as string
            json_data = json.loads(json_data)#loads() converts string to json format
            
            resp = requests.post('http://127.0.0.1:8000/get_platform/', json=json_data)
            #json_data in json format is passed on to backend get_platform API
            if resp.status_code != 201:
                raise ApiError(resp.status_code)
            print('Created task. ID: {}'.format(resp.json()["id"]))#resp consists the tuple which was just added

            return render(request, 'result.html',{"done":True})
            
        else:
            #condition when post is unsuccessfull, and/or form is invalid
            return render(request, 'result.html', 
                          {'form': form ,
                          'done':False
                          })
        
    


