from django.test import TestCase
from django.test import Client
c = Client()
response = c.post('userlist', {'title': '1'})
response.status_code
response = c.get('/userlist')
response.content
# Create your tests here.
