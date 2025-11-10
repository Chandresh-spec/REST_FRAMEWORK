from django.urls import path
from .views import StudentDetails

urlpatterns = [
    path('students',StudentDetails),

]
