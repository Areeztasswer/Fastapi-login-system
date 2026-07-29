
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://areez1712_db_user:nVPtC61xpSQXI6y1@cluster1.fsqxslh.mongodb.net/ProductDB?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(MONGO_URI)

db = client["ProductDB"]

product_collection = db["products"]
user_collection = db["users"]
