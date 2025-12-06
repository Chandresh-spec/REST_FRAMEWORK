from rest_framework import serializers

from .models import DoctorModel




class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorModel
        fields="__all__"
        