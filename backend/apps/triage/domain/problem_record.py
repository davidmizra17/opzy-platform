"""Registro estructurado del problema y reglas de enrutamiento. Sin Django."""

from dataclasses import dataclass, field
from enum import StrEnum


class Route(StrEnum):
    BUILD = "build"      # quiere construir algo (landing, sitio)
    SOLVE = "solve"      # problema en un proceso existente
    OTHER = "other"      # fuera de alcance o poco claro


class PainType(StrEnum):
    ACQUISITION = "acquisition"
    OPERATIONS = "operations"
    UNCLEAR = "unclear"


@dataclass(frozen=True)
class Fact:
    """Un dato que dio el cliente, con referencia al mensaje de origen."""

    key: str
    value: str
    message_id: str


@dataclass
class ProblemRecord:
    business_name: str = ""
    industry: str = ""
    country: str = ""
    goal: str = ""
    restatement: str = ""
    pain_type: PainType = PainType.UNCLEAR
    processes_involved: int = 0
    tools: list[str] = field(default_factory=list)
    regulated_data: bool = False
    out_of_scope: bool = False
    facts: list[Fact] = field(default_factory=list)
    confidence: float = 0.0
    clarifying_rounds: int = 0
    confirmed: bool = False

    def fact_texts(self) -> list[str]:
        return [f.value for f in self.facts]


@dataclass(frozen=True)
class RoutingDecision:
    route: Route
    needs_human: bool
    reason: str


CONFIDENCE_THRESHOLD = 0.7
MAX_CLARIFYING_ROUNDS = 2


def decide_route(record: ProblemRecord) -> RoutingDecision:
    """Reglas de enrutamiento. Solo se aplican a un registro confirmado por el cliente."""
    if not record.confirmed:
        raise ValueError("El cliente debe confirmar el resumen antes de enrutar.")

    if record.out_of_scope:
        return RoutingDecision(Route.OTHER, needs_human=False, reason="fuera de alcance")

    if record.confidence < CONFIDENCE_THRESHOLD:
        return RoutingDecision(Route.OTHER, needs_human=True, reason="confianza baja")

    if record.pain_type is PainType.ACQUISITION:
        return RoutingDecision(Route.BUILD, needs_human=False, reason="captación")

    if record.pain_type is PainType.OPERATIONS:
        complex_case = record.processes_involved > 1 or record.regulated_data
        return RoutingDecision(
            Route.SOLVE,
            needs_human=True,
            reason="varios procesos o datos regulados" if complex_case else "un proceso",
        )

    if record.clarifying_rounds >= MAX_CLARIFYING_ROUNDS:
        return RoutingDecision(Route.OTHER, needs_human=True, reason="sigue poco claro")

    return RoutingDecision(Route.OTHER, needs_human=True, reason="sin clasificar")
