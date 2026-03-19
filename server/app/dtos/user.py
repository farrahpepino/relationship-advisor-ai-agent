from pydantic import BaseModel

class User_Dto(BaseModel):
    email: str
    name: str
    
    class Config:
        from_attributes = True
        
        
    
    
    