"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.main
Descripción: Punto de entrada principal de la aplicación FastAPI para el backend de AnalogX.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.database import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ciclo de vida de la aplicación: asegura la inicialización y persistencia de SQLite."""
    try:
        seed_database()
    except Exception as e:
        print(f"Aviso en ciclo de vida BD: {e}")
    yield



@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ciclo de vida de la aplicación: asegura la inicialización y persistencia de SQLite."""
    try:
        seed_database()
    except Exception as e:
        print(f"Aviso en ciclo de vida BD: {e}")
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# Configuración de CORS para interactuar de forma segura con frontend_analogX
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusión del router modular v1 y alias /api
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(api_router, prefix="/api")


@app.get("/", tags=["Estado y Diagnóstico"])
def root():
    """
    Endpoint raíz de comprobación de estado y bienvenida al motor AnalogX.
    """
    return {
        "status": "online",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "docs_url": "/docs",
        "api_v1_base": settings.API_V1_STR,
        "notice": "Fase 0 activa: Auditoría científica, modelado de datos y esquemas Pydantic completos.",
    }


@app.get("/health", tags=["Estado y Diagnóstico"])
def health_check():
    """
    Comprobación de salud básica para orquestación y desarrollo local en VS Code / Docker.
    """
    return {
        "status": "healthy",
        "service": "analogx-backend",
        "version": settings.VERSION,
        "phase": 0,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

