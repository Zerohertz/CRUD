from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.crud import router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="🦀 CRUD 🦀")

origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/users", tags=["CRUD"])
