from django.contrib import admin
from .models import Product, Order


@admin.action(description='Archive products')
def mark_archived(modeladmin, request, queryset):
    queryset.update(archived=True)

@admin.action(description='Unarchive products')
def mark_unarchived(modeladmin, request, queryset):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [mark_archived, mark_unarchived]
    list_display = ['pk', 'name',  'description_short', 'price', 'discount', 'archived']
    list_display_links = 'name',
    search_fields = 'name', 'description'
    fieldsets = [
        (None, {
            'fields': ('name', 'description')
        }),
        ('Price options', {
            'fields': ('price', 'discount'),
            'classes': ('wide',)
        }),
        ('Extra options', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': "Extra options for delete"
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 40:
            return obj.description
        return obj.description[:48] + '...'


class ProductInline(admin.TabularInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline] 
    list_display = ['delivery_address', 'promocode', 'created_at', 'verbose_name']

    def get_queryset(self, request):
        return Order.objects.select_related('user')
    
    def verbose_name(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username