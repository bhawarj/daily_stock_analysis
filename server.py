# -*- coding: utf-8 -*-
"""
===================================
Daily Stock Analysis - FastAPI backend entrypoint
===================================

Responsibilities:
1. Expose the RESTful API service
2. Configure CORS support
3. Provide health check endpoints
4. Serve frontend static assets in production mode

Startup examples:
    uvicorn server:app --reload --host 0.0.0.0 --port 8000
    (When GUARD_ENABLED is active, add --no-proxy-headers or keep
     FORWARDED_ALLOW_IPS consistent with GUARD_TRUSTED_PROXIES)

    Or via main.py:
    python main.py --serve-only      # Start API service only
    python main.py --serve           # Start API + analysis pipeline
"""

import logging

from src.config import setup_env, get_config
from src.logging_config import setup_logging

# Initialize environment variables and logging
setup_env()

config = get_config()
level_name = (config.log_level or "INFO").upper()
level = getattr(logging, level_name, logging.INFO)

setup_logging(
    log_prefix="api_server",
    console_level=level,
    extra_quiet_loggers=['uvicorn', 'fastapi'],
)

# Import the application instance from api.app
from api.app import app  # noqa: E402

# Export the app for uvicorn
__all__ = ['app']


if __name__ == "__main__":
    import uvicorn

    from api.middlewares.security_guard import uvicorn_proxy_kwargs

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        **uvicorn_proxy_kwargs(),
    )
