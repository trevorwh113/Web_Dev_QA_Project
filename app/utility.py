"""
Provides utility functions, such as those to access
the backend database and those to manipulate data.
"""
from enum import Enum
from client import Client

class Status(Enum):
    READY = 1
    NEEDS_FILLING = 2
    NO_RENEWAL = 3
    RENEWAL_AVAIL = 4
    NON_ACTIVE = 5

def get_active_prescripts(client_phone):
    """
    Returns a list of all the perscription info stored 
    in the database. Return list has format:
    [[drug_name, din, next_refill_date, prescribed_by, status], ...]
    [[str,       int, str,              str,           enum - Status],      ...]
    """
    # Mocks this functionality for now.
    clients = get_all_clients()
    for c in clients:
        if c.phone_number == client_phone:
            return c.active_prescripts

def get_all_clients():
    """
    Returns a list of all the clients stored in the database. 
    """
    # *** MOCKING ACTUAL FUNCTION *** #

    #mock perscriptions
    prescripts = [
        ["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1], 
        
        ["Green Slime", 654328, "2024-10-19", "Dr. John Smith", 2],

        ["Drug Slime", 895632, "2024-10-20", "Dr. John Smith", 3], 

        ["Blue Slime", 889654, "2024-10-21", "Dr. John Smith", 4], 

        ["Purple Slime", 552664, "2024-10-22", "Dr. John Smith", 1], 
    ]


    # Creating client objects
    client1 = Client("John", "Doe", "(123)-456-7890", "28/09/2004")
    client1.add_new_prescript(["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1])
    client1.add_new_prescript(["Green Slime", 654328, "2024-10-19", "Dr. John Smith", 2])
    client1.add_new_prescript(["Drug Slime", 895632, "2024-10-20", "Dr. John Smith", 3])
    client1.add_new_prescript(["Blue Slime", 889654, "2024-10-21", "Dr. John Smith", 4])
    client1.add_new_prescript(["Purple Slime", 552664, "2024-10-22", "Dr. John Smith", 1])
    client1.add_old_prescript(["old Slime", 552664, "2024-10-22", "Dr. John Smith", 5])

    client2 = Client("Jaine", "Fall", "(613)-999-7777", "8/02/2000")
    client2.add_new_prescript(["Red Slime", 123456, "2024-10-23", "Dr. Jane Doe", 1])
    

    client3 = Client("Piper", "Mario", "(444)-656-6565", "17/04/1990")
    client3.add_new_prescript("Prescription X")

    client4 = Client("Car", "Binky", "(444)-224-2345", "10/10/2020")
    client4.add_new_prescript("Prescription Y")
    client4.add_new_prescript("Prescription Z")

    client5 = Client("Helio", "Ptile", "(123)-767-5456", "8/02/2000")
    client5.add_new_prescript("Prescription 1")
    client5.add_new_prescript("Prescription 2")
    client5.add_new_prescript("Prescription 3")
    client5.add_new_prescript("Prescription 4")

    client6 = Client("Cotton", "Candy", "(232)-456-7890", "22/12/2012")

    client7 = Client("Last", "One", "(777)-666-5555", "14/12/3000")
    for i in range(13):
        client7.add_new_prescript(f"Prescription {i+1}")

    # List of all clients
    return [client1, client2, client3, client4, client5, client6, client7]



### ***** INVENTORY FUNCTIONS ***** ###
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