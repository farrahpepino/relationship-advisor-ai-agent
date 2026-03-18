from app.database import conversations_col, messages_col
from datetime import datetime
from bson import ObjectId

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    
    if "conversation_id" in doc:
        doc["conversation_id"] = str(doc["conversation_id"])
    
    return doc

def create_conversation(user_id: str, title: str = None):
    conversation = {
        "user_id": user_id,
        "title": title or "New Conversation",
        "last_opened": datetime.now(),
        "status": "active"
    }
    
    result = conversations_col.insert_one(conversation)
    return str(result.inserted_id)

def add_message(role: str, content: str, conversation_id: str):
    message = {
        "role": role,
        "content": content,
        "conversation_id": ObjectId(conversation_id),
        "created_at": datetime.now(),
    }
    
    result = messages_col.insert_one(message)
    update_last_opened(conversation_id)
    # EDIT: update title later
    return str(result.inserted_id)

def get_user_conversations(user_id: str):
    conversations = conversations_col.find({"user_id": user_id}).sort("last_opened", -1)
    return [serialize(c) for c in conversations]
    
def get_messages(conversation_id):
    messages = messages_col.find({"conversation_id": conversation_id}).sort("created_at")
    return list(serialize(m) for m in messages)

def update_last_opened(conversation_id: str):
    conversations_col.update_one(
        {"_id": conversation_id},
        {"$set": {"last_opened": datetime.now()}}
    )
    
# def update_title(conversation_id: str, title: str):
#     conversations_col.update_one(
#         {"_id": conversation_id},
#         {"$set": {}}
#     )
        
