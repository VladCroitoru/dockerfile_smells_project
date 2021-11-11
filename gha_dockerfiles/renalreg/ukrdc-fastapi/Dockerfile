FROM python:3.9-slim

ARG GITHUB_SHA
ARG GITHUB_REF
ARG SENTRY_DSN

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.1.11 \
    GITHUB_SHA=$GITHUB_SHA \
    GITHUB_REF=$GITHUB_REF \
    SENTRY_DSN=$SENTRY_DSN

WORKDIR /app

RUN python -m pip install -U pip==21.0.1 && pip install poetry

COPY . ./

RUN poetry install --no-dev --no-interaction

CMD ["poetry", "run", "uvicorn", "ukrdc_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
