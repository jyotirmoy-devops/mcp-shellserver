# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        git \
        gcc \
        libffi-dev \
        libssl-dev \
        && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

# Install helm
RUN curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install uv using pip
RUN pip install --no-cache-dir uv

# Set workdir
WORKDIR /app

# Copy pyproject.toml and source code
COPY pyproject.toml /app/
COPY . /app

# Create a uv virtual environment, install dependencies from pyproject.toml, and sync using global uv
RUN uv venv .venv && \
    uv pip install -r pyproject.toml && \
    uv sync

# Expose port (adjust if needed)
EXPOSE 8000

# Set entrypoint to use uv run
CMD ["uv", "run", "server.py"] 