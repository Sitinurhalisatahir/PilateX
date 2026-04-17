from pydantic import BaseModel, EmailStr, Field

class MemberCreate(BaseModel):
    nama: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    no_telepon: str = Field(..., min_length=8, max_length=15)
    kelas_id: int

class MemberUpdate(BaseModel):
    nama: str | None = Field(None, min_length=2, max_length=100)
    no_telepon: str | None = Field(None, min_length=8, max_length=15)
    kelas_id: int | None = None

class MemberResponse(BaseModel):
    id: int
    nama: str
    email: str
    no_telepon: str
    kelas_id: int

    class Config:
        from_attributes = True