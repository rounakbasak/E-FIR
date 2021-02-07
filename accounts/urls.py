from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.indexView,name="home"),
    path('login-as-police/',loginaspoliceView.as_view(),name="login-as-police_url"),
    path('create-police/',create-policeView,name="create-police_url"),
    path('logout/',LogoutView.as_view(next_page='login-option'),name="logout"),
    path('create-user/',create-userView,name="create-user_url"),
    path('login-as-user/',loginasuserView.as_view(),name="login-as-user_url"),
    path('police-page/',police-pageView,name="police-page"),
    path('user-page/',user-pageView,name="user-page"),
]