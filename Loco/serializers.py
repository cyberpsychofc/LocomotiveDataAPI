from rest_framework import serializers
from .models import Locomotive

class LocomotivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locomotive
        fields = ['motive_power','gauge','name', 'traction', 'usage', 'series', 'numbers', 'img_src', 'manufacturer','axles','numbers_built', 'production','power', 'status']
    
    def broad_electric(LocomotiveSerializer):
        LocomotiveSerializer.Meta.fields = ['motive_power','gauge','name', 'traction', 'usage', 'series', 'img_src', 'manufacturer','axles','numbers_built', 'production','power', 'status']
    