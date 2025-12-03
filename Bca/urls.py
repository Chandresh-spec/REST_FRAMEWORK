from django.urls import path,include
from .views import Student_View
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from .views import Student_ViewSet,Simple_ViewSet,StudentView,LoginView,Info_views,Product_views,TeacherLogin,Login_views,Student_api,Tester,CustomLoginAPI,basic_view
from . import views

router=SimpleRouter()
router.register('student',Student_ViewSet)
router.register('prod',Product_views)
from rest_framework.authtoken import views







urlpatterns = [
    path('', include(router.urls)),
    path('person/',Student_View.as_view()),
    path('register/',StudentView.as_view()),
    path('login/',LoginView.as_view()),
    path('info/',Info_views.as_view()),
    path('tlogin/',TeacherLogin.as_view()),
    path('treg/',Login_views.as_view()),
    path('st/',Student_api.as_view()),
    path('custom/',Tester.as_view()),
    path('cs/',CustomLoginAPI.as_view()),
    path('basic/',basic_view.as_view())



]
