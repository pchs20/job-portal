#! /usr/bin/env bash

echo "Running prestart.sh"

# Run migrations
if [ "$DOMAIN" = "localhost" ]; then
  echo "Running alembic"
  alembic upgrade head
fi

# Create initial data in DB
if [ "$DOMAIN" = "localhost" ]; then
  echo "Running init_db.py"
  python /graphene_start/app/database/init_db.py
fi

# Run webserver
echo "Running uvicorn"
if [ "$DOMAIN" = "localhost" ]; then
  # Local
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
  # Production
  uvicorn app.main:app --host 0.0.0.0 --port 8000
fi

echo "Finished prestart.sh"
