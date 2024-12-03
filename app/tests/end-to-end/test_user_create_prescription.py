"""
This test file implements an end-to-end test for creating a new prescription for
a client. NOTE: Requires the app to be concurrently running at the URL (the
local host).
"""
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re
import random

# URL of the development server -----------------------------
URL = "http://127.0.0.1:5000"


def test_create_prescription():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate to a prescription creation page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JAINE FALL").click()
        expect(page).to_have_title(re.compile("Client Page"))
        page.get_by_role("button", name="Create Prescription").click()
        expect(page).to_have_title(re.compile("Prescription Creation"))

        # Randomize Doctor name
        name = "Dr. " + str(random.randint(0,999999999))

        # Fill in input and submit
        page.get_by_label("DIN").fill("999999")
        page.get_by_label("refill").fill("01/01/2025")
        page.get_by_placeholder("DR. XXX").fill(name)
        page.get_by_role("button", name="Submit").click()
        expect(page).to_have_title(re.compile("Client Page"))

        

        # Find prescription in list
        locator = page.get_by_text(name)
        expect(locator).to_be_visible()


        browser.close()



# Fail cases
def test_fail_prescription_noDIN():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate to a prescription creation page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JAINE FALL").click()
        expect(page).to_have_title(re.compile("Client Page"))
        page.get_by_role("button", name="Create Prescription").click()
        expect(page).to_have_title(re.compile("Prescription Creation"))

        # Randomize Doctor name
        name = "Dr. " + str(random.randint(0,999999999))

        # Fill in input and submit
        page.get_by_label("refill").fill("01/01/2025")
        page.get_by_placeholder("DR. XXX").fill(name)
        page.get_by_role("button", name="Submit").click()
        
        # Ensure page did not change
        expect(page).to_have_title(re.compile("Prescription Creation"))
        
        browser.close()


def test_fail_prescription_wrongDIN():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the home page and make sure it comes up.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        
        # Navigate to a prescription creation page.
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))
        page.get_by_role("button", name="JAINE FALL").click()
        expect(page).to_have_title(re.compile("Client Page"))
        page.get_by_role("button", name="Create Prescription").click()
        expect(page).to_have_title(re.compile("Prescription Creation"))

        # Randomize Doctor name
        name = "Dr. " + str(random.randint(0,999999999))

        # Fill in input and submit
        page.get_by_label("DIN").fill("923948939248923489")
        page.get_by_label("refill").fill("01/01/2025")
        page.get_by_placeholder("DR. XXX").fill(name)
        page.get_by_role("button", name="Submit").click()
        
        # Ensure page did not change
        expect(page).to_have_title(re.compile("Prescription Creation"))
        
        browser.close()