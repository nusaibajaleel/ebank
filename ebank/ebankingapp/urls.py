from django.urls import path
from.  import views

app_name='ebankingapp'

urlpatterns=[
    path('',views.allBranches,name='allBranches'),
    path('<slug:c_slug>/',views.allBranches,name='branch_by_district'),
    path('account/',views.AccountType,name='account'),
    path('<slug:c_slug>/<slug:branch_slug>/',views.BranchDetail,name='branchdetail'),
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('regform',views.regform,name='regform'),


]