"""
This file contains functional test for the ViewPrescription feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest


def test_load_prescription_page():
    """
    Success case: Tests that the clients precription page is loaded with (GET).
    """
    # Load the prescription page (GET)
    response = app.test_client().get('/clients/(123)-456-7890')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Active Perscriptions" in response.data, "Did not load clients prescription page correctly"
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"Drug Name" in response.data, "Did not load page correctly"
    assert b"Green Slime" in response.data, "Did not load page correctly"
    assert b"Drug Slime" in response.data, "Did not load page correctly"
    assert b"Blue Slime" in response.data, "Did not load page correctly"
    assert b"Purple Slime" in response.data, "Did not load page correctly"
    assert b"old Slime" in response.data, "Did not load page correctly"

