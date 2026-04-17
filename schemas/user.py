from pydantic import BaseModel, EmailStr

# Schema untuk register
class UserCreate(BaseModel):
    nama: str
    email: EmailStr
    password: str

# Schema untuk response (tanpa password)
class UserResponse(BaseModel):
    id: int
    nama: str
    email: str

    class Config:
        from_attributes = True

# Schema untuk login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema untuk token JWT
class Token(BaseModel):
    access_token: str
    token_type: str