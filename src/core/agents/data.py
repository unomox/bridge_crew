from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DataAgent:
    name: str = "data"

    def perform(self, task: str) -> str:  # pragma: no cover - simple stub
        return f"Data processed task: {task}"


