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

# Drug Search ---------------------------------------------
def test_drug_search_by_name():
    """
    Searches for a few drugs in the inventory pages by actually 
    using the web page interface with a name or partial name.
    """    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Naviguate to the inventory search page.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        page.get_by_role("button", name="Search Inventory").click()
        expect(page).to_have_title(re.compile("Search Inventory"))

        # 1. Failure Case: Search by Invalid Drug Name
        page.get_by_placeholder("Drug Name or DIN...").fill("NOT REAL")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Drug Name:").all()
        assert len(all_found) == 0, "Mistakenly found a hit"

        # 2. Success Case: Search by Full Drug Name (1 hit)
        page.get_by_placeholder("Drug Name or DIN...").fill("malarone")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Drug Name:").all()
        assert len(all_found) == 1, "Found more or less than 1 hit"
        expect(all_found[0]).to_contain_text(re.compile("MALARONE"))

        # 3. Success Case: Search by Partial Drug Name (many hits)
        page.get_by_placeholder("Drug Name or DIN...").fill("dr")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Drug Name:").all()
        assert len(all_found) == 3, "Found more or less than 3 hits"
        expect(all_found[0]).to_contain_text(re.compile("DRUG NAME"))
        expect(all_found[1]).to_contain_text(re.compile("DRUG SLIME"))
        expect(all_found[2]).to_contain_text(re.compile("MIEBO EYE DROPS"))

        browser.close()

def test_drug_search_by_din():
    """
    Searches for a few drugs in the inventory pages by actually 
    using the web page interface with a din.
    """    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Naviguate to the inventory search page.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        page.get_by_role("button", name="Search Inventory").click()
        expect(page).to_have_title(re.compile("Search Inventory"))

        # 1. Failure Case: Search by Invalid DIN
        page.get_by_placeholder("Drug Name or DIN...").fill("000000")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Drug Name:").all()
        assert len(all_found) == 0, "Mistakenly found a hit"

        # 2. Success Case: Search by Valid DIN
        page.get_by_placeholder("Drug Name or DIN...").fill("605699")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Drug Name:").all()
        assert len(all_found) == 1, "Found more or less than 1 hit"
        expect(all_found[0]).to_contain_text(re.compile("PARACETAMOL"))

        browser.close()

# Client Search ---------------------------------------------
def test_client_search_by_name():
    """
    Searches for a few clients in the client pages by actually 
    using the web page interface with a name or partial name.
    """    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Naviguate to the client search page.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))

        # 1. Failure Case: Search by Invalid Client Name
        page.get_by_placeholder("Name or Phone Number...").fill("NO ONE")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Client Name:").all()
        assert len(all_found) == 0, "Mistakenly found a hit"

        # 2. Success Case: Search by Full Client Name (1 hit)
        page.get_by_placeholder("Name or Phone Number...").fill("car BINKY")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Client Name:").all()
        assert len(all_found) == 1, "Found more or less than 1 hit"
        expect(all_found[0]).to_contain_text(re.compile("CAR BINKY"))

        # 3. Success Case: Search by Partial Client Name (many hits)
        page.get_by_placeholder("Name or Phone Number...").fill("newman")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Client Name:").all()
        assert len(all_found) == 3, "Found more or less than 3 hits"
        expect(all_found[0]).to_contain_text(re.compile("PERCY NEWMAN"))
        expect(all_found[1]).to_contain_text(re.compile("HELENE NEWMAN"))
        expect(all_found[2]).to_contain_text(re.compile("SAMANTHA NEWMAN"))

        browser.close()

def test_client_search_by_phone():
    """
    Searches for a few clients in the client pages by actually 
    using the web page interface with a phone-number.
    """    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Naviguate to the client search page.
        page.goto(URL)
        expect(page).to_have_title(re.compile("Home"))
        page.get_by_role("button", name="Manage Client Prescriptions").click()
        expect(page).to_have_title(re.compile("Manage Client Prescriptions"))

        # 1. Failure Case: Search by Invalid Phone Number
        page.get_by_placeholder("Name or Phone Number...").fill("(000)-000-0000")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Client Name:").all()
        assert len(all_found) == 0, "Mistakenly found a hit"

        # 2. Success Case: Search by Valid Phone Number
        page.get_by_placeholder("Name or Phone Number...").fill("(111)-111-2222")
        page.get_by_test_id("submit").click()
        all_found = page.get_by_role("button", name="Client Name:").all()
        assert len(all_found) == 1, "Found more or less than 1 hit"
        expect(all_found[0]).to_contain_text(re.compile("EGG MAN"))

        browser.close()
