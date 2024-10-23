"""
This file contains additional unit tests for the client_create
feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest

# Success cases for /clients route ------------------------------
def test_load_prescription_page():
    """
    Success case: Tests that the clients precription creation page is loaded with (GET).
    """
    # Load the search page without any search arguments (GET)
    response = app.test_client().get('/clients/(123)-456-7890')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Active Perscriptions" in response.data, "Did not load clients create page correctly"
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"Drug Name" in response.data, "Did not load page correctly"
    assert b"Green Slime" in response.data, "Did not load page correctly"
    assert b"Drug Slime" in response.data, "Did not load page correctly"
    assert b"Blue Slime" in response.data, "Did not load page correctly"
    assert b"Purple Slime" in response.data, "Did not load page correctly"
    assert b"old Slime" in response.data, "Did not load page correctly"

