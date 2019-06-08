from rest_framework import serializers
from .models import CourseOverview

class CourseOverviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseOverview
        fields = '__all__'
        #fields = ('specicfic_list_names_from_json_file')
        

