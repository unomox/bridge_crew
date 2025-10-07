from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Protocol


@dataclass
class BacklogItem:
    identifier: str
    title: str
    acceptance_criteria: List[str] = field(default_factory=list)


@dataclass
class ExecutionPlan:
    plan_id: str
    summary: str
    tasks: List[str] = field(default_factory=list)


class Agent(Protocol):
    name: str

    def perform(self, task: str) -> str:  # pragma: no cover - behavior defined by implementers
        ...


AgentMap = Dict[str, Agent]


