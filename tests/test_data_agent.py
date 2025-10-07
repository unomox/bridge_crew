from src.core.agents.data import DataAgent


def test_data_agent_perform():
    agent = DataAgent()
    out = agent.perform("Analyze requirements")
    assert "Data processed task" in out

