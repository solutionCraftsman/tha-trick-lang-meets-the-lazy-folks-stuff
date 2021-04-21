from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:pk>', views.details, name='post_details'),
    path('create', views.create, name='create_post')
]
