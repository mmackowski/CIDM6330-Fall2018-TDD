from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

        # # request = HttpRequest()
        # # response = home_page(request)
        # html = response.content.decode('utf8')
        # # expected_html = render_to_string('home.html')

        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        # self.assertTemplateUsed(response, 'home.html')

# Create your tests here.
