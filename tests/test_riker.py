from src.core.agents.base import BacklogItem
from src.core.agents.data import DataAgent
from src.core.orchestrator.riker import RikerOrchestrator


def test_riker_plan_and_delegate():
    riker = RikerOrchestrator(agents={"data": DataAgent()})
    item = BacklogItem(identifier="BC-1", title="Initialize orchestrator skeleton")
    plan = riker.plan(item)
    assert plan.plan_id == "plan-BC-1"
    assert any("Implement" in t for t in plan.tasks)

    status = riker.delegate(plan)
    assert status is not None
    assert "Data processed task" in status or "Delegated" in status


