from src.core.agents.worf import WorfAgent


def test_worf_agent_perform():
    agent = WorfAgent()
    out = agent.perform("Scan dependencies")
    assert "Worf completed security task" in out


