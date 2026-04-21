# Pilatex API

**Sistem Manajemen Kelas Pilates & Member**

Pilatex adalah RESTful API yang dibangun menggunakan FastAPI untuk mengelola kelas pilates dan member. API ini mendukung autentikasi JWT, operasi CRUD untuk dua entitas utama (Kelas dan Member), serta relasi One-to-Many antar entitas.

---

## Informasi Proyek

| Item | Detail |
|------|--------|
| Nama | Sistem Manajemen Kelas Pilates & Member |
| Framework | FastAPI |
| Bahasa | Python 3.13 |
| Database | SQLite |
| ORM | SQLAlchemy |
| Autentikasi | JWT (JSON Web Token) |

---

## 📁 Struktur Proyek

```
PilateX/
├── main.py          # Entry point FastAPI
├── database.py      # Koneksi & session database
├── models/          # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   ├── kelas.py
│   └── member.py
├── schemas/         # Pydantic schemas
│   ├── __init__.py
│   ├── user.py
│   ├── kelas.py
│   └── member.py
├── routers/         # Endpoint per domain
│   ├── __init__.py
│   ├── auth.py
│   ├── kelas.py
│   └── member.py
├── auth/            # JWT & security logic
│   ├── __init__.py
│   ├── jwt.py
│   └── auth.py
├── requirements.txt # Dependensi Python
└── README.md        # Dokumentasi proyek
```

---
