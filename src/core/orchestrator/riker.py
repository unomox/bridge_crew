from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from src.core.agents.base import AgentMap, BacklogItem, ExecutionPlan


@dataclass
class RikerOrchestrator:
    agents: AgentMap

    def plan(self, item: BacklogItem) -> ExecutionPlan:
        summary = f"Plan for {item.identifier}: {item.title}"
        tasks = [
            "Analyze requirements",
            "Design approach and identify risks",
            "Implement changes",
            "Write tests and validation",
            "Prepare PR with evidence and decisions",
        ]
        return ExecutionPlan(plan_id=f"plan-{item.identifier}", summary=summary, tasks=tasks)

    def delegate(self, plan: ExecutionPlan) -> Optional[str]:
        # Delegate basic analysis/design tasks to Data if available
        results: List[str] = []
        data = self.agents.get("data")
        if data is not None:
            for task in plan.tasks:
                if any(keyword in task.lower() for keyword in ["analyze", "design"]):
                    results.append(data.perform(task))

        return (
            ", ".join(results) if results else f"Delegated {len(plan.tasks)} tasks to specialists"
        )


