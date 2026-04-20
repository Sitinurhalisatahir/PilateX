from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.member import Member
from schemas.member import MemberCreate, MemberUpdate, MemberResponse
from auth.auth import get_current_user
from models.user import User
from typing import List

router = APIRouter(prefix="/members", tags=["Member"])

# GET semua member (protected)
@router.get("/", response_model=List[MemberResponse], status_code=200)
def get_all_members(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Member).all()

# GET member by ID (protected)
@router.get("/{member_id}", response_model=MemberResponse, status_code=200)
def get_member(
    member_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member tidak ditemukan")
    return member

# POST tambah member baru (protected)
@router.post("/", response_model=MemberResponse, status_code=201)
def create_member(
    data: MemberCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = db.query(Member).filter(Member.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email member sudah terdaftar")

    member = Member(**data.model_dump())
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

# PUT update member (protected)
@router.put("/{member_id}", response_model=MemberResponse, status_code=200)
def update_member(
    member_id: int,
    data: MemberUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member tidak ditemukan")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(member, key, value)

    db.commit()
    db.refresh(member)
    return member

# DELETE member (protected)
@router.delete("/{member_id}", status_code=200)
def delete_member(
    member_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member tidak ditemukan")
    db.delete(member)
    db.commit()
    return {"message": f"Member '{member.nama}' berhasil dihapus"}