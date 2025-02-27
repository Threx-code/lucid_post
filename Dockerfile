ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

LABEL authors="oluwatosin"

#Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PATH="/root/.local/bin:${PATH}"


#Install all dependencies
RUN apt-get update && apt-get install -y \
    #for mysql
    default-libmysqlclient-dev \
    #for pillow
    libjpeg-dev \
    # for cairoSVG
    libcairo2 \
    gcc \
    make \
    && rm -rf /var/lib/apt/lists/*


# Set environment variables
ENV MYSQLCLIENT_CFLAGS="$(mysql_config --cflags)"
ENV MYSQLCLIENT_LDFLAGS="$(mysql_config --libs)"

#Set the working directory
RUN mkdir -p /src
WORKDIR /src

# create the virtual environment
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY ./src /src
COPY .env .env


ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

ARG DEBUG=0
ENV DEBUG=${DEBUG}

ARG PROJECT_NAME="ai-agent"

EXPOSE 8000

## Run the Django app with Gunicorn for production readiness
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.wsgi:application"]

