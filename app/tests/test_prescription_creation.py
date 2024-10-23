"""
This file contains functional tests for the prescription create
feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest


def test_load_clients_create_page():
    """
    Success case: Tests that the clients precription creation page is loaded with (GET).
    """
    # Load the create page (GET)
    response = app.test_client().get('/clients/(123)-456-7890/create')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Drug Name:" in response.data, "Did not load prescription create page correctly"
    assert b"Prescription Creation" in response.data, "Did not load page correctly"

def test_submit_clients_create_page():
    """
    Success case: Tests that a submission redirects to the client page (POST).
    """
    # Submit the create page with arguments (POST)
    response = app.test_client().post('/clients/(123)-456-7890/create', data={"dname": "","DIN": "","dosage": "","preBy": "","interval": ""})
    assert response.status_code == 200
    assert b"Client Page" in response.data, "Did not load client page correctly"