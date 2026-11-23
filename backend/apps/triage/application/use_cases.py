"""Turno del agente. Pendiente de implementar en la Fase 1.

Flujo previsto:
1. Cargar historial y registro del problema.
2. Llamar al LLM con el catálogo de secciones y las herramientas
   (update_problem_record, confirm_summary, update_page, escalate).
3. Ejecutar las llamadas a herramientas a través de los casos de uso de cada módulo.
4. Devolver errores de validación al LLM para que corrija (máximo N reintentos).
5. Transmitir la respuesta al widget.
"""

from apps.triage.domain.problem_record import ProblemRecord, RoutingDecision, decide_route

from .ports import LlmClient


class TriageUseCases:
    def __init__(self, llm: LlmClient):
        self.llm = llm

    def route(self, record: ProblemRecord) -> RoutingDecision:
        return decide_route(record)
