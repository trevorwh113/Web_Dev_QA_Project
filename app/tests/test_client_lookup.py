"""
This file contains additional unit tests for the client_lookup
feature, from a front-end perspective (the flask routes).
"""
from app import app
import pytest

# Success cases for /clients route ------------------------------
def test_load_clients_search_page():
    """
    Success case: Tests that the clients search page is loaded with
    all its entries (GET).
    """
    # Load the search page without any search arguments (GET)
    response = app.test_client().get('/clients')
    # Make sure correct page comes up.
    assert response.status_code == 200
    assert b"Client Lookup" in response.data, "Did not load clients search page correctly"
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"(123)-456-7890" in response.data, "Did not load a client entry correctly"
    assert b"(613)-999-7777" in response.data, "Did not load a client entry correctly"
    assert b"(444)-656-6565" in response.data, "Did not load a client entry correctly"
    assert b"(444)-224-2345" in response.data, "Did not load a client entry correctly"
    assert b"(123)-767-5456" in response.data, "Did not load a client entry correctly"
    assert b"(232)-456-7890" in response.data, "Did not load a client entry correctly"
    assert b"(777)-666-55555" in response.data, "Did not load a client entry correctly"

def test_search_client_by_name():
    """
    Success case: Tests that a search loads the page with only the the 
    entries matching the search parameter - client_name (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/clients', data={"search_par": "j"})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"(123)-456-7890" in response.data, "Did not load a client entry correctly"
    assert b"(613)-999-7777" in response.data, "Did not load a client entry correctly"
    assert b"(444)-656-6565" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-224-2345" not in response.data, "Mistakenly loaded a client entry"
    assert b"(123)-767-5456" not in response.data, "Mistakenly loaded a client entry"
    assert b"(232)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(777)-666-55555" not in response.data, "Mistakenly loaded a client entry"

def test_search_client_by_phone():
    """
    Success case: Tests that a search loads the page with only the the 
    entries matching the search parameter - phone_number (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/clients', data={"search_par": "(777)-666-55555"})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"(123)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(613)-999-7777" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-656-6565" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-224-2345" not in response.data, "Mistakenly loaded a client entry"
    assert b"(123)-767-5456" not in response.data, "Mistakenly loaded a client entry"
    assert b"(232)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(777)-666-5555" in response.data, "Did not load a client entry correctly"

# Failure cases for /clients route ------------------------------
def test_search_client_invalid():
    """
    Failure case: Tests that a search loads the page with no entries
    given an invalid search parameter (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/clients', data={"search_par": ""})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"(123)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(613)-999-7777" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-656-6565" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-224-2345" not in response.data, "Mistakenly loaded a client entry"
    assert b"(123)-767-5456" not in response.data, "Mistakenly loaded a client entry"
    assert b"(232)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(777)-666-55555" not in response.data, "Mistakenly loaded a client entry"

def test_search_client_not_found():
    """
    Failure case: Tests that a search loads the page with no entries
    given a search parameter that is not in the data (POST).
    """
    # Load the search page with a search argument (POST)
    response = app.test_client().post('/clients', data={"search_par": "Luigi Mario"})
    assert response.status_code == 200
    # Make sure the data has been correctly loaded in.
    # ** May have to change once backend is implemented.
    assert b"(123)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(613)-999-7777" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-656-6565" not in response.data, "Mistakenly loaded a client entry"
    assert b"(444)-224-2345" not in response.data, "Mistakenly loaded a client entry"
    assert b"(123)-767-5456" not in response.data, "Mistakenly loaded a client entry"
    assert b"(232)-456-7890" not in response.data, "Mistakenly loaded a client entry"
    assert b"(777)-666-55555" not in response.data, "Mistakenly loaded a client entry"
