from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write("no order yet")
            return
        products = Product.objects.all()

        for product in products:
            order.products.add(product)
        order.save()