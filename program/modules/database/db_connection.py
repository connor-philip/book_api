# import config
from pymongo import MongoClient
from os import environ

databaseIP = environ['databaseIP']
client = MongoClient("mongodb://" + databaseIP)
db = client.bookdb
