from rest_framework import serializers
from .models import Locomotive
from collections import OrderedDict

class LocomotivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locomotive
        fields = '__all__'
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] != "NA"])
    def electric_filter(LocomotiveSerializer):
        LocomotiveSerializer.Meta.fields = ['motive_power','gauge','name', 'traction', 'usage', 'series', 'img_src', 'manufacturer','axles','numbers_built', 'production','power', 'status']
    def broadDiesel_filter(LocomotiveSerializer):
        LocomotiveSerializer.Meta.fields = ['motive_power','gauge','name', 'usage', 'series', 'numbers', 'img_src', 'manufacturer','axles','numbers_built', 'production','power', 'status']
    def standard_filter(LocomotiveSerializer):
        LocomotiveSerializer.Meta.fields = ['motive_power','gauge','name', 'usage', 'series', 'img_src', 'manufacturer','axles','numbers_built', 'production','power', 'status']