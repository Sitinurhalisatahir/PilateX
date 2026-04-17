from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(Integer, primary_key=True, index=True)
    nama_kelas = Column(String, nullable=False)
    jadwal = Column(String, nullable=False)
    kapasitas = Column(Integer, nullable=False)
    instruktur_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relasi Many-to-One ke User
    instruktur = relationship("User", back_populates="kelas")

    # Relasi One-to-Many: 1 kelas punya banyak member
    members = relationship("Member", back_populates="kelas")