from rest_framework import serializers
from .models import IntegratedPlatforms

class IntegratedPlatformsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IntegratedPlatforms
        fields = '__all__'
        #fields = ('specicfic_list_names_from_json_file')
        

