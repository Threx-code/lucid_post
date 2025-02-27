ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

LABEL authors="oluwatosin"

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PATH="/root/.local/bin:${PATH}"

# Install all dependencies
RUN apt-get update && apt-get install -y \
    # MySQL development libraries
    default-libmysqlclient-dev \
    default-mysql-client \
    libssl-dev \
    build-essential \
    pkg-config \
    python3-dev \
    gcc \
    make \
    # For Pillow
    libjpeg-dev \
    # For CairoSVG
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /src

# Create the virtual environment
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip before installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./src /src
COPY .env .env

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

ARG DEBUG=0
ENV DEBUG=${DEBUG}

EXPOSE 8000

## Run the Django app with Gunicorn for production readiness
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.wsgi:application"]
