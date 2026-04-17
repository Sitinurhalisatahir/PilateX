from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Lokasi file database SQLite
DATABASE_URL = "sqlite:///./pilatex.db"

# Engine: koneksi utama ke database
# check_same_thread=False khusus untuk SQLite agar bisa dipakai di banyak request
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal: factory untuk membuat sesi database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: kelas induk yang diwarisi semua models
Base = declarative_base()

# Dependency: inject sesi database ke setiap endpoint
# Otomatis ditutup setelah request selesai
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()