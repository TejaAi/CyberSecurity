
from dotenv import load_dotenv
load_dotenv()
import os

from pymongo.mongo_client import MongoClient

uri =  os.environ["mongodb_url"]

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)