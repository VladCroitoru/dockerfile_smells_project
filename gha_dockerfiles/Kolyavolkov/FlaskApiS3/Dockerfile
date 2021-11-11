FROM python:3.8-slim as base
ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT
LABEL maintaner="Volkov Nikolai"
ENV POETRY_VERSION=1.1.10 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM base as poetry
RUN apt-get update && apt-get install -y build-essential curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-dev

# FROM poetry as tests
# WORKDIR $PYSETUP_PATH
# RUN poetry install
# WORKDIR /app
# COPY . .
# RUN make lint && make test


FROM base as artifact
RUN apt-get update; apt-get install -y curl
COPY --from=poetry $POETRY_HOME $POETRY_HOME
COPY --from=poetry $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /app
COPY . .
ENV FLASK_APP=restapi
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1:5000/health || exit 1
EXPOSE 5000

