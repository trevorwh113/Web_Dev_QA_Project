"""
Provides utility functions, such as those to access
the backend database and those to manipulate data.
"""

def get_all_inv():
    """
    Returns a list of all the inventory elements stored 
    in the database. Return list has format:
    [[drug_name, din, usage, dosage, quantity], ...]
    [[str,       int, str,   str,    int],      ...]
    """
    
    # Mocks this functionality for now.
    inv_data = [
        ["Drug Name", 904954, "Used to reduce inflamation of the sinuses which causes sneezing and runny noses.", 
        "1 spray daily in each nostril", 10], 
        
        ["Paracetamol", 605699, "Used to sooth pain in the funny bone.", 
        "1 ingested orally daily", 0], 
       
        ["Lisdexamfetamine", 565232, "Used to increase focus and quell hunger.", 
        "1 ingested orally in the morning", 452], 
       
        ["Uranium-235", 445544, "Used to inflict a lethal dose of ionizing radiation.", 
        "Rub over chest for 15 minutes daily", 3], 
       
        ["Green Slime", 999999, "Found under office sink, may hydrate skin?", 
        "Apply topically to dry area", 47]
    ]

    return inv_data

def get_all_clients():
    """
    Returns a list of all the clients stored in the database. 
    Return list has format:
    [[full_name, birth_date, phone_number, active_prescriptions], ...]
    [[str,       str,        str,          int],                  ...]
    """
    
    # Mocks this functionality for now.
    client_data = [
        ["John Doe", "28/09/2004", "(123)-456-7890", 3], 
        ["Jaine Fall", "8/02/2000", "(613)-999-7777", 10], 
        ["Piper Mario", "17/04/1990", "(444)-656-6565", 1], 
        ["Car Binky", "10/10/2020", "(444)-224-2345", 2], 
        ["Helio Ptile", "8/02/2000", "(123)-767-5456", 4], 
        ["Cotton Candy", "22/12/2012", "(232)-456-7890", 0], 
        ["Last One", "14/12/3000", "(777)-666-55555", 13]
    ]

    return client_data

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


def valid_string(string):
    """Checks that the input is can be cast to a non-empty string."""
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
