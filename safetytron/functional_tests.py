#!/usr/bin/env python

from selenium import webdriver

import unittest

# Feature: Compare two images of a city for safety
#   In order to decide the safety of a city
#   I want users to compare random images from google streetview

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_user_can_see_our_app(self):
        """
        Scenario: a user visits our website
            Given: a visitor goes to the URL
            When: they look at the title
            Then: they see the application name
        """
        self.browser.get('http://localhost:31337')
        self.assertIn('safetytron', self.browser.title)
        self.fail("finish the tests")
        
if __name__ == '__main__':
    unittest.main()
