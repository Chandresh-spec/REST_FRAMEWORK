from django.urls import path,include
from .views import Student_View
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from .views import Student_ViewSet,Simple_ViewSet,StudentView,LoginView,Info_views,Product_views,TeacherLogin,Login_views
from . import views
router=SimpleRouter()
router.register('student',Student_ViewSet)
router.register('prod',Product_views)






urlpatterns = [
    path('', include(router.urls)),
    path('person/',Student_View.as_view()),
    path('register/',StudentView.as_view()),
    path('login/',LoginView.as_view()),
    path('info/',Info_views.as_view()),
    path('teacher/',views.teacher_view,name='teacher'),
    path('tlogin/',TeacherLogin.as_view()),
    path('treg/',Login_views.as_view())



]
