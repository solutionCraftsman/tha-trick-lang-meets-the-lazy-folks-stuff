from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_index, name='gallery_index'),
    path('<int:pk>/', views.man_details, name='man_details')
]
