"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models.db_models
Descripción: Modelos de tablas relacionales SQLModel para persistencia SQLite en AnalogX.
"""

from typing import Optional
from sqlmodel import Field, SQLModel


class RegionDB(SQLModel, table=True):
    __tablename__ = "regions"

    id: str = Field(primary_key=True, index=True)
    name: str = Field(index=True)
    body: str = Field(default="Earth")
    study_role: str = Field(index=True)  # reference_calibration | research_candidate
    country: str = Field(default="Bolivia")
    department: Optional[str] = None
    description: str
    approx_lat: Optional[float] = None
    approx_lon: Optional[float] = None
    elevation_min_m: Optional[float] = None
    elevation_max_m: Optional[float] = None
    crs_code: str = Field(default="EPSG:4326")
    crs_name: str = Field(default="WGS 84 / Geographic")
    vertical_datum: str = Field(default="Geoide EGM96")
    novelty_level: Optional[str] = None
    novelty_justification: Optional[str] = None
    verification_status: str = Field(default="verificado_con_fuente")
    primary_analog_feature: str = Field(default="")


class PlanetaryTargetDB(SQLModel, table=True):
    __tablename__ = "planetary_targets"

    id: str = Field(primary_key=True, index=True)
    name: str = Field(index=True)
    body: str = Field(index=True)  # Mars | Moon
    target_feature_name: str
    regional_context: str
    center_lat: float
    center_lon: float
    crs_code: str
    crs_name: str
    vertical_datum: str
    target_type: str
    verification_status: str
    description: str
    mission_program: str  # Artemis | Mars Exploration Program
    trek_portal_url: Optional[str] = None


class MissionUseCaseDB(SQLModel, table=True):
    __tablename__ = "mission_use_cases"

    id: str = Field(primary_key=True, index=True)
    title: str
    category: str = Field(index=True)  # rover_mobility | instrument_calibration | base_habitat_shielding | isru_resources
    earth_region_id: str = Field(index=True)
    planetary_target_id: str = Field(index=True)
    applicable_mission: str  # ej. NASA Artemis III/IV, Mars 2020, VIPER
    description: str
    operational_method: str
    trl_readiness: int = Field(default=4)  # Technology Readiness Level (1-9)
    nasa_challenge_dimension: str  # Una de las 7 dimensiones oficiales del reto


class DatasetDB(SQLModel, table=True):
    __tablename__ = "datasets"

    official_id: str = Field(primary_key=True, index=True)
    name: str
    source_id: str = Field(index=True)
    mission: str
    instrument: str
    version: Optional[str] = None
    spatial_resolution: str
    units: str
    download_method: str
    download_url: str
    strict_category: str  # dato_instrumental | producto_derivado | interpretacion_bibliografica
    verification_status: str = Field(default="verificado_con_fuente")
    limitaciones: str


class ScientificSourceDB(SQLModel, table=True):
    __tablename__ = "sources"

    id: str = Field(primary_key=True, index=True)
    name: str
    agency: str
    url: str
    license: str
    priority: str = Field(default="MVP")


class BibliographicCitationDB(SQLModel, table=True):
    __tablename__ = "citations"

    id: str = Field(primary_key=True, index=True)
    title: str
    authors: str
    publication_year: int
    doi: Optional[str] = None
    url: Optional[str] = None
    source_id: Optional[str] = None
