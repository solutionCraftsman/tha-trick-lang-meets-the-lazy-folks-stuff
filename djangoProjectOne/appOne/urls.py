from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('path-two/', views.path_two, name='path-two')
]
