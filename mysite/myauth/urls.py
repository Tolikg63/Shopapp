from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'myauth'

urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(template_name='myauth/login.html', 
        redirect_authenticated_user=True), 
        name='login'),
        # path('logout/', views.MyLogoutView.as_view(), name='logout'),
        path('logout/', views.logout_view, name='logout'),
        path('about-me/', views.AboutMeView.as_view(), name='about-me'),
        path('register/', views.RegisterView.as_view(), name='register'),
]