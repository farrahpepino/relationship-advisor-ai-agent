from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

try:
    client.admin.command('ismaster')
    print("MongoDB connected successfully!")
except Exception as e:
    print("Error connecting to MongoDB:", e)

db_name = os.getenv("DB_NAME")
db = client[db_name]

conversations_col = db["conversations"]
messages_col = db["messages"]

# indexes
conversations_col.create_index("user_id")
messages_col.create_index([("conversation_id", 1), ("_id", -1)])