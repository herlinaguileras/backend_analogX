"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.core.database
Descripción: Configuración del motor de base de datos SQLite y sesiones con SQLModel.
"""

import os
from pathlib import Path
from typing import Generator
from sqlmodel import Session, SQLModel, create_engine

# Ruta absoluta anclada a la raíz del repositorio backend_analogX
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_DB_PATH = BASE_DIR / "analogx.db"

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_PATH}")

# connect_args={"check_same_thread": False} es requerido para SQLite en FastAPI multihilo
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)


def init_db() -> None:
    """Crea todas las tablas en la base de datos si no existen."""
    SQLModel.metadata.create_all(engine)


def seed_database() -> None:
    """Puebla la base de datos con los registros científicos iniciales."""
    from app.core.seed import seed_database as _seed
    _seed()


def get_session() -> Generator[Session, None, None]:
    """Generador de sesión de base de datos para inyección de dependencias en FastAPI."""
    with Session(engine) as session:
        yield session
