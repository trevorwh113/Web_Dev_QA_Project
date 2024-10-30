"""
Temporary script to figure out querying the database.
"""
from database import get_database

# Get the database using the method we defined in pymongo_test_insert file
dbname = get_database()
 
# Retrieve a collection named "user_1_items" from database
collection_name = dbname["clients"]
 
item_details = collection_name.find()


for item in item_details:
    for value in item.values():
        print(value)
    # for value in 
    print()