from src.core.agents.crusher import CrusherAgent


def test_crusher_agent_perform():
    agent = CrusherAgent()
    out = agent.perform("Validate tests")
    assert "Crusher validated quality task" in out


