from pydantic import BaseModel

class Item(BaseModel):
    name : str
    status : str

class UserBase(BaseModel):
    name : str
    score : int
class UserCreate(UserBase):
    pass
class User(UserBase):
    class Config:
        orm_mode = True