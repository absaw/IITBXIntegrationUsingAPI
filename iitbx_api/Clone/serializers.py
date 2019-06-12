from rest_framework import serializers
from .models import repoclone

class repocloneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = repoclone
        fields = '__all__'
        #fields = ('ticker','open')
        

