FROM joyzoursky/python-chromedriver:3.9

ARG BUILD_ENV

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

RUN pip install poetry
WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install $(if [ "$BUILD_ENV" = 'prod' ]; then echo '--no-dev'; fi) \
    --no-root --no-interaction --no-ansi

COPY . /app

EXPOSE 8080

ENV PORT=8080

CMD exec functions-framework --target=main
