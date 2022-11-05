import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv('MONGO_URI')
#print(uri)

client = MongoClient(uri)
db = client.BOOKS
books_db = db.BOOKS_DB
transaction_db = db.TRANSACTIONS_DB

print(books_db.count_documents({}))