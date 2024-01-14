from. import views
from django.urls import path

app_name='credentials'

urlpatterns = [

    path('', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form',views.form,name='form'),
    path('regform',views.regform,name='regform'),
    path('signout',views.signout,name='signout'),


    ]