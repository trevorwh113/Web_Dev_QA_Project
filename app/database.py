"""
Provides the connection to the PyMongo Database. Meant to be imported
by other files which must communicate with the database.
"""
from pymongo import MongoClient

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://trevorwh113:busJB0wm2CG7vEgd@group-8-fs.rxzle.mongodb.net/?retryWrites=true&w=majority&appName=Group-8-FS"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['medicine_mgmt_data']
