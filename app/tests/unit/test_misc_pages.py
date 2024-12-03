"""
This file contains front-end unit tests for the view of the home page
and two pages which are not included in our selected implemented 
functionality: the supply order page and the drug information view 
page. This test was added to ensure code coverage > 90%.
"""
from app import app
import pytest


def test_load_home_page():
    """
    Success case: Tests that the home page is loaded correctly (GET).
    """
    # Load the home page (GET)
    response = app.test_client().get('/')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Medicine Management System" in response.data, "Did not load home page correctly"
    assert b"Manage Client Prescriptions" in response.data, "Did not load home page correctly"
    assert b"Search Inventory" in response.data, "Did not load home page correctly"
    assert b"Manage Supply Orders" in response.data, "Did not load home page correctly"

def test_load_inv_info_page():
    """
    Success case: Tests that the inventory information page is loaded correctly (GET).
    """
    # Load the inventory information page (GET)
    response = app.test_client().get('/inventory/904954')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Error" in response.data, "Did not load inventory information page correctly"
    assert b"904954" in response.data, "Did not load inventory information page correctly"

def test_load_supply_page():
    """
    Success case: Tests that the supply page is loaded correctly (GET).
    """
    # Load the supply page (GET)
    response = app.test_client().get('/supply')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Error" in response.data, "Did not load supply page correctly"