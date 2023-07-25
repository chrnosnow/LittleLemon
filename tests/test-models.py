from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView


class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_getall(self):
        item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        item2 = MenuItem.objects.create(title="Omlette", price=45, inventory=63)
        item3 = MenuItem.objects.create(title="Pancakes", price=27, inventory=503)
        self.assertEqual(MenuItem.objects.all().count(), 3)
    
