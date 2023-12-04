import unittest
from Product import Product
from Shop import Shop

class ShopTest(unittest.TestCase):
    def setUp(self):
        self.a = Product('apple', 5)
        self.b = Product('strawberry', 15)
        self.c = Product('banana', 10)
        self.d = Product('watermelon', 8)
        self.product_list = [self.a, self.b, self.c, self.d]
        self.shop = Shop(self.product_list)

    def test_get_products(self):
        for product in self.product_list:
            self.assertIsInstance(product, Product)

    def test_set_products(self):
        self.failureException(self.shop.set_products(self.product_list), self.shop)

    def test_sorted_list_products(self):
        shop = self.shop.get_sorted_list_products()
        for i in range(len(shop) - 1):
            tmp = shop[i].get_cost()
            self.assertGreaterEqual(shop[i + 1].get_cost(), tmp)

    def test_most_expensive_product(self):
        self.assertEqual(self.shop.get_most_expensive_product().get_cost(),
                         max(self.product_list, key=lambda x: x.get_cost()).get_cost())


if __name__ == "__main__":
    unittest.main(verbosity=2)

# $ python -m unittest Shop_unittest.py -v