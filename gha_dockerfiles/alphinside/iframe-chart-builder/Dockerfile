FROM python:3.8-slim as builder-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    POETRY_VERSION=1.1.10
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./

RUN apt-get update && apt-get install --no-install-recommends -y git curl build-essential && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - && \
    chmod a+x /opt/poetry/bin/poetry && \
    /opt/poetry/bin/poetry install --no-dev -vv

FROM python:3.8-slim as runtime
ENV PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY --from=builder-base $PYSETUP_PATH/pyproject.toml pyproject.toml
COPY ./app /app

ENV PORT=8080
EXPOSE $PORT
RUN set -e && . /opt/pysetup/.venv/bin/activate
ENTRYPOINT /opt/pysetup/.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port $PORT