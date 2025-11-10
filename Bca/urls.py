from django.urls import path
from .views import StudentDetails,Student_View

urlpatterns = [
    path('students',StudentDetails),
    path('person/',Student_View.as_view())

]
