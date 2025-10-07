from __future__ import annotations

from dataclasses import dataclass


@dataclass
class WorfAgent:
    name: str = "worf"

    def perform(self, task: str) -> str:  # pragma: no cover - simple stub
        return f"Worf completed security task: {task}"


