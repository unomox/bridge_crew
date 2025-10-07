from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any, Dict, Optional


_LOGGER_NAME = "bridge_crew"


def _ensure_logger_configured() -> logging.Logger:
    logger = logging.getLogger(_LOGGER_NAME)
    if not logger.handlers:
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.propagate = False
    return logger


def _now_iso() -> str:
    return datetime.now(tz=timezone.utc).isoformat()


def log_info(event: str, correlation_id: Optional[str] = None, **attributes: Any) -> None:
    logger = _ensure_logger_configured()
    payload: Dict[str, Any] = {
        "ts": _now_iso(),
        "level": "INFO",
        "event": event,
    }
    if correlation_id is not None:
        payload["correlationId"] = correlation_id
    if attributes:
        payload["attributes"] = attributes
    logger.info(json.dumps(payload, separators=(",", ":")))


