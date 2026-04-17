from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    no_telepon = Column(String, nullable=False)
    kelas_id = Column(Integer, ForeignKey("kelas.id"), nullable=False)

    # Relasi Many-to-One ke Kelas
    kelas = relationship("Kelas", back_populates="members")