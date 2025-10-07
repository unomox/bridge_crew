from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LaForgeAgent:
    name: str = "laforge"

    def perform(self, task: str) -> str:  # pragma: no cover - simple stub
        return f"La Forge optimized CI task: {task}"


