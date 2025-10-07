from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from src.core.agents.base import AgentMap, BacklogItem, ExecutionPlan
from src.core.observability.logging import log_info


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
        plan = ExecutionPlan(plan_id=f"plan-{item.identifier}", summary=summary, tasks=tasks)
        log_info("orchestrator.plan", correlation_id=plan.plan_id, itemId=item.identifier, tasks=len(tasks))
        return plan

    def delegate(self, plan: ExecutionPlan) -> Optional[str]:
        # Delegate basic analysis/design tasks to Data if available
        results: List[str] = []
        data = self.agents.get("data")
        if data is not None:
            for task in plan.tasks:
                if any(keyword in task.lower() for keyword in ["analyze", "design"]):
                    out = data.perform(task)
                    results.append(out)
                    log_info("delegate.data", correlation_id=plan.plan_id, task=task)

        return (
            ", ".join(results) if results else f"Delegated {len(plan.tasks)} tasks to specialists"
        )


