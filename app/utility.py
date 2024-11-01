"""
Provides utility functions, such as those to access
the backend database and those to manipulate data.
"""
from database import get_database


### ***** PRESCRIPTION FUNCTIONS ***** ###
def get_active_prescripts(client):
    """
    Returns a list of all the perscription info stored 
    in the database. Return list has format:
    [[drug_name, din, next_refill_date, prescribed_by, status], ...]
    [[str,       int, str,              str,           enum - Status],      ...]
    """  
    return client[4]

def update_prescriptions(c_phone, actives, olds):
    """Updates the prescriptions in the database."""
    db = get_database()

    clients = db["clients"]

    query_filter = {'phone_number' : c_phone}

    update_operation = { 
        '$set' : { 
            'active_pres' : actives,
            'old_pres' : olds
        }
    }

    clients.update_one(query_filter, update_operation)

def get_old_prescripts(client):
    """
    Returns a list of all the old perscription info stored 
    in the database. Return list has format:
    [[drug_name, din, next_refill_date, prescribed_by, status], ...]
    [[str,       int, str,              str,           enum - Status],      ...]
    """  
    return client[5]


### ***** CLIENT FUNCTIONS ***** ###
def get_all_clients():
    """
    Returns a list of all the clients stored in the database. 
    Return list has format:
    [[full_name, birth_date, phone_number, active_prescriptions], ...]
    [[str,       str,        str,          int],                  ...]
    """
    # Retrieve the client inventory from the database.
    dbname = get_database()    
    collection_name = dbname["clients"]
    clients_raw = collection_name.find()
    clients_data = []

    # Convert to the list format used elsewhere.
    for client in clients_raw:
        c_data = [client["first_name"] + " " + client["last_name"],
                  client["dob"],
                  client["phone_number"],
                  len(client["active_pres"])]
        clients_data.append(c_data)
    
    return clients_data

def get_client_by_phone(phone_number):
    """
    Returns more detailed information about a client,
    searching the databased using their phone number. 
    """
    db = get_database()

    clients = db["clients"]

    client_raw = clients.find_one({"phone_number" : phone_number})

    client=list(client_raw.values())[1:]

    return client

def filter_clients(clients, par):
    """
    Filters a given client dataset to only include entires containing 
    the name or phone_number. Assumes both are valid non-empty strings. 
    Expected format for inv and return:
    [[full_name, birth_date, phone_number, active_prescriptions], ...]
    [[str,       str,        str,          int],                  ...]
    """
    new_clients = []
    search_str = ""     # Default 'ignore' value

    # Validate search parameter
    if valid_string(par):
        search_str = str(par)

    # Only search if string is non-empty.
    if search_str != "":
        for entry in clients:
            # Search by name.
            if search_str.lower() in entry[0].lower():
                new_clients.append(entry)
            # Search by phone number.
            elif search_str == entry[2]:
                new_clients.append(entry)
    
    return new_clients

def save_new_prescription(phone_number, pres_data):
    """
    Saves the prescriptiong information to the database
    in the entry for the client with the matchign phone_number.
    """
    # Mock this for now--do nothing.
    pass


### ***** INVENTORY FUNCTIONS ***** ###
def get_all_inv():
    """
    Returns a list of all the inventory elements stored 
    in the database. Return list has format:
    [[drug_name, din, usage, dosage, quantity], ...]
    [[str,       int, str,   str,    int],      ...]
    """
    # Retrieve the drug inventory from the database.
    dbname = get_database()    
    collection_name = dbname["drugs"]
    inv_raw = collection_name.find()
    inv_data = []

    # Convert to the list format used elsewhere.
    for drug in inv_raw:
        drug_data = [drug["drug_name"],
                     drug["din"],
                     drug["usage"],
                     drug["dosage"],
                     drug["quantity"]]
        inv_data.append(drug_data)
    
    return inv_data

def filter_inv(inv, par):
    """
    Filters a given inventory dataset to only include entires containing 
    the drug_name or din. Assumes par is int >= 0 or non-empty string. 
    Expected format for inv and return:
    [[drug_name, din, usage, dosage, quantity], ...]
    [[str,       int, str,   str,    int],      ...]
    """
    new_inv = []
    drug_name = ""  # Default 'ignore' value
    drug_din = -1   # Defualt 'ignore' value

    # Validate search parameter
    if valid_int(par):
        drug_din = int(par)
    elif valid_string(par):
        drug_name = str(par)

    for entry in inv:
        # Search by name.
        if drug_name != "" and drug_name.lower() in entry[0].lower():
            new_inv.append(entry)
        # Search by din.
        elif drug_din != -1 and drug_din == entry[1]:
            new_inv.append(entry)
    
    return new_inv


### ***** MISC FUNCTIONS ***** ###
def valid_string(string):
    """Checks that the input can be cast to a non-empty string."""
    if string == None:
        return False
    else:
        string = str(string).strip()
        if len(string) > 0:
            return True
        else:
            return False

def valid_int(num):
    """Checks that the input can be cast to a non-negative int."""
    if num == None:
        return False
    else:
        try:
            num = int(num)
            if num >= 0:
                return True
            else:
                return False
        except:
            return False

