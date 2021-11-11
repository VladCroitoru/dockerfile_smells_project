FROM python:3.9 AS builder
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.6 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$VENV_PATH/bin:$PATH"
RUN pip install poetry==$POETRY_VERSION
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

FROM node:14-bullseye AS builder-node
ENV NPMSETUP_PATH="/opt/npmsetup"
WORKDIR $NPMSETUP_PATH
COPY cobrand_hackney/package.json cobrand_hackney/package-lock.json ./
RUN npm install

FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    NPMSETUP_PATH="/opt/npmsetup" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$VENV_PATH/bin:$PATH"
RUN apt-get update && apt-get install -y \
    binutils gdal-bin libproj-dev git \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /app
COPY --from=builder-node $NPMSETUP_PATH cobrand_hackney/
COPY . .
#RUN ./manage.py collectstatic --no-input
