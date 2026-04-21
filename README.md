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

## Struktur Proyek

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

## Instalasi & Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/[username]/pilatex.git
cd pilatex
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
```

### 3. Aktifkan Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Jalankan Server
```bash
uvicorn main:app --reload
```

### 6. Buka di Browser
| Platform | URL |
|----------|-----|
| Root API | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |

---

## Daftar Endpoint

### Autentikasi
| Method | Endpoint | Deskripsi | Auth |
|--------|----------|-----------|------|
| POST | /auth/register | Daftar user baru | ❌ |
| POST | /auth/login | Login & dapat token JWT | ❌ |

### Kelas
| Method | Endpoint | Deskripsi | Auth |
|--------|----------|-----------|------|
| GET | /kelas/ | Ambil semua kelas | ❌ |
| GET | /kelas/{id} | Ambil kelas by ID | ❌ |
| POST | /kelas/ | Buat kelas baru | ✅ |
| PUT | /kelas/{id} | Update kelas | ✅ |
| DELETE | /kelas/{id} | Hapus kelas | ✅ |

### Member
| Method | Endpoint | Deskripsi | Auth |
|--------|----------|-----------|------|
| GET | /members/ | Ambil semua member | ✅ |
| GET | /members/{id} | Ambil member by ID | ✅ |
| POST | /members/ | Tambah member baru | ✅ |
| PUT | /members/{id} | Update member | ✅ |
| DELETE | /members/{id} | Hapus member | ✅ |

===

## Relasi Database & ERD

### Relasi Antar Entitas
Terdapat 2 relasi One-to-Many dalam project ini:

- **User → Kelas** : 1 instruktur dapat memiliki banyak kelas
- **Kelas → Member** : 1 kelas dapat memiliki banyak member

### ERD (Entity Relationship Diagram)
users (1) ──────< kelas (Many)
│
└──────< members (Many)

### Penjelasan Relasi

- **users → kelas** : 1 instruktur dapat memiliki banyak kelas (One-to-Many)
- **kelas → members** : 1 kelas dapat memiliki banyak member (One-to-Many)

### Penjelasan Tabel

**Tabel users**
| Kolom | Tipe | Keterangan |
|-------|------|------------|
| id | Integer | Primary Key |
| nama | String | Nama instruktur |
| email | String | Email unik |
| hashed_password | String | Password terenkripsi |

**Tabel kelas**
| Kolom | Tipe | Keterangan |
|-------|------|------------|
| id | Integer | Primary Key |
| nama_kelas | String | Nama kelas pilates |
| jadwal | String | Jadwal kelas |
| kapasitas | Integer | Kapasitas peserta |
| instruktur_id | Integer | Foreign Key → users.id |

**Tabel members**
| Kolom | Tipe | Keterangan |
|-------|------|------------|
| id | Integer | Primary Key |
| nama | String | Nama member |
| email | String | Email unik |
| no_telepon | String | Nomor telepon |
| kelas_id | Integer | Foreign Key → kelas.id |

===

## Cara Autentikasi di Swagger UI

### 1. Register
- Buka `http://127.0.0.1:8000/docs`
- Cari endpoint `POST /auth/register`
- Klik **Try it out**
- Isi request body:
```json
{
    "nama": "Nama Kamu",
    "email": "email@gmail.com",
    "password": "password123"
}
```
- Klik **Execute**

### 2. Login & Dapat Token
- Cari endpoint `POST /auth/login`
- Klik **Try it out**
- Isi request body:
```json
{
    "email": "email@gmail.com",
    "password": "password123"
}
```
- Klik **Execute**
- Copy `access_token` dari response

### 3. Masukkan Token
- Klik tombol **Authorize** 🔒 di pojok kanan atas
- Isi kolom **Value** dengan token
- Klik **Authorize** → **Close**

### 4. Akses Endpoint Terproteksi
- Sekarang semua endpoint yang membutuhkan token sudah bisa diakses
- Tandanya gembok 🔒 akan **tertutup**
