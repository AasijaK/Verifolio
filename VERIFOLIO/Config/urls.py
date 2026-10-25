from django.urls import path

from Verifolio.VERIFOLIO.Config import views

urpatterns = [
    path('', views.Index, name='home'),
    
]