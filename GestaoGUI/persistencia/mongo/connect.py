from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


def make_connection():
    uri = "mongodb+srv://msalcmd:"+os.environ['MONGODB_PASSWORD']+"@aluguelcarros.mqebr34.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        #print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(e)
        return False
