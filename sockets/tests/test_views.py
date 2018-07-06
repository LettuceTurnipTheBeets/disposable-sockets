from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 301)
