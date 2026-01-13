from django.urls import path
from . import views

app_name = 'requestdataapp'

urlpatterns = [
    path('', views.req, name='req'),
    path('bio/', views.bio, name='bio'),
]
