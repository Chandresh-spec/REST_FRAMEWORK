from django.urls import path,include
from .views import Student_View
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from .views import Student_ViewSet
router=SimpleRouter()
router.register('student',Student_ViewSet)





urlpatterns = [
    path('', include(router.urls)),
    path('person/',Student_View.as_view()),


]
