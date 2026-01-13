from django.urls import path
from . import views

app_name = 'shopapp'

urlpatterns = [
    path('', views.ShopIndexView.as_view(), name='index'),
    path('groups/', views.ShopGroupsView.as_view(), name='group'),
    path('products/', views.ProductListView.as_view(), name='products_list'),
    path('products/create/', views.create_product, name='create_products'),
    path('products/creation/', views.CreateProductView.as_view(), name='creation_products'),
    path('products/<int:pk>/', views.ProductDetailsView.as_view(), name='products_details'),
    path('orders/', views.orders_list, name='orders_list'),
]