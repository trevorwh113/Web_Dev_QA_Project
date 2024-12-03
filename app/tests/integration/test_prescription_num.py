"""
This file contains an integration test for the update prescription
feature, and if its results show up on the client search page.
"""
from app import app
import utility, pytest, json

# Success cases ---------------------------------------------
def test_prescription_num_1():
    """
    Success case: Test for removing an active prescription.
    """
    # get client from data base
    client = utility.get_client_by_phone("(444)-656-6565")
    acts = utility.get_active_prescripts(client)
    olds = utility.get_old_prescripts(client)
    
    num = len(acts) # number of active prescriptions
    
    # check that client is actually in client search page
    response1 = app.test_client().post('/clients', data={"search_par": "(444)-656-6565"})
    assert bytes(str(num), 'utf-8') in response1.data, "Active prescription number incorrect"
    assert b"(444)-656-6565" in response1.data, "Did not load a client entry correctly"
    assert response1.status_code == 200 # ensure data is loaded correctly
    
    # update perscriptions
    p = acts.pop()
    p[4] = "5"
    olds.append(p)
    
    num = len(acts) # update number of active prescriptions
    
    # post updated lists to the html/js script that handles it
    response2 = app.test_client().post('/update_list', json={
        'id': "(444)-656-6565",
        'active': acts, 
        'old': olds
    }, )
    
    assert response2.status_code == 200
            
    # check that client is STILL in client search page
    response3 = app.test_client().post('/clients', data={"search_par": "(444)-656-6565"})
    assert response3.status_code == 200
    assert b"(444)-656-6565" in response3.data, "Did not load a client entry correctly"
    #check that number of active prescriptions is in response data
    assert bytes(str(num), 'utf-8') in response3.data, "Did not change prescription number"
    
def test_prescription_num_2():
    """Success case: Test for adding an active prescription (from the history list)."""
    # get client from data base
    client = utility.get_client_by_phone("(444)-656-6565")
    acts = utility.get_active_prescripts(client)
    olds = utility.get_old_prescripts(client)
    
    num = len(acts) # number of active prescriptions
    
    # check that client is actually in client search page
    response1 = app.test_client().post('/clients', data={"search_par": "(444)-656-6565"})
    assert b"(444)-656-6565" in response1.data, "Did not load a client entry correctly"
    assert bytes(str(num), 'utf-8') in response1.data, "Active prescription number incorrect"
    assert response1.status_code == 200 # ensure data is loaded correctly
    
    # update perscriptions
    p = olds.pop()
    p[4] = "2"
    acts.append(p)
    num = len(acts)
    
    # post updated lists to the html/js script that handles it
    response2 = app.test_client().post('/update_list', json={
        'id': "(444)-656-6565",
        'active': acts, 
        'old': olds
    }, )
    
    assert response2.status_code == 200
    
    # check that client is STILL in client search page   
    response3 = app.test_client().post('/clients', data={"search_par": "(444)-656-6565"})
    assert response3.status_code == 200
    assert b"(444)-656-6565" in response3.data, "Did not load a client entry correctly"
    #check that number of active prescriptions is in response data
    assert bytes(str(num), 'utf-8') in response3.data, "Did not change prescription number"