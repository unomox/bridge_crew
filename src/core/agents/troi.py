from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TroiAgent:
    name: str = "troi"

    def perform(self, task: str) -> str:  # pragma: no cover - simple stub
        return f"Troi clarified stakeholder intent for task: {task}"


