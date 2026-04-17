from pydantic import BaseModel, Field

class KelasCreate(BaseModel):
    nama_kelas: str = Field(..., min_length=3, max_length=100)
    jadwal: str = Field(..., min_length=3)
    kapasitas: int = Field(..., gt=0)
    instruktur_id: int

class KelasUpdate(BaseModel):
    nama_kelas: str | None = Field(None, min_length=3, max_length=100)
    jadwal: str | None = None
    kapasitas: int | None = Field(None, gt=0)

class KelasResponse(BaseModel):
    id: int
    nama_kelas: str
    jadwal: str
    kapasitas: int
    instruktur_id: int

    class Config:
        from_attributes = True