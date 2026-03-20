from openai import OpenAI
from dotenv import load_dotenv
import os
from uuid import uuid4
from fastapi import HTTPException

from app.repositories.message_repository import Message_Repository
from app.repositories.conversation_repository import Conversation_Repository
from app.models.message import Message

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Chat_Service:
    def __init__(self):
        self.message_repository = Message_Repository()
        self.conversation_repository = Conversation_Repository() 
    
    def create_conversation(self, db, user_id):
        return self.conversation_repository.create(db, user_id)

    def get_conversation(self, db, conversation_id):
        return self.conversation_repository.get_conversation(db, conversation_id)

    def get_conversations(self, db, user_id):
        return self.conversation_repository.get_conversations(db, user_id)

    def get_messages(self, db, conversation_id):
        return self.message_repository.get_messages(db, conversation_id)

    def send_message(self, db, user_id, conversation_id, input):
        conversation = self.conversation_repository.get_conversation(db, conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        
        if conversation.user_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized")


        messages = self.message_repository.get_messages(db, conversation_id)
        
        history = [
            {"role": m.role, "content": m.content}
            for m in messages
        ]
        
        history.append({"role": "user", "content":input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=history
            )
            reply = response.choices[0].message.content or ""
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="AI failed")
        
        self.message_repository.create(db, Message(
            id=str(uuid4()),
            conversation_id=conversation_id,
            role="user",
            content=input
        ))

        self.message_repository.create(db, Message(
            id=str(uuid4()),
            conversation_id=conversation_id,
            role="assistant",
            content=reply
        ))
        
        if len(messages) >= 4:
            self.generate_title(db, conversation_id)

        return reply

    def generate_title(self, db, conversation_id):
        messages = self.message_repository.get_messages(db, conversation_id)

        conversation_text = "\n".join([m.content for m in messages])

        response = client.responses.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Generate a short title (max 6 words) for a relationship advice conversation."
                },
                {
                    "role": "user",
                    "content": conversation_text
                }
            ]
        )

        title = response.choices[0].message.content

        self.conversation_repository.update_title(db, conversation_id, title)

        return title