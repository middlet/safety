"""
these are the tests for the main application
"""

from django.core.urlresolvers import resolve, reverse
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from safety.views import home_page
from safety.views import update_on_click

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
        
    def test_click_page_resolves_correctly(self):
        found = resolve('/api/update')
        self.assertEqual(found.func, update_on_click)
        
    def test_selection_updates_database(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['click'] = '1'
        
        response = update_on_click(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
        
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
