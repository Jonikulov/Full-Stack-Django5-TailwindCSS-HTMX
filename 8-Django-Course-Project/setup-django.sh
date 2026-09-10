#!/usr/bin/env bash
# Stop execution if anything fails
set -e

# # Wait for the DB to be ready (Postgres might still be waking up)
# echo "Checking database connection..."
# ./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Database is up!"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Apply migrations (The image HAS the new migration files inside it!)
echo "Running migrations..."
python manage.py migrate --noinput

# Start the actual web server
echo "Starting web server..."

case "$ENV_STATE" in
    prod)
        exec gunicorn django_blog_project.wsgi:application \
            --bind 0.0.0.0:8000 \
            --workers "$GUNICORN_WORKERS" \
            --forwarded-allow-ips "*"
        ;;
    dev)
        exec python manage.py runserver 0.0.0.0:8000
        ;;
    *)
        echo "FATAL: ENV_STATE must be 'prod' or 'dev' — got '${ENV_STATE:-<unset>}'. Check that .env exists and is loaded." >&2
        exit 1
        ;;
esac

exec "$@"  # executes whatever CMD (or runtime override)
