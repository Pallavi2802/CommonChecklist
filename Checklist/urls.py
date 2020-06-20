from django.contrib import admin
from django.urls import path, include
from . import views
from Counselor import urls as urlsCounselors
from student import urls as urlsStudents

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('loginuser/', views.Login.as_view(), name="Loginuser"),
    path('signupuser/', views.Signup.as_view(), name="Signupuser"),
    path('logoutuser', views.Logout.as_view(), name="logoutuser"),
    path('counselor/', include(urlsCounselors)),
    path('changePassword/', views.ChangePassword.as_view(), name="changePassword"),
    path('student/', include(urlsStudents)),
    path('systemaccounts/', include('django.contrib.auth.urls'))
]
