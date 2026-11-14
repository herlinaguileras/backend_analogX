"""
AnalogX — Planetary Analog Discovery Engine
Módulo: app.models.evidence
Descripción: Esquemas Pydantic para evidencias cualitativas, comparaciones estructuradas y limitaciones científicas.
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from app.models.dataset import VerificationStatusEnum


class ComparabilityTypeEnum(str, Enum):
    """Categorización epistemológica de la comparación Tierra-Marte."""
    directa = "directa"
    indirecta = "indirecta"
    cualitativa = "cualitativa"
    incompatible = "incompatible"


class QualitativeEvidence(BaseModel):
    """
    Evidencia cualitativa geológica documentada en literatura o misiones espaciales.
    """
    id: str = Field(..., description="Identificador único de la evidencia cualitativa")
    region_id: str = Field(..., description="Identificador de la región asociada (terrestre o planetaria)")
    feature_name: str = Field(..., description="Nombre del rasgo geológico (ej. 'Polígonos de desecación de halita')")
    description: str = Field(..., description="Descripción geológica detallada de la observación visual o de campo")
    observed_features: List[str] = Field(
        default_factory=list,
        description="Lista de descriptores observables (ej. 'grietas tensionales', 'rebordes sobreelevados')"
    )
    geological_interpretation: str = Field(..., description="Inferencia de procesos sedimentarios o hidrotermales activos")
    bibliographical_source: str = Field(..., description="Cita bibliográfica formal que sustenta la evidencia")
    verification_status: VerificationStatusEnum = Field(
        VerificationStatusEnum.verificado_con_fuente,
        description="Estado de verificación de la evidencia"
    )


class ScientificLimitation(BaseModel):
    """
    Documenta explícitamente una divergencia física, química o ambiental que limita la analogía.
    Garantiza que el sistema no induzca a conclusiones falsas de equivalencia total.
    """
    id: str = Field(..., description="Identificador de la limitación (ej. 'lim_gravity_slope_difference')")
    parameter_name: str = Field(..., description="Parámetro o proceso físico afectado (ej. 'Aceleración gravitacional')")
    terrestrial_condition: str = Field(..., description="Valor o estado en la Tierra (ej. 'g = 9.81 m/s²')")
    planetary_condition: str = Field(..., description="Valor o estado en Marte/Luna (ej. 'g = 3.71 m/s²')")
    limitation_mechanism: str = Field(..., description="Explicación del mecanismo físico que impide la equivalencia")
    impact_on_analogy: str = Field(..., description="Impacto geológico: cómo debe interpretarse con cautela el dato")
    is_blocking_for_direct_comparison: bool = Field(
        ...,
        description="True si la diferencia invalida cualquier comparación matemática directa"
    )


class StructuredComparison(BaseModel):
    """
    Estructura analítica que compara una dimensión específica entre un análogo terrestre y un objetivo planetario.
    """
    id: str = Field(..., description="Identificador de la comparación estructurada")
    terrestrial_region_id: str = Field(..., description="ID de la región terrestre analizada")
    planetary_region_id: str = Field(..., description="ID del objetivo planetario contrastado")
    variable_or_feature: str = Field(..., description="Nombre del parámetro o rasgo comparado (ej. 'slope', 'polygons')")
    comparability_type: ComparabilityTypeEnum = Field(
        ...,
        description="Clasificación epistemológica: directa | indirecta | cualitativa | incompatible"
    )
    terrestrial_measurement_id: Optional[str] = Field(
        None,
        description="ID de la medición instrumental terrestre o None si cualitativa"
    )
    planetary_measurement_id: Optional[str] = Field(
        None,
        description="ID de la medición instrumental planetaria o None si cualitativa"
    )
    resolution_compatibility: str = Field(
        ...,
        description="Evaluación de resolución cruzada (ej. 'Incompatible sin remuestreo: 30m vs 463m')"
    )
    resampling_required: bool = Field(
        ...,
        description="True si se requiere transformación o convolución de escala espacial"
    )
    physical_divergence_notes: str = Field(
        ...,
        description="Notas rigurosas sobre divergencias ambientales y geológicas no reducibles"
    )
    scientific_limitations: List[ScientificLimitation] = Field(
        default_factory=list,
        description="Lista de limitaciones físicas asociadas a esta comparación específica"
    )
    verification_status: VerificationStatusEnum = Field(
        VerificationStatusEnum.pendiente_de_verificar,
        description="Nivel de verificación del análisis comparativo"
    )
    summary_conclusion: Optional[str] = Field(
        None,
        description="Conclusión científica sintetizada del grado de plausibilidad análoga"
    )

