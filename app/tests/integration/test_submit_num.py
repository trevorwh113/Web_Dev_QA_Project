"""
This file contains an integration test for the prescription create
feature, and if its results show up on the client search page.
"""
from app import app
import pytest
import random
from database import get_database

# Success cases ---------------------------------------------
def test_submit_and_search():
    """
    Success case: Tests that a prescription submission increases the number of
    active prescriptions on the client search page.
    """

    # Get number of prescriptions
    phone_num = '(444)-656-6565'
    dbname = get_database()    
    client = dbname["clients"].find_one({"phone_number": phone_num})
    num = len(client["active_pres"])

    # Search for client and confirm prescription number
    response = app.test_client().post('/clients', data={"search_par": "(444)-656-6565"})
    assert b"(444)-656-6565" in response.data, "Did not load a client entry correctly" # Ensure data is loaded in 
    assert bytes(str(num), 'utf-8') in response.data, "Number was initially not correct"

    # Create a distinct new prescription.
    target = f"Dr. {random.randint(0,1000000)}"
    data = {"DIN": "445544", "preBy": target, "refill": "01/01/2025"}

    # Submit the prescription to the client
    response = app.test_client().post('/clients/(444)-656-6565/create', data=data)
    assert response.status_code == 200

    # Search for client and make sure prescription number has increased
    num += 1
    response = app.test_client().post('/clients', data={"search_par": "(444)-656-6565"})
    assert bytes(str(num), 'utf-8') in response.data, "Did not change prescription number"
    