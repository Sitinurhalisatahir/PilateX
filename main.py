from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from database import Base, engine
from routers import auth, kelas, member
import traceback

Base.metadata.create_all(bind=engine)

security = HTTPBearer()

app = FastAPI(
    title="Pilatex API",
    description="Sistem Manajemen Kelas Pilates & Member",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "traceback": traceback.format_exc()}
    )

app.include_router(auth.router)
app.include_router(kelas.router)
app.include_router(member.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Selamat datang di Pilatex API 🧘"}