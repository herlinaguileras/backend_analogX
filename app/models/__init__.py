"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models
Exportación unificada de esquemas y modelos científicos Pydantic.
"""

from app.models.dataset import (
    AccessTypeEnum,
    DatasetMetadata,
    PriorityEnum,
    ProcessingComplexityEnum,
    ScientificSource,
    StrictCategoryEnum,
    VerificationStatusEnum,
)
from app.models.evidence import (
    ComparabilityTypeEnum,
    QualitativeEvidence,
    ScientificLimitation,
    StructuredComparison,
)
from app.models.observation import (
    ObservationMeasurement,
    ObservedVariable,
)
from app.models.region import (
    BoundingBox,
    CoordinateSystemTypeEnum,
    CRSDatumMetadata,
    PlanetEnum,
    PlanetaryRegion,
    TerrestrialRegion,
)

__all__ = [
    # dataset
    "AccessTypeEnum",
    "VerificationStatusEnum",
    "PriorityEnum",
    "StrictCategoryEnum",
    "ProcessingComplexityEnum",
    "ScientificSource",
    "DatasetMetadata",
    # region
    "PlanetEnum",
    "CoordinateSystemTypeEnum",
    "CRSDatumMetadata",
    "BoundingBox",
    "TerrestrialRegion",
    "PlanetaryRegion",
    # observation
    "ObservedVariable",
    "ObservationMeasurement",
    # evidence
    "ComparabilityTypeEnum",
    "QualitativeEvidence",
    "ScientificLimitation",
    "StructuredComparison",
    # catalog & frontend
    "catalog_data",
    "frontend",
]

