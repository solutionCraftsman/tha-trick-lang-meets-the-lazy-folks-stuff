from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello'),
    path('fiver/', views.fiver, name='hello')
]
