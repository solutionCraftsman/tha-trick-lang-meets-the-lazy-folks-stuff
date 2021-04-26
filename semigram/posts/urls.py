from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('post_creation/', views.post_creation, name='post_creation'),
]
