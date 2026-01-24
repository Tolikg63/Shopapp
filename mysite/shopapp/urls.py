from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'shopapp'

routers = DefaultRouter()
routers.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.ShopIndexView.as_view(), name='index'),
    path('groups/', views.ShopGroupsView.as_view(), name='group'),
    path('products/create/', views.create_product, name='create_products'),
    path('products/creation/', views.CreateProductView.as_view(), name='creation_products'),
    path('products/', views.ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductDetailsView.as_view(), name='products_details'),
    path('orders/', views.orders_list, name='orders_list'),
    path('api/', include(routers.urls)),
]