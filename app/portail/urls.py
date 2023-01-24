from django.urls import path, include
from portail import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.PortailHome.as_view(), name='home_page'),
] 