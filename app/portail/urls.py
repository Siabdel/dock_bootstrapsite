from django.urls import path
from portail import views

urlpatterns = [
    path('home/', views.home, name='home'),
] 