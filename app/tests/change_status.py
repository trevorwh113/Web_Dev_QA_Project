"""
This test file implements an end-to-end test for changing prescription
status on the client info page. NOTE: Requires the app to be concurrently 
running at the URL (the local host).
"""
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re

# URL of the development server -----------------------------
URL = "http://127.0.0.1:5000"

# Success cases ---------------------------------------------
def test_change_active_to_active_1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate to a client info page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JOHN DOE").click()
        expect(page).to_have_title(re.compile("Client Page"))
        

        # find first prescription in list and change its status
        con = page.get_by_test_id('A0')
        expect(con).to_be_visible()
        con.get_by_test_id('options').select_option("Ready")
        assert con.get_by_test_id('options').input_value() == '1'


        browser.close()

def test_change_active_to_active_2():
 
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate to a client info page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JOHN DOE").click()
        expect(page).to_have_title(re.compile("Client Page"))
        

        # find first prescription in list and change its status
        con = page.get_by_test_id('A0')
        expect(con).to_be_visible()
        con.get_by_test_id('options').select_option("Needs Filling")
        assert con.get_by_test_id('options').input_value() == '2'


        browser.close()

def test_change_active_to_inactive():

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate to a client info page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JOHN DOE").click()
        expect(page).to_have_title(re.compile("Client Page"))
        

        # Find the first prescriptions select box and change the prescription to inactive
        act = page.get_by_test_id('A0')
        expect(act).to_be_visible()
        content = act.text_content()
        act.get_by_test_id('options').select_option("Non-Active")

        # Check that the prescription got moved to the other list
        old = page.get_by_text(content)
        expect(old).to_be_visible()
        assert old.get_by_test_id('options').input_value() == '5'

        browser.close()

def test_change_inactive_to_active():
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
        
        # Navigate to a client info page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JOHN DOE").click()
        expect(page).to_have_title(re.compile("Client Page"))
        

        # Find the first prescriptions select box and change the prescription to active
        old = page.get_by_test_id('O0')
        expect(old).to_be_visible()
        content = old.text_content()
        old.get_by_test_id('options').select_option("Needs Filling")

        # Check that the prescription got moved to the other list
        act = page.get_by_text(content)
        expect(act).to_be_visible()
        assert act.get_by_test_id('options').input_value() == '2'

        browser.close()