FROM python:3.13-slim-trixie

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext && rm -rf /var/lib/apt/lists/*
# Install uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    # Set uv to use the container's native Python and stop downloading
    UV_PYTHON_PREFERENCE=only-system \
    # Forbid uv from ever downloading Python at runtime
    UV_PYTHON_DOWNLOADS=never \
    # Enable bytecode compilation
    UV_COMPILE_BYTECODE=1 \
    # Copy from the cache instead of linking
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./
# Install dependencies without the project itself 
RUN --mount=type=cache,target=/root/.cache/uv \
    # uv sync --locked --no-default-groups --no-install-project
    uv sync --locked --no-install-project

# Copy the rest of the code
COPY . /app
# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    # uv sync --locked --no-default-groups
    uv sync --locked

# Place the venv at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Ensure script is executable
RUN chmod +x /app/start-django.sh

# Setup a non-root user
RUN groupadd --system --gid 999 django \
    && useradd --system --gid 999 --uid 999 --create-home django
USER django

EXPOSE 8000
# Use the venv's python directly via the PATH we set
ENTRYPOINT [ "/app/start-django.sh" ]
# CMD ["python", "manage.py", "runserver", "8000"]
