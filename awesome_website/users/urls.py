from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^register/', register, name='register')
]
