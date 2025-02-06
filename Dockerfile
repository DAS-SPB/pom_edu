# Dockerfile (nly for test project)

FROM python:3.12.1-slim

# Instal necessary utilities (curl, git, ...)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry (using pip)
RUN pip install --upgrade pip && \
    pip install poetry

# Create directory for project
WORKDIR /app

# Copy files for Poetry
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy all the other things
COPY . /app

# bash for default
CMD ["bash"]
