
import utility, pytest
from database import get_database


### TESTS FOR RELATED UTILITY FUNCTIONS ###
def test_get_active_prescripts():
    #from database
    db = get_database()
    collection_name = db["clients"]
    client_raw = collection_name.find_one({"phone_number" : "(444)-656-6565"})
    act_db = client_raw['active_pres']
    
    
    #from functions
    client = utility.get_client_by_phone("(444)-656-6565")
    act = utility.get_active_prescripts(client)
    
    assert act == act_db
    


def test_get_old_prescripts():
    #from database
    db = get_database()
    collection_name = db["clients"]
    client_raw = collection_name.find_one({"phone_number" : "(444)-656-6565"})
    old_db = client_raw['old_pres']
    
    
    #from functions
    client = utility.get_client_by_phone("(444)-656-6565")
    old = utility.get_old_prescripts(client)
    
    assert old == old_db

def test_update_prescriptions_1():
    client = utility.get_client_by_phone("(444)-656-6565")
    acts = utility.get_active_prescripts(client)
    olds = utility.get_old_prescripts(client)
    
    print(acts[0])
    
    acts[-1][4] = "3"
    
    utility.update_prescriptions("(444)-656-6565", acts, olds)
    
    acts_after = utility.get_active_prescripts(client)
    olds_after = utility.get_old_prescripts(client)
    
    assert acts == acts_after
    assert olds == olds_after
    
def test_update_prescriptions_2():
    client = utility.get_client_by_phone("(444)-656-6565")
    acts = utility.get_active_prescripts(client)
    olds = utility.get_old_prescripts(client)
    
    acts[-1][4] = "2"
    
    utility.update_prescriptions("(444)-656-6565", acts, olds)
    
    acts_after = utility.get_active_prescripts(client)
    olds_after = utility.get_old_prescripts(client)
    
    assert acts == acts_after
    assert olds == olds_after

def test_update_prescriptions_3():
    client = utility.get_client_by_phone("(444)-656-6565")
    acts = utility.get_active_prescripts(client)
    olds = utility.get_old_prescripts(client)
    
    p = acts.pop()
    p[4] = "5"
    olds.append(p)
    
    utility.update_prescriptions("(444)-656-6565", acts, olds)
    
    acts_after = utility.get_active_prescripts(client)
    olds_after = utility.get_old_prescripts(client)
    
    assert acts == acts_after
    assert olds == olds_after
    
def test_update_prescriptions_4():
    client = utility.get_client_by_phone("(444)-656-6565")
    acts = utility.get_active_prescripts(client)
    olds = utility.get_old_prescripts(client)
    
    p = olds.pop()
    p[4] = "2"
    acts.append(p)
    
    utility.update_prescriptions("(444)-656-6565", acts, olds)
    
    acts_after = utility.get_active_prescripts(client)
    olds_after = utility.get_old_prescripts(client)
    
    assert acts == acts_after
    assert olds == olds_after