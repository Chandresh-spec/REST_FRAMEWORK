from django.urls import path,include
from .views import StudentDetails,Student_View
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router=DefaultRouter()
router.register(r'students',StudentViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('students',StudentDetails),
    path('person/',Student_View.as_view())


]
