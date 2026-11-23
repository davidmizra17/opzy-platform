"""Puertos de triage. El adaptador del LLM vive en infrastructure."""

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class ToolCall:
    name: str
    input: dict[str, Any]


@dataclass(frozen=True)
class AgentReply:
    text: str
    tool_calls: list[ToolCall]


class LlmClient(Protocol):
    def respond(
        self, *, system: str, messages: list[dict], tools: list[dict]
    ) -> AgentReply: ...
