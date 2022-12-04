from django.test import TestCase

from mainapp.models import Product

class ModelTest(TestCase):
    
    def setUp(self):
        self.product = Product.objects.create(
            name="MacBook", 
            price=10
        )

    def test_product_model(self):
        product = self.product
        self.assertTrue(isinstance(product, Product))
        