#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:31337')

assert 'Django' in browser.title
