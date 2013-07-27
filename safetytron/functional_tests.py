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
        self.browser.get('http://localhost:31337')
        """
        Scenario: a user visits our website
            Given: a visitor goes to the URL
            When: they look at the titlebar
            Then: they see the application name
        """
        self.assertIn('safetytron', self.browser.title)

        """
        Scenario: a user visits our website
            Given: a visitor goes to the URL
            When: they look at the page
            Then: they see a title
        """
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('safetytron', header_text)
        
        """
        Scenario: a user visits our website
            Given: a visitor goes to the URL
            When: they look at the page
            Then: they see image1
            Then: they see a button with "="
            Then: they see image2
        """
        image1 = self.browser.find_element_by_id('image1')
        image2 = self.browser.find_element_by_id('image2')
        button = self.browser.find_element_by_id('button')
        self.assertIsNotNone(image1)
        self.assertIsNotNone(image2)
        self.assertIsNotNone(button)
        
        """
        Scenario: a user visits our website
            Given: a visitor goes to the URL
            When: they look at the page
            Then: they see image1 which is different to image2
        """
        self.assertNotEqual(image1.get_attribute('src'), image2.get_attribute('src'))
        
        
        
        
        # this is here to remind us we need to continue unit tests
        self.fail("finish the tests")
        
if __name__ == '__main__':
    unittest.main()
