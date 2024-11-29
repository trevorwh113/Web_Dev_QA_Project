"""
This test file implements an end-to-end test for search 
functionality in both the drug and client contexts by simulating
a few search queries. NOTE: Requires the app to be concurrently 
running at the URL (the local host).
"""
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re

# URL of the development server -----------------------------
URL = "http://127.0.0.1:5000"

# Success cases ---------------------------------------------
def test_drug_search():
    """
    Success Case: Searches for a few clients in the client
    pages by actually using the web page interface.
    """    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))

        # Naviguate through the inventory page and back.
        page.get_by_role("button", name="Search Inventory").click()
        expect(page).to_have_title(re.compile("Search Inventory"))

        # 1. Successful search by name // not done
        page.get_by_placeholder("Drug Name or DIN...").fill("pa")
        page.get_by_test_id("submit").click()

        browser.close()