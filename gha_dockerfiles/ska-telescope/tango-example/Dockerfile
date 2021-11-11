ARG BUILD_IMAGE="artefact.skao.int/ska-tango-images-pytango-builder:9.3.14"
ARG BASE_IMAGE="artefact.skao.int/ska-tango-images-pytango-runtime:9.3.14"
FROM $BUILD_IMAGE AS buildenv

FROM $BASE_IMAGE

# Install Poetry
USER root
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python - && \
    cd /usr/local/bin && \
    chmod a+x /opt/poetry/bin/poetry && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock* ./

# Install runtime dependencies and the app
RUN poetry install --no-dev

USER tango

RUN poetry config virtualenvs.create false

# create ipython profile too so that itango doesn't fail if ipython hasn't run yet
RUN ipython profile create
