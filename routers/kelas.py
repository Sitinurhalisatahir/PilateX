from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.kelas import Kelas
from schemas.kelas import KelasCreate, KelasUpdate, KelasResponse
from auth.auth import get_current_user
from models.user import User
from typing import List

router = APIRouter(prefix="/kelas", tags=["Kelas"])

# GET semua kelas (public)
@router.get("/", response_model=List[KelasResponse], status_code=200)
def get_all_kelas(db: Session = Depends(get_db)):
    return db.query(Kelas).all()

# GET kelas by ID (public)
@router.get("/{kelas_id}", response_model=KelasResponse, status_code=200)
def get_kelas(kelas_id: int, db: Session = Depends(get_db)):
    kelas = db.query(Kelas).filter(Kelas.id == kelas_id).first()
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")
    return kelas

# POST buat kelas baru (protected)
@router.post("/", response_model=KelasResponse, status_code=201)
def create_kelas(
    data: KelasCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    kelas = Kelas(**data.model_dump())
    db.add(kelas)
    db.commit()
    db.refresh(kelas)
    return kelas

# PUT update kelas (protected)
@router.put("/{kelas_id}", response_model=KelasResponse, status_code=200)
def update_kelas(
    kelas_id: int,
    data: KelasUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    kelas = db.query(Kelas).filter(Kelas.id == kelas_id).first()
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(kelas, key, value)

    db.commit()
    db.refresh(kelas)
    return kelas

# DELETE kelas (protected)
@router.delete("/{kelas_id}", status_code=200)
def delete_kelas(
    kelas_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    kelas = db.query(Kelas).filter(Kelas.id == kelas_id).first()
    if not kelas:
        raise HTTPException(status_code=404, detail="Kelas tidak ditemukan")
    db.delete(kelas)
    db.commit()
    return {"message": f"Kelas '{kelas.nama_kelas}' berhasil dihapus"}