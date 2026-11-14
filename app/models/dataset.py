"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models.dataset
Descripción: Esquemas Pydantic para fuentes científicas oficiales y catálogos de datasets.
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl


class AccessTypeEnum(str, Enum):
    """Tipo de acceso y requerimientos de autorización para descarga."""
    publico_sin_login = "publico_sin_login"
    publico_con_registro = "publico_con_registro"
    restringido_aprobacion = "restringido_aprobacion"
    privado = "privado"


class VerificationStatusEnum(str, Enum):
    """Clasificación estricta del nivel de verificación del dato científico."""
    verificado_con_fuente = "verificado_con_fuente"
    inferencia_razonable = "inferencia_razonable"
    hipotesis = "hipotesis"
    pendiente_de_verificar = "pendiente_de_verificar"


class PriorityEnum(str, Enum):
    """Prioridad operativa para el motor AnalogX."""
    MVP = "MVP"
    segunda_fase = "segunda_fase"
    descartado = "descartado"


class StrictCategoryEnum(str, Enum):
    """Categoría estricta obligatoria para todo dataset catalogado."""
    dato_instrumental = "dato_instrumental"
    producto_derivado = "producto_derivado"
    interpretacion_bibliografica = "interpretacion_bibliografica"
    dato_demostracion = "dato_demostracion"


class ProcessingComplexityEnum(str, Enum):
    """Nivel de complejidad técnica de procesamiento del dataset."""
    baja = "baja"
    media = "media"
    alta = "alta"
    critica = "critica"


class ScientificSource(BaseModel):
    """
    Representa una fuente u organismo científico oficial (ej. NASA PDS, ESA CDSE).
    """
    id: str = Field(..., description="Identificador único slug de la fuente (ej. 'nasa_pds')")
    name: str = Field(..., description="Nombre canónico completo de la fuente")
    agency: str = Field(..., description="Agencia responsable (NASA, ESA, CSA, JAXA, etc.)")
    catalog_or_mission: str = Field(..., description="Misión, instrumento o catálogo federado principal")
    url: str = Field(..., description="URL oficial del recurso")
    access_type: AccessTypeEnum = Field(..., description="Tipo de acceso y credenciales requeridas")
    auth_requirements: Optional[str] = Field(None, description="Descripción de credenciales (URS, OAuth2, etc.) o None")
    license: str = Field(..., description="Licencia de uso del dato (ej. 'NASA Open Data Policy')")
    verification_status: VerificationStatusEnum = Field(
        VerificationStatusEnum.pendiente_de_verificar,
        description="Estado de verificación científica de la fuente"
    )
    priority: PriorityEnum = Field(PriorityEnum.MVP, description="Prioridad para la hoja de ruta de AnalogX")
    notes: Optional[str] = Field(None, description="Observaciones técnicas o metodológicas")


class DatasetMetadata(BaseModel):
    """
    Metadatos rigurosos para un dataset específico indexado en el motor.
    """
    official_id: str = Field(..., description="Identificador de producto oficial (ej. 'NASADEM_HGT.001')")
    name: str = Field(..., description="Nombre descriptivo del producto")
    source_id: str = Field(..., description="Clave de la fuente asociada en ScientificSource")
    url: str = Field(..., description="URL o DOI específico de acceso o documentación del producto")
    version: Optional[str] = Field(None, description="Versión oficial del producto o algoritmo de procesamiento")
    spatial_coverage: str = Field(..., description="Cobertura geográfica o planetaria del producto")
    spatial_resolution: str = Field(..., description="Resolución espacial cuantitativa con unidades (ej. '30m', '463m')")
    temporal_coverage: Optional[str] = Field(None, description="Periodo temporal cubierto o fecha de observación")
    available_formats: List[str] = Field(default_factory=list, description="Formatos de distribución (GeoTIFF, PDS3, etc.)")
    units: str = Field(..., description="Unidades físicas de los valores raster o tabulares")
    download_method: str = Field(..., description="Método técnico de descarga (API REST, STAC, HTTPS, SFTP)")
    strict_category: StrictCategoryEnum = Field(
        ...,
        description="Categoría estricta: dato_instrumental | producto_derivado | interpretacion_bibliografica | dato_demostracion"
    )
    processing_complexity: ProcessingComplexityEnum = Field(
        ProcessingComplexityEnum.media,
        description="Grado de complejidad técnica para ingerir y normalizar el producto"
    )
    limitaciones: str = Field(..., description="Restricciones de calidad, vacíos o sesgos físicos conocidos")
    is_verified: bool = Field(False, description="Flag booleano de verificación")
    verification_status: VerificationStatusEnum = Field(
        VerificationStatusEnum.pendiente_de_verificar,
        description="Nivel de verificación del producto"
    )

