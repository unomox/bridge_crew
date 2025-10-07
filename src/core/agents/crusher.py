from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CrusherAgent:
    name: str = "crusher"

    def perform(self, task: str) -> str:  # pragma: no cover - simple stub
        return f"Crusher validated quality task: {task}"


