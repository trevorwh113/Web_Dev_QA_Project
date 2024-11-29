"""
This test file implements an integration/end-to-end test for
the html button navigation between pages. NOTE: Requires the
app to be concurrently running at the URL (the local host).
"""
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re

# URL of the development server -----------------------------
URL = "http://127.0.0.1:5000"

# Success cases ---------------------------------------------
def test_home_and_back_buttons():
    """
    Success Case: Navigates from the home page to all other 
    accessible implemented pages. 
    """    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate through the client pages.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JOHN DOE").click()
        expect(page).to_have_title(re.compile("Client Page"))
        page.get_by_role("button", name="Create Prescription").click()
        expect(page).to_have_title(re.compile("Prescription Creation"))
        
        # Naviguate back to the home page.
        page.get_by_role("button", name="Cancel").click()
        expect(page).to_have_title(re.compile("Client Page"))
        page.get_by_test_id("back").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_test_id("back").click()
        expect(page).to_have_title(re.compile("Home"))

        # Naviguate through the inventory page and back.
        page.get_by_role("button", name="Search Inventory").click()
        expect(page).to_have_title(re.compile("Search Inventory"))
        page.get_by_test_id("back").click()
        expect(page).to_have_title(re.compile("Home"))

        # Naviguate to the supply page.
        page.get_by_role("button", name="Manage Supply Orders").click()
        expect(page).to_have_title(re.compile("Unavailable"))

        browser.close()