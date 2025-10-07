from src.core.observability.logging import log_info


def test_log_info_outputs_json(capsys):
    log_info("test-event", correlation_id="cid-1", foo="bar")
    out = capsys.readouterr().out.strip()
    assert out.startswith("{") and out.endswith("}")
    assert '"event":"test-event"' in out
    assert '"correlationId":"cid-1"' in out
    assert '"foo":"bar"' in out


