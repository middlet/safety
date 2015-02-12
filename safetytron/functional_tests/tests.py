from django.test import LiveServerTestCase

from pyvirtualdisplay import Display
from selenium import webdriver

import unittest

# Feature: Compare two images of a city for safety
#   In order to decide the safety of a city
#   I want users to compare random images from google streetview

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def test_user_can_see_our_app(self):
        self.browser.get(self.live_server_url)
        """
        Scenario: a user visits our website
            Given: a visitor goes to "/"
            When: they look at the titlebar
            Then: they see the application name
        """
        self.assertIn('safetytron', self.browser.title)

        """
        Scenario: a user visits our website
            Given: a visitor goes to "/"
            When: they look at the page
            Then: they see a title
        """
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('safetytron', header_text)
        
        """
        Scenario: a user visits and sees the comparison images
            Given: a visitor goes to "/"
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
        Scenario: a user visits and sees two distinct images
            Given: a visitor goes to "/"
            When: they look at the page
            Then: they see image1 which is different to image2
        """
        self.assertNotEqual(image1.get_attribute('src'), image2.get_attribute('src'))
        
        """
        Scenario: a user visits and sees a counter for number of uses
            Given: a visitor goes to "/"
            When: they look at the bottom of the page
            Then: they see a counter for number of clicks
        """
        counter = self.browser.find_element_by_id('counter')
        self.assertIsNotNone(counter)
        """
        Scenario: a user votes for an image
            Given: a visitor clicks on an image
            When: they look at the click counter
            Then: the counter has incremented
        """
        counter_text = counter.text
        ncount_before = int(counter_text.split()[0])
        image1.click()
        counter_text = counter.text
        ncount_after = int(counter_text.split()[0])
        self.assertNotEqual(ncount_before, ncount_after)

        # this is here to remind us we need to continue unit tests
        self.fail("finish the tests")
        
