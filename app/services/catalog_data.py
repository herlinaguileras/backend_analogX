"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.services.catalog_data
Re-exportación desde app.models.catalog_data para compatibilidad.
"""

from app.models.catalog_data import (
    CITATIONS,
    DATASETS,
    EARTH_REGIONS,
    FINDINGS,
    LIMITATIONS,
    OBSERVATIONS,
    PLANETARY_TARGETS,
    SOURCES,
    build_comparison_payload,
)

__all__ = [
    "CITATIONS",
    "DATASETS",
    "EARTH_REGIONS",
    "FINDINGS",
    "LIMITATIONS",
    "OBSERVATIONS",
    "PLANETARY_TARGETS",
    "SOURCES",
    "build_comparison_payload",
]
