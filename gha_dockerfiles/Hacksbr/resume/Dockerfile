FROM python:3.9.7-slim-buster

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    # python
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    POETRY_VERSION=1.1.11 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin"

# system deps
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl git mercurial \
        # deps for building python deps
        build-essential \
        # cleaning cache
        && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
        # installing `poetry` package manager
        && curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
        && poetry --version

# copy only requirements, to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# project initialization
RUN echo "$DJANGO_ENV" \
  && poetry install \
    $(if [ "$DJANGO_ENV" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction --no-ansi \
  # cleaning poetry installation's cache for production
  && if [ "$DJANGO_ENV" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x '/docker-entrypoint.sh'

CMD ["/docker-entrypoint.sh"]
