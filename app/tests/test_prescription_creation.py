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
    valid DIN is entered. Also makes sure database is updated accordingly (POST).
    Note that this test should result in a client "JOHN DOE" getting a new
    prescription. This client exists solely for testing purposes.
    """
    # Create a distinct new prescription.
    target = f"Dr. {random.randint(0,1000000)}"
    data = {"DIN": "445544", "preBy": target, "interval": "01/01/2025"}

    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data=data)
    assert response.status_code == 200
    assert b"Client Page" in response.data, "Did not load client page correctly"
    assert bytes(target, 'utf-8') in response.data, "Did not load new prescription correctly"

    # Check that the prescription was added to the database.
    dbname = database.get_database()    
    client = dbname["clients"].find_one({"phone_number": "(123)-456-7890"})
    client_actives = client["active_pres"]
    found = False
    for pres in client_actives:
        if target in pres:
            found = True
            break
    assert found, "Did not update database correctly with new prescription"

# Failure cases for /clients/(123)-456-7890/create route ------------------------------
def test_submit_with_invalid_din():
    """
    Failure case: Tests that a submission remains on the prescription creation
    page when given an invalid DIN (not an integer). Also ensures database is
    not updated (POST).
    """
    # Create an invalid test prescription.
    data = {"DIN": "", "preBy": "NOT A DOCTOR", "interval": "01/01/2025"}

    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data=data)
    assert response.status_code == 200
    assert b"Prescription Creation" in response.data, "Did not reload prescription creation page correctly"

    # Check that the prescription was NOT added to the database.
    dbname = database.get_database()    
    client = dbname["clients"].find_one({"phone_number": "(123)-456-7890"})
    client_actives = client["active_pres"]
    not_found = True
    for pres in client_actives:
        if "NOT A DOCTOR" in pres:
            not_found = False
            break
    assert not_found, "Wrongly updated the database with new prescription"

def test_submit_with_inexistant_din():
    """
    Failure case: Tests that a submission remains on the prescription creation
    page when given an inexsitent DIN (not in the drug database). Also ensures 
    the client database is not updated (POST).
    """
    # Create a test prescription with inexistent din.
    data = {"DIN": "000000000", "preBy": "NOT A DRUG", "interval": "01/01/2025"}

    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data=data)
    assert response.status_code == 200
    assert b"Prescription Creation" in response.data, "Did not reload prescription creation page correctly"

    # Check that the prescription was NOT added to the database.
    dbname = database.get_database()    
    client = dbname["clients"].find_one({"phone_number": "(123)-456-7890"})
    client_actives = client["active_pres"]
    not_found = True
    for pres in client_actives:
        if "NOT A DRUG" in pres:
            not_found = False
            break
    assert not_found, "Wrongly updated the database with new prescription"
