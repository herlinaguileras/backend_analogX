"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models.observation
Descripción: Esquemas Pydantic para variables observadas y mediciones científicas cuantitativas/cualitativas.
"""

from typing import Any, Optional, Union
from pydantic import BaseModel, Field
from app.models.dataset import VerificationStatusEnum


class ObservedVariable(BaseModel):
    """
    Definición conceptual de una variable física, morfológica o espectral observada.
    """
    id: str = Field(..., description="Slug identificador de la variable (ej. 'slope_gradient', 'roughness_rms')")
    name: str = Field(..., description="Nombre formal de la variable (ej. 'Gradiente de Pendiente Basal')")
    physical_quantity: str = Field(..., description="Magnitud física (ej. 'Ángulo', 'Longitud', 'Reflectancia')")
    canonical_unit: str = Field(..., description="Unidad canónica en el Sistema Internacional o 'adimensional'")
    description: str = Field(..., description="Definición física y significado geológico del parámetro")
    measurement_scale: str = Field(
        ...,
        description="Escala de observación: 'microscopica', 'submetrica', 'decametrica', 'regional_cuenca'"
    )


class ObservationMeasurement(BaseModel):
    """
    Medición u observación científica individual con estricto registro de auditoría.
    Contiene exactamente los 13 campos obligatorios requeridos por la arquitectura de AnalogX.
    Admite None / Optional en campos pendientes de verificación para evitar datos inventados.
    """
    id: str = Field(
        ...,
        description="1. Identificador único de la medición (ej. 'obs_uyuni_nasadem_slope_01')"
    )
    source_name: str = Field(
        ...,
        description="2. Nombre del repositorio, misión u organismo emisor oficial"
    )
    source_url: str = Field(
        ...,
        description="3. Enlace permanente verificable, DOI o URL de acceso al producto"
    )
    product_id: str = Field(
        ...,
        description="4. Identificador de producto oficial del catálogo (ej. 'NASADEM_HGT.001', 'PSP_003160_1410')"
    )
    acquisition_date: Optional[str] = Field(
        None,
        description="5. Fecha de adquisición o captura en formato ISO 8601 (YYYY-MM-DD) o None si no verificado"
    )
    version: Optional[str] = Field(
        None,
        description="6. Versión del producto o algoritmo de procesamiento"
    )
    unit: str = Field(
        ...,
        description="7. Unidad física de la medición (ej. 'grados', 'metros', 'dB', 'adimensional')"
    )
    spatial_resolution: str = Field(
        ...,
        description="8. Resolución espacial con unidades (ej. '30m', '463m', '0.25m/px')"
    )
    crs_datum: str = Field(
        ...,
        description="9. Sistema de coordenadas y datum vertical específico de la medición"
    )
    processing_method: str = Field(
        ...,
        description="10. Método de cálculo o algoritmo aplicado (ej. 'Filtro Sobel 3x3', 'Banda DCS 8-7-5')"
    )
    value: Optional[Union[float, int, str, dict, list]] = Field(
        None,
        description="11. Valor numérico escalar, categoría o estructura vectorial observada (None si pendiente)"
    )
    quality_uncertainty: Optional[str] = Field(
        None,
        description="12. Margen de incertidumbre, error estándar instrumental o limitaciones documentadas"
    )
    verification_status: VerificationStatusEnum = Field(
        VerificationStatusEnum.pendiente_de_verificar,
        description="13. Nivel de verificación científica: verificado_con_fuente | inferencia_razonable | hipotesis | pendiente_de_verificar"
    )

