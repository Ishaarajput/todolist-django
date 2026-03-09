from django.urls import path
from todo import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup,name='register'),
    path('login/',views.login,name='login')
]