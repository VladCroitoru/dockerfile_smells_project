##### Stage 1 #####
FROM python:3.8 AS builder

ENV APP_ROOT_DIR="/opt/trader"
RUN mkdir -p $APP_ROOT_DIR
WORKDIR $APP_ROOT_DIR

# poetry env vars
ENV POETRY_NO_INTERACTION=1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Update path with poetry executables
ENV PATH "${POETRY_HOME}/bin:${APP_ROOT_DIR}/.venv/bin:${PATH}"

# install deps in specific folder so they can be copied
COPY ./pyproject.toml ./poetry.lock ${APP_ROOT_DIR}/
RUN poetry install --no-dev

############### Stage 2  ####################
FROM builder as execution

# add non-root user and give access to source code.
RUN groupadd -r trader \
    && useradd -r -s /bin/false -g trader trader

WORKDIR ${APP_ROOT_DIR}

COPY --from=builder --chown=trader:trader ${POETRY_HOME} ${POETRY_HOME}
COPY --from=builder --chown=trader:trader ${APP_ROOT_DIR}/.venv ${APP_ROOT_DIR}/.venv

COPY --chown=trader:trader ./app ./app
COPY --chown=trader:trader ./scripts/start.sh ./start.sh

USER trader
ENV RUNTIME_MODE "docker"
ENV TZ "US/Pacific"

# ENV RUN_GUNICORN true
EXPOSE 5000
ENTRYPOINT ["/opt/trader/start.sh", "5000"]
