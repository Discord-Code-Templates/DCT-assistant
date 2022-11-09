import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv('MONGODB_URI')

client = MongoClient(URI) # Connecting to the database

DB = client["MainDB"] # Getting the database "MainDB"

TEMPLATES = DB["templates"] # Getting the collection "templates"

USERS = DB["users"] # Getting the collection "users" (This is for the site)