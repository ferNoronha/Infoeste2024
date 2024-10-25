from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_router
from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite que o React no localhost acesse a API
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers (Content-Type, Authorization, etc.)
)
app.include_router(api_router)