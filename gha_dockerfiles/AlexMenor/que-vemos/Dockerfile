FROM python:3.8-slim AS base

LABEL version="1.0" maintainer="Alejandro Menor <alex4menor@gmail.com>"

FROM base AS builder

RUN apt update && \
    apt install -y --no-install-recommends build-essential

RUN pip install poetry

RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --dev | /venv/bin/pip install -r /dev/stdin

FROM base AS final

RUN apt update && apt install make -y --no-install-recommends

RUN groupadd -r tests && useradd --no-log-init -r -g tests tests

USER tests

ENV PATH="/venv/bin:$PATH"

ARG NUM_OF_WATCHABLES_PER_SESSION=20
ARG MAX_USERS_PER_SESSION=8
ARG MODE=dev
ENV NUM_OF_WATCHABLES_PER_SESSION=$NUM_OF_WATCHABLES_PER_SESSION
ENV MAX_USERS_PER_SESSION=$MAX_USERS_PER_SESSION
ENV MODE=$MODE

COPY --from=builder /venv /venv

WORKDIR /test
VOLUME /test

CMD ["python", "-m", "pytest"]