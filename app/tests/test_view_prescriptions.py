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
    # Check some of the data to ensure it is properly loaded in.
    assert b"URANIUM-235" in response.data, "Did not load page correctly"
    assert b"Dr. Sherman Sheep" in response.data, "Did not load page correctly"
    assert b"LISDEXAMFETAMINE" in response.data, "Did not load page correctly"
    assert b"Dr. Black Sheep" in response.data, "Did not load page correctly"
    assert b"PARACETAMOL" in response.data, "Did not load page correctly"
    assert b"Dr. Two Sheep" in response.data, "Did not load page correctly"

