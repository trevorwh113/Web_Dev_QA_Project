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

def filter_inv(inv, drug_name, din):
    """
    Filters a given inventory dataset to only include
    entires containing the drug_name and/or din. Assumes
    din and drug_name as int >= 0 and non-empty string,
    respectively. Expected format for inv and return:
    [[drug_name, din, usage, dosage, quantity], ...]
    [[str,       int, str,   str,    int],      ...]
    """
    new_inv = []

    # Validate search parameters
    if valid_string(drug_name):
        drug_name = str(drug_name)
    else:
        drug_name = ""
    if valid_int(din):
        din = int(din)
    else:
        din = -1

    for entry in inv:
        # Search by name.
        if drug_name != "" and drug_name in entry[0]:
            new_inv.append(entry)
        # Search by din.
        elif din != -1 and din == entry[1]:
            new_inv.append(entry)
    
    return new_inv

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
