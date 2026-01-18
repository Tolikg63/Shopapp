from django.test import TestCase
from django.urls import reverse
from .utils import add_two_numbers


class AddTwoNumbersTestCase(TestCase):
    def test_add_two_numbers(self):
        result = add_two_numbers(2, 2)
        self.assertEqual(result, 4)


class ProductCreateViewTestCase(TestCase):
    def test_create_product(self):
        response = self.client.post(
            reverse('shopapp:creation_products'),
            {
                'name': 'Chair',
                'price': '1231.2',
                'description': "A good chair",
                'discount': '10',
            }
        )
        self.assertRedirects(response, reverse('shopapp:creation_products'))
