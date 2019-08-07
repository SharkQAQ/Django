from django.urls import path
from . import views
urlpatterns = [
    path('student/', views.students),
    path('', views.index),
    path('main/', views.main),
    path('login/', views.login),
    path('logout/', views.logout),
    path('regist/', views.regist),
]
