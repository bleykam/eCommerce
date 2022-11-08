from django.test import TestCase
from django.test import Client









class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def test_renew_form_date_field_help_text(self):
        first_type = type(lst[0])
        for item in lst:
            assert type(item) == first_type
        form = BidForm()
        self.assertEqual(form.fields['user'], self.client.response.context['user'])
