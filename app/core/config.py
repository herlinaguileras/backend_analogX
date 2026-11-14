"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.core.config
Descripción: Configuración centralizada del backend para desarrollo y producción.
"""

from typing import List
from pydantic import BaseModel, Field


class Settings(BaseModel):
    """
    Configuraciones del backend de AnalogX.
    Permite configuración vía variables de entorno o valores por defecto controlados.
    """
    PROJECT_NAME: str = "AnalogX — Planetary Analog Discovery Engine"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    DESCRIPTION: str = (
        "Motor de descubrimiento y caracterización de análogos planetarios para NASA Space Apps Challenge 2026. "
        "Permite contrastar depósitos evaporíticos e hidrotermales del Altiplano boliviano con paleocuencas de cloruro en Marte."
    )
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3100",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3100",
        "http://127.0.0.1:5173",
    ]
    DATA_CATALOG_PATH: str = "research/dataset_catalog.csv"
    ENVIRONMENT: str = "development"


settings = Settings()

