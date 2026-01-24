from timeit import default_timer
from django.contrib.auth.models import Group
from .models import Product, Order
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpRequest, HttpResponse
from .forms import ProductForm, GroupForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from rest_framework.viewsets import ModelViewSet

from .forms import ProductForm
from .models import Product, Order
from .serializers import ProductSerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ShopIndexView(View):
    def get(self, request):
        products = [
            ("Laptop", 1999),
            ("Desktop", 2999),
            ("Smartphone", 999)
        ]
        context = {
            "time_running": default_timer(),
            "products": products
        }
        return render(request, "shopapp/shop-index.html", context)


# def shop_index(request):
#     products = [
#         ("Laptop", 1999),
#         ("Desktop", 2999),
#         ("Smartphone", 999)
#     ]
#     context = {
#         "time_running": default_timer(),
#         "products": products
#     }
#     return render(request, "shopapp/shop-index.html", context)


class ShopGroupsView(View):
    def get(self, request):
        context = {
            'form': GroupForm(),
            "groups": Group.objects.prefetch_related("permissions").all()
        }
        return render(request, "shopapp/group-list.html", context)
    def post(self, request):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


# def shop_groups(request):
#     context = {"groups": Group.objects.prefetch_related("permissions").all()}
#     return render(request, "shopapp/group-list.html", context)

# class ProductDetailsView(View):
#     def get(self, request, pk):
#         context = {
#             # 'product': Product.objects.get(pk=pk)
#             'product': get_object_or_404(Product, pk=pk)
#         }
#         return render(request, 'shopapp/products-details.html', context)
    
class ProductDetailsView(DetailView):
    template_name = 'shopapp/products-details.html'
    model = Product
    context_object_name = 'product'


# class ProductListView(TemplateView):
#     template_name = 'shopapp/products-list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.all()
#         return context

class ProductListView(ListView):
    template_name = "shopapp/products-list.html"
    model = Product
    context_object_name = 'products'

# def products_list(request):
#     context = {
#         "products": Product.objects.all()
#     }
#     return render(request, "shopapp/products-list.html", context)


def orders_list(request):
    context = {"orders": Order.objects.select_related("user").all()}
    return render(request, "shopapp/orders-list.html", context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse("shopapp:products_list")
            return redirect(url)
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "shopapp/create-product.html", context=context)


class CreateProductView(CreateView):
    template_name = 'shopapp/create-product2.html'
    model = Product
    fields = 'name', 'description', 'price', 'discount'
    success_url = reverse_lazy('shopapp:products_list')