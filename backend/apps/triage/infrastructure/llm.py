"""Adaptadores del LLM. Agregar el del proveedor elegido implementando LlmClient."""

from apps.triage.application.ports import AgentReply


class FakeLlmClient:
    """Para tests y desarrollo local sin clave de API."""

    def __init__(self, replies: list[AgentReply] | None = None):
        self.replies = list(replies or [])
        self.calls: list[dict] = []

    def respond(self, *, system, messages, tools) -> AgentReply:
        self.calls.append({"system": system, "messages": messages, "tools": tools})
        return self.replies.pop(0) if self.replies else AgentReply(text="", tool_calls=[])
