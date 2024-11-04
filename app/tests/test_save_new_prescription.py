"""
Tests the ability to save prescriptions in utility.py.
"""
import utility
import random
import pytest
from database import get_database



# Function is always called with a valid phone number and valid drug data
# Is not called if user input doesn't have a valid din
# User input is always an array [int, string, string]

def test_save_new_prescription0():
    phone_num = '(444)-224-2345'
    rando = str(random.randint(1, 999999))
    user_input = [445544, "Dr."+rando, "12/12/1212"]
    utility.save_new_prescription(phone_num, user_input, utility.valid_drug(user_input[0]))

    dbname = get_database()    
    client = dbname["clients"].find_one({"phone_number": phone_num})
    client_actives = client["active_pres"]
    found = False
    for pres in client_actives:
        if user_input[0] in pres and user_input[1] in pres and user_input[2] in pres:
            found = True
            break
    assert found, "Did not update database correctly with new prescription"



def test_save_new_prescription1():
    phone_num = '(444)-224-2345'
    user_input = [445544, "", ""]
    utility.save_new_prescription(phone_num, user_input, utility.valid_drug(user_input[0]))

    dbname = get_database()    
    client = dbname["clients"].find_one({"phone_number": phone_num})
    client_actives = client["active_pres"]
    found = False
    for pres in client_actives:
        if user_input[0] in pres and user_input[1] in pres and user_input[2] in pres:
            found = True
            break
    assert found, "Did not update database correctly with new prescription"