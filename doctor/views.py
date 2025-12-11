from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorSerializer
from .models import DoctorModel
from rest_framework.permissions import IsAuthenticated

# Create your views here.




class Doctor_View(viewsets.ModelViewSet):
    queryset=DoctorModel.objects.all()
    serializer_class=DoctorSerializer
    permission_classes=[IsAuthenticated,IsDoctor]