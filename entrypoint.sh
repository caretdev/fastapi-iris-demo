#!/bin/sh

alembic upgrade head

uvicorn app.main:app \
      --workers 1 \
      --host 0.0.0.0 \
      --port 8000 "$@"