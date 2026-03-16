from django.urls import path
from todo import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup,name='register'),
    path('login/',views.login,name='login'),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addtask/",views.addtask),
    path("complete/<int:id>/",views.complete),
    path("delete/<int:id>/",views.delete),
    path("logout/", views.logout, name="logout"),
]