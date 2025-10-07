from src.core.agents.troi import TroiAgent


def test_troi_agent_perform():
    agent = TroiAgent()
    out = agent.perform("Clarify acceptance criteria")
    assert "Troi clarified stakeholder intent" in out


