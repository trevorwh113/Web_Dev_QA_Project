"""
This file contains functional tests for the prescription create
feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest
import random
import database

# Success cases for /clients/(123)-456-7890/create route ------------------------------
def test_load_clients_create_page():
    """
    Success case: Tests that the clients precription creation page is loaded with (GET).
    """
    # Load the create page (GET)
    response = app.test_client().get('/clients/(123)-456-7890/create')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Prescription Creation" in response.data, "Did not load prescription creation page correctly"
    assert b"DIN:" in response.data, "Did not input form correctly"
    assert b"Prescribed By:" in response.data, "Did not input form correctly"
    assert b"Refill Date:" in response.data, "Did not input form correctly"
    assert b"Submit" in response.data, "Did not load submit button correctly"
    assert b"Cancel" in response.data, "Did not load cancel button correctly"

def test_submit_with_valid_data():
    """
    Success case: Tests that a submission redirects to the client page when a
    valid DIN is entered (POST). Note that this test should result in a client 
    "JOHN DOE" getting a new prescription. Does NOT check the database.
    """
    # Create a distinct new prescription.
    target = f"Dr. {random.randint(0,1000000)}"
    data = {"DIN": "445544", "preBy": target, "refill": "01/01/2025"}

    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data=data)
    assert response.status_code == 200
    assert b"Client Page" in response.data, "Did not load client page correctly"
    assert bytes(target, 'utf-8') in response.data, "Did not load new prescription correctly"

# Failure cases for /clients/(123)-456-7890/create route ------------------------------
def test_submit_with_invalid_din():
    """
    Failure case: Tests that a submission remains on the prescription creation
    page when given an invalid DIN (not an integer) (POST). Does NOT check the 
    database.
    """
    # Create an invalid test prescription.
    data = {"DIN": "", "preBy": "NOT A DOCTOR", "refill": "01/01/2025"}

    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data=data)
    assert response.status_code == 200
    assert b"Prescription Creation" in response.data, "Did not reload prescription creation page correctly"

def test_submit_with_inexistant_din():
    """
    Failure case: Tests that a submission remains on the prescription creation
    page when given an inexsitent DIN (not in the drug database) (POST). Does NOT 
    check the database.
    """
    # Create a test prescription with inexistent din.
    data = {"DIN": "000000000", "preBy": "NOT A DRUG", "refill": "01/01/2025"}

    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data=data)
    assert response.status_code == 200
    assert b"Prescription Creation" in response.data, "Did not reload prescription creation page correctly"
