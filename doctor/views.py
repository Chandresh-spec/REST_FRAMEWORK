from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorSerializer
from .models import DoctorModel
# Create your views here.




class Doctor_View(viewsets.ModelViewSet):
    queryset=DoctorModel.objects.all()
    serializer_class=DoctorSerializer