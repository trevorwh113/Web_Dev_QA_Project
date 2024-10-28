"""
Temporary script to figure out how to write to the database.
"""
from database import get_database

# Get the database using the method we defined in pymongo_test_insert file
dbname = get_database()
client_collection = dbname["clients"]
drug_collection = dbname["drugs"]

# Add some itmes to the clients database
ap_1 = [["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1],
        ["Green Slime", 654328, "2024-10-19", "Dr. John Smith", 2],
        ["Drug Slime", 895632, "2024-10-20", "Dr. John Smith", 3],
        ["Blue Slime", 889654, "2024-10-21", "Dr. John Smith", 4],
        ["Purple Slime", 552664, "2024-10-22", "Dr. John Smith", 1]]
op_1 = [["old Slime", 552664, "2024-10-22", "Dr. John Smith", 5]]
client_1 = { 
    "phone_number": "(123)-456-7890",
    "first_name": "John",
    "last_name": "Doe",
    "dob": "28/09/2004",
    "active_pres": ap_1,
    "old_pres": op_1
} 

ap_2 = [["Drug Name", 904954, "2024-10-18", "Dr. John Smith", 1],
        ["Green Slime", 654328, "2024-10-19", "Dr. John Smith", 2],
        ["Drug Slime", 895632, "2024-10-20", "Dr. John Smith", 3],
        ["Blue Slime", 889654, "2024-10-21", "Dr. John Smith", 4]]
op_2 = [["Purple Slime", 552664, "2024-10-22", "Dr. John Smith", 1],
        ["old Slime", 552664, "2024-10-22", "Dr. John Smith", 5]]
client_2 = { 
    "phone_number": "(444)-656-6565",
    "first_name": "Piper",
    "last_name": "Mario",
    "dob": "17/04/1990",
    "active_pres": ap_2,
    "old_pres": op_2
} 

# Add one item to the drug database
drug_1 = {
    "drug_name": "Paracetamol",
    "din": 605699,
    "usage": "Used to sooth pain in the funny bone.",
    "dosage": "1 ingested orally daily",
    "quantity": 0
}

client_collection.insert_many([client_1,client_2])
drug_collection.insert_one(drug_1)