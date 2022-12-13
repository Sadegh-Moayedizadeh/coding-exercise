import json
from decimal import Decimal

from app.forms import ProductForm
from app.models import Category, Order, OrderItem, Product
from django.shortcuts import reverse
from django.test import Client, TestCase


class TestSample(TestCase):
    def setUp(self):
        self.client = Client()
        order = Order.objects.create(address="torgozabad", email="fashabori@email.com")
        category = Category.objects.create(name="bomb")
        product = Product.objects.create(category=category, name="atomic_bomb", price=Decimal("1611.29"), stock=5)
        OrderItem.objects.create(order=order, product=product)

    def test_available_model_manager_default_manager(self):
        self.assertEqual(Product._meta.default_manager, Product.objects)

    def test_available_manager_should_return_product_with_non_zero_stock(self):
        category = Category.objects.create(name="a_category")
        product = Product.objects.create(
            category=category,
            name='a_product',
            price=Decimal('1611.29'),
            stock=2)
        qs = Product.available.filter(name='a_product')
        self.assertTrue(qs.exists())
        self.assertEqual(qs.first(), product)

    def test_available_manager_should_not_return_product_with_zero_stock(self):
        category = Category.objects.create(name="a_category")
        product = Product.objects.create(
            category=category,
            name='a_product',
            price=Decimal('1611.29'),
            stock=0)
        qs = Product.available.filter(name='a_product')
        self.assertFalse(qs.exists())

    def test_correct_model_form(self):
        data = {
            "category": 1,
            "name": "pc",
            "description": "dfkjas;ldfkjas;ldfjkc",
            "price": "999.00",
            "stock": 2,
        }
        form = ProductForm(data)
        self.assertTrue(form.is_valid())

    def test_price_bigger_than_1000_should_fail_validation(self):
        data = {
            "category": 1,
            "name": "pc",
            "description": "dfkjas;ldfkjas;ldfjkc",
            "price": "1001",
            "stock": 2,
        }
        form = ProductForm(data)
        self.assertFalse(form.is_valid())

    def test_description_less_than_20_chars_should_fail_validation(self):
        data = {
            "category": 1,
            "name": "pc",
            "description": "less than 20 chars",
            "price": "10",
            "stock": 2,
        }
        form = ProductForm(data)
        self.assertFalse(form.is_valid())

    def test_checkout(self):
        expected = {"total_price": "1611.290000"}
        res = self.client.get(reverse('checkout', args=(1,)))
        data = json.loads(res.content.decode())
        self.assertEqual(Decimal(expected["total_price"]), Decimal(data['total_price']))

    def test_not_existing_order_should_return_404(self):
        res = self.client.get(reverse('checkout', args=(1000,)))
        self.assertEqual(res.status_code, 404)
