#!/usr/bin/env bash
# Stop execution if anything fails
set -e

# Wait for the DB to be ready (Postgres might still be waking up)
echo "Checking database connection..."
./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up!"

# Apply migrations (The image HAS the new migration files inside it!)
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Start the actual web server
echo "Starting Gunicorn server..."
# exec gunicorn src.myproject.wsgi:application \
#     --bind 0.0.0.0:8000 \
#     --workers 4 \
#     --access-logfile - \
#     --error-logfile -

exec "$@"  # executes whatever CMD is (or override at runtime)
