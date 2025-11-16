from django.urls import path,include
from .views import Student_View
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from .views import Student_ViewSet,Simple_ViewSet,StudentView,LoginView
router=SimpleRouter()
router.register('student',Student_ViewSet)


router1=DefaultRouter()
router1.register('name',Simple_ViewSet,basename='name')


urlpatterns = [
    path('', include(router.urls)),
    path('',include(router1.urls)),
    path('person/',Student_View.as_view()),
    path('register/',StudentView.as_view()),
    path('login/',LoginView.as_view())



]
