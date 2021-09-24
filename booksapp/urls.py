from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg, name='home'),
    path('form', views.submitform, name='form-submit'),
    path('home/', views.home, name='home')
]