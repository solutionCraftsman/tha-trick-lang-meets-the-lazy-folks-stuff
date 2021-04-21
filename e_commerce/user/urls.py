from django.urls import path
from . import views

urlpatterns = [
    path('create_merchant/', views.create_merchant, name='create_merchant')
]
