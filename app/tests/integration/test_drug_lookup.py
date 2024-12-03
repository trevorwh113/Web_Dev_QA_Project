"""
This file contains additional unit tests for the drug_lookup
feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest

# Success cases for /inventory route ------------------------------
def test_load_inventory_search_page():
    """
    Success case: Tests that the inventory page is loaded with
    all five entries (GET).
    """
    # Load the search page without any search arguments (GET)
    response = app.test_client().get('/inventory')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Search Inventory" in response.data, "Did not load inventory page correctly"
    # Make sure the data has been correctly loaded in.
    assert b"904954" in response.data, "Did not load a drug entry correctly"
    assert b"605699" in response.data, "Did not load a drug entry correctly"
    assert b"565232" in response.data, "Did not load a drug entry correctly"
    assert b"445544" in response.data, "Did not load a drug entry correctly"
    assert b"999999" in response.data, "Did not load a drug entry correctly"

def test_search_inventory_by_name():
    """
    Success case: Tests that a search loads the page with only the the 
    entries matching the search parameter - drug_name (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/inventory', data={"search_par": "am"})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    assert b"904954" in response.data, "Did not load a drug entry correctly"
    assert b"605699" in response.data, "Did not load a drug entry correctly"
    assert b"565232" in response.data, "Did not load a drug entry correctly"
    assert b"445544" not in response.data, "Mistakenly loaded a drug entry"
    assert b"999999" not in response.data, "Mistakenly loaded a drug entry"

def test_search_inventory_by_din():
    """
    Success case: Tests that a search loads the page with only the the 
    entries matching the search parameter - din (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/inventory', data={"search_par": 445544})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    assert b"904954" not in response.data, "Mistakenly loaded a drug entry"
    assert b"605699" not in response.data, "Mistakenly loaded a drug entry"
    assert b"565232" not in response.data, "Mistakenly loaded a drug entry"
    assert b"445544" in response.data, "Did not load a drug entry correctly"
    assert b"999999" not in response.data, "Mistakenly loaded a drug entry"

# Failure cases for /inventory route ------------------------------
def test_search_inventory_invalid():
    """
    Failure case: Tests that a search loads the page with no entries
    given an invalid search parameter (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/inventory', data={"search_par": ""})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    assert b"904954" not in response.data, "Mistakenly loaded a drug entry"
    assert b"605699" not in response.data, "Mistakenly loaded a drug entry"
    assert b"565232" not in response.data, "Mistakenly loaded a drug entry"
    assert b"445544" not in response.data, "Mistakenly loaded a drug entry"
    assert b"999999" not in response.data, "Mistakenly loaded a drug entry"

def test_search_inventory_not_found():
    """
    Failure case: Tests that a search loads the page with no entries
    given a search parameter that is not in the data (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/inventory', data={"search_par": 111111})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    assert b"904954" not in response.data, "Mistakenly loaded a drug entry"
    assert b"605699" not in response.data, "Mistakenly loaded a drug entry"
    assert b"565232" not in response.data, "Mistakenly loaded a drug entry"
    assert b"445544" not in response.data, "Mistakenly loaded a drug entry"
    assert b"999999" not in response.data, "Mistakenly loaded a drug entry"
