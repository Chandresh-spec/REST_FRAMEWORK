from django.urls import path,include
from .views import Doctor_View
from rest_framework.routers import  DefaultRouter
router = DefaultRouter()
router.register('ele', Doctor_View, basename='doctor')
urlpatterns = [
    path("",include(router.urls)),
    

]
