"""
This file contains additional unit tests for the client_create
feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest

# Success cases for /clients route ------------------------------
def test_load_clients_create_page():
    """
    Success case: Tests that the clients precription creation page is loaded with (GET).
    """
    # Load the search page without any search arguments (GET)
    response = app.test_client().get('/clients/(123)-456-7890/create')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Drug Name:" in response.data, "Did not load clients create page correctly"
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"Prescription Creation" in response.data, "Did not load page correctly"

def test_submit_clients_create_page():
    """
    Success case: Tests that a search loads the page with only the the 
    entries matching the search parameter - client_name (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data={"dname": "","DIN": "","dosage": "","preBy": "","interval": ""})
    assert response.status_code == 200
    
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"Client Page" in response.data, "Did not load a client entry correctly"