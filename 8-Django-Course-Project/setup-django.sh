#!/usr/bin/env bash
# Stop execution if anything fails
set -e

# # Wait for the DB to be ready (Postgres might still be waking up)
# echo "Checking database connection..."
# ./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up!"

# Apply migrations (The image HAS the new migration files inside it!)
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Start the actual web server
echo "Starting web server..."
exec "$@"  # executes whatever CMD (or runtime override)
