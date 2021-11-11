# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ENV PYTHONUNBUFFERED 1

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

RUN apt-get update && apt-get install gnupg2 -y --no-install-recommends

ARG USERNAME="vscode"

# Persist command history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && echo $SNIPPET >> "/root/.bashrc"

# Setup Python project
ARG POETRY_VERTION="1.1.10"
RUN pip3 install poetry==${POETRY_VERTION} pre-commit
COPY wxsls-pyfn/poetry.lock wxsls-pyfn/pyproject.toml /workspace/wxsls-pyfn/
RUN cd /workspace/wxsls-pyfn/ && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Setup JavaScript project
COPY wxsls-page/package.json wxsls-page/package-lock.json /workspace/wxsls-page/
RUN cd /workspace/wxsls-page/ && npm ci --unsafe-perm=true

WORKDIR /workspace
COPY docker-entrypoint.sh /
ENTRYPOINT [ "sh", "/docker-entrypoint.sh" ]
CMD [ "sleep", "infinity" ]
