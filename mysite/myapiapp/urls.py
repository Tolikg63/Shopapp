from django.urls import path
from . import views

app_name = 'myapiapp'

urlpatterns = [
    path('hello/', views.hello_world_view, name='hello'),
    path('groups/', views.group_view, name='group'),
    path('users/', views.UserListView.as_view(), name='user'),
    path('groups-list/', views.GroupListView.as_view(), name='group-list'),
]