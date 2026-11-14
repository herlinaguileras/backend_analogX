"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models.frontend
Descripción: Modelos Pydantic para el contrato de transporte y tipos científicos requeridos por el frontend.
"""

from typing import Any, Generic, List, Literal, Optional, TypeVar, Union
from pydantic import BaseModel, Field

T = TypeVar("T")

PlanetaryBody = Literal["Earth", "Mars", "Moon"]
SourcePriority = Literal["MVP", "segunda_fase", "descartado"]
VerificationStatus = Literal[
    "verificado_con_fuente",
    "inferencia_razonable",
    "hipotesis",
    "pendiente_de_verificar",
]
DatasetCategory = Literal[
    "dato_instrumental",
    "producto_derivado",
    "interpretacion_bibliografica",
    "dato_demostracion",
]
ObservedVariableType = Literal[
    "pendiente",
    "rugosidad",
    "morfologia",
    "mineralogia",
    "procesos_evaporiticos",
    "contexto_ambiental",
]
ComparisonType = Literal["directa", "indirecta", "cualitativa"]
PhysicalIncompatibility = Literal[
    "gravedad",
    "atmosfera",
    "datums",
    "procesos_antiguos_vs_actuales",
    "resolucion_espacial",
    "unidades",
    "metodo_procesamiento",
    "otra",
]

AnalogyNotice = Literal[
    "La analogía no implica habitabilidad ni idoneidad para una base humana."
]

MissionCategory = Literal[
    "rover_mobility",
    "instrument_calibration",
    "base_habitat_shielding",
    "isru_resources",
]


class MissionUseCaseFrontend(BaseModel):
    id: str
    title: str
    category: MissionCategory
    earth_region_id: str
    planetary_target_id: str
    applicable_mission: str
    description: str
    operational_method: str
    trl_readiness: int = 4
    nasa_challenge_dimension: str


class ListResponse(BaseModel, Generic[T]):
    items: List[T]
    next_cursor: Optional[str] = None


class SpatialResolution(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None
    unit: Optional[str] = None
    description: Optional[str] = None


class CrsDatum(BaseModel):
    body: PlanetaryBody
    crs_name: Optional[str] = None
    authority_code: Optional[str] = None
    horizontal_datum: Optional[str] = None
    vertical_datum: Optional[str] = None
    coordinate_unit: Optional[str] = None
    latitude_convention: Optional[Literal["planetocentric", "planetographic"]] = None
    longitude_convention: Optional[Literal["east_180", "east_360", "west_360"]] = None


class BibliographicCitation(BaseModel):
    id: str
    title: Optional[str] = None
    authors: Optional[List[str]] = None
    publication_year: Optional[int] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    source_id: Optional[str] = None
    accessed_at: Optional[str] = None


class ScientificLimitationFrontend(BaseModel):
    id: str
    text: str
    incompatibilities: List[PhysicalIncompatibility]
    affected_observation_ids: List[str] = Field(default_factory=list)
    citation_ids: List[str] = Field(default_factory=list)
    verification_status: VerificationStatus
    analogy_notice: AnalogyNotice = "La analogía no implica habitabilidad ni idoneidad para una base humana."


class DatasetMetadataFrontend(BaseModel):
    id: str
    source_id: Optional[str] = None
    product_id: Optional[str] = None
    mission: Optional[str] = None
    instrument: Optional[str] = None
    version: Optional[str] = None
    spatial_resolution: Optional[SpatialResolution] = None
    units: Optional[List[str]] = None
    download_method: Optional[str] = None
    download_url: Optional[str] = None
    category: DatasetCategory
    verification_status: VerificationStatus
    limitations: List[ScientificLimitationFrontend] = Field(default_factory=list)


class ScientificSourceFrontend(BaseModel):
    id: str
    name: str
    agency: Optional[str] = None
    official_url: Optional[str] = None
    url: Optional[str] = None
    license: Optional[str] = None
    priority: SourcePriority


class RegionGeometry(BaseModel):
    type: Literal["Point", "Polygon", "MultiPolygon"]
    coordinates: Any


class RegionMetadataBase(BaseModel):
    id: str
    name: str
    country: Optional[str] = None
    description: Optional[str] = None
    geometry: Optional[RegionGeometry] = None
    approximate_coordinates: Optional[List[float]] = None
    crs_datum: Optional[CrsDatum] = None
    novelty_level: Optional[Literal["reference_established", "candidate_to_assess", "documented_novelty"]] = None
    novelty_justification: Optional[str] = None
    verification_status: VerificationStatus
    dataset_ids: List[str] = Field(default_factory=list)
    citation_ids: List[str] = Field(default_factory=list)
    limitations: List[ScientificLimitationFrontend] = Field(default_factory=list)


class EarthRegion(RegionMetadataBase):
    body: Literal["Earth"] = "Earth"
    study_role: Literal["reference_calibration", "research_candidate"]


class PlanetaryTarget(RegionMetadataBase):
    body: Literal["Mars", "Moon"]
    study_role: Literal["planetary_target"] = "planetary_target"


class ScientificObservationFrontend(BaseModel):
    id: str
    region_id: str
    dataset_id: Optional[str] = None
    source_id: Optional[str] = None
    source_url: Optional[str] = None
    product_id: Optional[str] = None
    acquisition_date: Optional[str] = None
    version: Optional[str] = None
    variable: ObservedVariableType
    unit: Optional[str] = None
    spatial_resolution: Optional[SpatialResolution] = None
    crs_datum: Optional[CrsDatum] = None
    processing_method: Optional[str] = None
    value: Optional[Union[float, int, str]] = None
    quality: Optional[str] = None
    uncertainty: Optional[str] = None
    verification_status: VerificationStatus
    citation_ids: List[str] = Field(default_factory=list)
    limitations: List[ScientificLimitationFrontend] = Field(default_factory=list)


class QualitativeEvidenceFrontend(BaseModel):
    id: str
    text: str
    evidence_type: Literal["bibliografica", "observacional"]
    comparison_type: ComparisonType
    region_ids: List[str] = Field(default_factory=list)
    observation_ids: List[str] = Field(default_factory=list)
    citation_ids: List[str] = Field(default_factory=list)
    verification_status: VerificationStatus
    limitations: List[ScientificLimitationFrontend] = Field(default_factory=list)
    analogy_notice: AnalogyNotice = "La analogía no implica habitabilidad ni idoneidad para una base humana."


class ResamplingRequirement(BaseModel):
    required: Optional[bool] = None
    target_resolution: Optional[SpatialResolution] = None
    method: Optional[str] = None
    justification: Optional[str] = None
    performed: Optional[bool] = None


class VariableComparisonFrontend(BaseModel):
    variable: ObservedVariableType
    earth_observation_id: Optional[str] = None
    target_observation_id: Optional[str] = None
    comparison_type: ComparisonType
    compatibility: Literal["compatible", "requires_processing", "incompatible", "pending"]
    compatibility_reason: Optional[str] = None
    common_unit: Optional[str] = None
    unit_conversion_method: Optional[str] = None
    resampling: ResamplingRequirement
    evidence_ids: List[str] = Field(default_factory=list)
    limitations: List[ScientificLimitationFrontend] = Field(default_factory=list)
    earth_value: Optional[str] = None
    target_value: Optional[str] = None


class ComparisonPayloadFrontend(BaseModel):
    id: str
    contract_version: Literal["0"] = "0"
    generated_at: Optional[str] = None
    methodology_version: Optional[str] = None
    earth_region: EarthRegion
    planetary_target: PlanetaryTarget
    observations: List[ScientificObservationFrontend] = Field(default_factory=list)
    variables: List[VariableComparisonFrontend] = Field(default_factory=list)
    qualitative_evidence: List[QualitativeEvidenceFrontend] = Field(default_factory=list)
    sources: List[ScientificSourceFrontend] = Field(default_factory=list)
    datasets: List[DatasetMetadataFrontend] = Field(default_factory=list)
    citations: List[BibliographicCitation] = Field(default_factory=list)
    limitations: List[ScientificLimitationFrontend] = Field(default_factory=list)
    mission_use_cases: List[MissionUseCaseFrontend] = Field(default_factory=list)
    analogy_notice: AnalogyNotice = "La analogía no implica habitabilidad ni idoneidad para una base humana."


class RegionDetailResponse(BaseModel):
    region: Union[EarthRegion, PlanetaryTarget]
    observations: List[ScientificObservationFrontend] = Field(default_factory=list)
    datasets: List[DatasetMetadataFrontend] = Field(default_factory=list)
    sources: List[ScientificSourceFrontend] = Field(default_factory=list)
    citations: List[BibliographicCitation] = Field(default_factory=list)
    mission_use_cases: List[MissionUseCaseFrontend] = Field(default_factory=list)


class CompareRequest(BaseModel):
    earth_region_id: str
    planetary_target_id: str


class FindingItem(BaseModel):
    id: str
    title: str
    summary: str
    evidence_count: int
    verification_status: VerificationStatus
    earth_region_name: str
    target_name: str
    limitations_summary: str

