from rest_framework import serializers
from .models import DroneData

class DroneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneData
        fields = '__all__'
