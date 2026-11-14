"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models.region
Descripción: Esquemas Pydantic para regiones terrestres, planetarias y metadatos de sistemas de referencia (CRS/Datum).
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class PlanetEnum(str, Enum):
    """Cuerpo celeste de la región analizada."""
    Tierra = "Tierra"
    Marte = "Marte"
    Luna = "Luna"


class CoordinateSystemTypeEnum(str, Enum):
    """Convención geométrica del sistema de coordenadas planetario."""
    geografico_terrestre = "geografico_terrestre"
    planetocentrico = "planetocentrico"
    planetografico = "planetografico"
    selenografico = "selenografico"


class CRSDatumMetadata(BaseModel):
    """
    Especificación explícita del Sistema de Coordenadas de Referencia (CRS) y Datum.
    Evita la asunción errónea de equivalencia entre superficies de referencia planetarias.
    """
    crs_name: str = Field(..., description="Nombre canónico (ej. 'WGS 84 / Geographic', 'IAU 2000 Mars')")
    crs_code: str = Field(..., description="Código de autoridad estándar (ej. 'EPSG:4326', 'IAU:49900')")
    datum_name: str = Field(..., description="Nombre del Datum geodésico (ej. 'World Geodetic System 1984', 'Mars 2000')")
    reference_surface: str = Field(
        ...,
        description="Superficie vertical u horizontal de referencia (ej. 'Geoide EGM96', 'Areoide MOLA R=3396.0km')"
    )
    is_planetary: bool = Field(..., description="True si es extraterrestre; False si es terrestre")
    equatorial_radius_m: Optional[float] = Field(None, description="Radio ecuatorial del elipsoide/esfera en metros")
    polar_radius_m: Optional[float] = Field(None, description="Radio polar en metros")
    flattening: Optional[float] = Field(None, description="Aplanamiento elipsoidal f = (a - b) / a")


class BoundingBox(BaseModel):
    """
    Límites espaciales geográficos o planetocéntricos de una región de interés (AOI).
    """
    min_lat: float = Field(..., description="Latitud mínima en grados decimales (Sur negativo)")
    max_lat: float = Field(..., description="Latitud máxima en grados decimales")
    min_lon: float = Field(..., description="Longitud mínima en grados decimales (Oeste negativo o 0-360 Este según CRS)")
    max_lon: float = Field(..., description="Longitud máxima en grados decimales")
    crs_code: str = Field("EPSG:4326", description="Código de referencia espacial de las coordenadas del bounding box")


class TerrestrialRegion(BaseModel):
    """
    Región análoga terrestre situada en el Altiplano boliviano o sectores análogos.
    """
    id: str = Field(..., description="Slug único identificador (ej. 'bo_salar_uyuni', 'bo_sol_de_manana')")
    name: str = Field(..., description="Nombre toponímico oficial")
    country: str = Field("Bolivia", description="País soberano")
    department: str = Field(..., description="Departamento administrativo (ej. 'Potosí', 'Oruro')")
    province: Optional[str] = Field(None, description="Provincia geográfica específica")
    bounding_box: BoundingBox = Field(..., description="Límites espaciales de la región")
    center_lat: float = Field(..., description="Latitud del centroide geográfico WGS84")
    center_lon: float = Field(..., description="Longitud del centroide geográfico WGS84")
    elevation_min_m: Optional[float] = Field(None, description="Cota mínima sobre el nivel medio del mar (geoide)")
    elevation_max_m: Optional[float] = Field(None, description="Cota máxima sobre el nivel medio del mar (geoide)")
    crs_datum: CRSDatumMetadata = Field(..., description="Metadatos completos de proyección y datum terrestre")
    geological_context: str = Field(..., description="Descripción del marco geomorfológico, volcánico o evaporítico")
    is_reference_site: bool = Field(
        False,
        description="True si es sitio patrón de calibración (Uyuni); False si es candidato de investigación novedoso"
    )
    primary_evaporite_minerals: List[str] = Field(
        default_factory=list,
        description="Fases salinas o minerales dominantes (halita, yeso, azufre, ulexita, etc.)"
    )
    literature_references: List[str] = Field(
        default_factory=list,
        description="Publicaciones científicas peer-reviewed que documentan el sitio"
    )


class PlanetaryRegion(BaseModel):
    """
    Región u objetivo geológico en un cuerpo extraterrestre (Marte o Luna).
    """
    id: str = Field(..., description="Slug único del objetivo planetario (ej. 'mars_terra_sirenum_chloride_01')")
    planet: PlanetEnum = Field(PlanetEnum.Marte, description="Cuerpo celeste de destino")
    target_feature_name: str = Field(..., description="Nombre del accidente o depósito geológico")
    regional_context: str = Field(..., description="Contexto provincial o de cuenca (ej. 'Tierras altas del sur / Terra Sirenum')")
    bounding_box: Optional[BoundingBox] = Field(None, description="Bounding box en coordenadas planetarias si está delimitado")
    center_lat: float = Field(..., description="Latitud planetocéntrica nominal en grados (-90 a +90)")
    center_lon: float = Field(..., description="Longitud planetocéntrica nominal en grados (0 a 360 Este)")
    coordinate_system_type: CoordinateSystemTypeEnum = Field(
        CoordinateSystemTypeEnum.planetocentrico,
        description="Sistema de coordenadas planetarias empleado"
    )
    crs_datum: CRSDatumMetadata = Field(..., description="Metadatos de elipsoide y Areoide/esfera planetaria")
    target_type: str = Field(..., description="Tipología geológica: 'deposito_cloruros', 'paleocanal_invertido', etc.")
    primary_references: List[str] = Field(
        default_factory=list,
        description="Publicaciones de misiones NASA que sustentan la detección del rasgo"
    )
    known_instrumental_observations: List[str] = Field(
        default_factory=list,
        description="Identificadores oficiales de productos que cubren el sitio (HiRISE, THEMIS, CRISM, MOLA)"
    )

