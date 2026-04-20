FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# RUN apt update && apt install gettext -y

# # Tell uv to use the container's native Python and stop downloading
# ENV UV_PYTHON_PREFERENCE=only-system
# # Forbid uv from ever downloading Python at runtime
# ENV UV_PYTHON_DOWNLOADS=never
# # Put the virtual environment in /opt/venv instead of /app/.venv
# ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Omit development dependencies
ENV UV_NO_DEV=1

# Install uv using the official multi-stage build method
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock ./
# Install dependencies without the project itself 
RUN uv sync --locked --frozen --no-cache --no-install-project --no-default-groups
# Copy the rest of your application code
COPY . /app

# # Add the virtual environment to the system PATH
# # This eliminates the need to use `uv run` or activate the venv
# ENV PATH="/opt/venv/bin:$PATH"
# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

RUN chmod 755 /app/start-django.sh

EXPOSE 8000
# Run the application using uv run
ENTRYPOINT [ "/app/start-django.sh" ]
