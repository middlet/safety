"""
these are the tests for the main application
"""

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from safety.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        actual_html = response.content.decode()
        self.assertEqual(self.strip_img(actual_html), self.strip_img(expected_html))
        
        
    def strip_img(self, html):
        """
        strip the image tags which are randomly generated
        """
        p1 = html.find('<img')
        p2 = html.find('">',p1+1)
        p3 = html.find('<img', p2+1)
        p4 = html.find('">', p3+1)
        
        html = html[:p1-1] + html[p2+1:p3-1] + html[p4+1:]
        return html        
