"""
This test file implements an integration/end-to-end test for
the html button navigation between pages.
"""
from flask import url_for
from playwright.sync_api import expect
import re

# Success cases ---------------------------------------------
def test_home_and_back_buttons(live_server, page):
    """
    Success Case: Navigates from the home page to all other 
    accessible implemented pages.
    """    
    # Load the home page and make sure it comes up.
    page.goto(url_for('home', _external=True))
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
