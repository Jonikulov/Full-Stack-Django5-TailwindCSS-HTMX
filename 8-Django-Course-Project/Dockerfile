FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

RUN apt update
RUN apt install gettext -y

# # Tell uv to use the container's native Python and stop downloading
# ENV UV_PYTHON_PREFERENCE=only-system
# # Forbid uv from ever downloading Python at runtime
# ENV UV_PYTHON_DOWNLOADS=never
# Put the virtual environment in /opt/venv instead of /code/.venv
ENV UV_PROJECT_ENVIRONMENT=/opt/venv

# Set recommended uv environment variables for Docker
ENV UV_COMPILE_BYTECODE=1
# Tell uv to copy files instead of using hardlinks (better for Docker layers)
ENV UV_LINK_MODE=copy 

# Install uv using the official multi-stage build method
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir /code
WORKDIR /code
COPY pyproject.toml uv.lock ./
# Install dependencies without the project itself 
RUN uv sync --frozen --no-install-project --no-default-groups
# Copy the rest of your application code
COPY . .

# # Add the virtual environment to the system PATH
# # This eliminates the need to use `uv run` or activate the venv
# ENV PATH="/opt/venv/bin:$PATH"

RUN chmod 755 /code/start-django.sh

EXPOSE 8000
# Run the application using uv run
ENTRYPOINT [ "/code/start-django.sh" ]
