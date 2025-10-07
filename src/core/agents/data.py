from __future__ import annotations

from dataclasses import dataclass
from src.core.observability.logging import log_info


@dataclass
class DataAgent:
    name: str = "data"

    def perform(self, task: str) -> str:  # pragma: no cover - simple stub
        log_info("data.perform", task=task)
        return f"Data processed task: {task}"


