#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status

# 1. Wait for the DB to be ready (Postgres might still be waking up)
echo "Checking database connection..."
./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up!"

# 2. Apply migrations (The image HAS the new migration files inside it!)
echo "Running migrations..."
python manage.py migrate --noinput

# 3. Collect static files
echo "Collecting static files..."
python src/manage.py collectstatic --noinput --clear

# 4. Start the actual web server
echo "Starting Gunicorn server..."
exec gunicorn src.myproject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --acess-logfile - \
    --error-logfile -

# exec "$@"
