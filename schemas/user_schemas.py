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

# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Login Response Schema
class LoginResponse(BaseModel):
    message: str
    user: UserResponse
