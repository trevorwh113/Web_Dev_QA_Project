"""
Temporary new test case using Playwright and pytest-flask
to run and verify a live server.
"""

from flask import url_for
from playwright.sync_api import expect

import time

def test_some_test(live_server, page):    
    page.goto(url_for('home', _external=True))
    page.screenshot(path="screenshots/google.png")

    # expect(page).to_have_title("Home")
    # assert "Home" in browser.title