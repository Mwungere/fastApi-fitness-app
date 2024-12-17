from pydantic import BaseModel, EmailStr

# Shared Base Schema for User
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Create Schema
class UserCreate(UserBase):
    password: str

# Response Schema
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for Successful Login Response
class LoginResponse(BaseModel):
    message: str
    user: UserResponse