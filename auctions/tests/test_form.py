from django.test import TestCase
from django.test import Client
from auctions import models
from django.test.utils import setup_test_environment
from auctions.models import Bid, AuctionItem, User


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(first_name="Brittany", last_name = "Leykam", email = "bleykam@gmail.com", id = 1, username="bleykam")
        item = AuctionItem.objects.create( id = 1, title = 'Cat', description = "Fat, furry feline.  Eats and sleeps mostly.  Pure EVIL", \
                           price = 2.50, category = "Pets", image = "Blank", comment = "EWWWW", bidcount = 5, active = True )

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test_get_absolute_url(self):
        item = AuctionItem.objects.get(id=1)

        self.assertEqual(AuctionItem.objects.get(id=1), '/auctions/1')