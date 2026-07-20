#!/bin/sh
echo "Running migrations ... "
# alembic revision --autogenerate -m "initial"
alembic upgrade head

echo "Starting Gunicorn..."
exec gunicorn server.app.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000