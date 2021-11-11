FROM ubuntu:20.04 AS base

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install --yes --no-install-recommends python3-pip binutils && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /app


COPY requirements-pipenv.txt /tmp/
RUN python3 -m pip install --disable-pip-version-check --no-cache-dir --requirement=/tmp/requirements-pipenv.txt && \
    rm --recursive --force /tmp/*

COPY Pipfile Pipfile.lock ./
RUN pipenv sync --system --clear && \
    rm --recursive --force /usr/local/lib/python3.*/dist-packages/tests/ /tmp/* /root/.cache/*


FROM base AS checker

RUN \
    pipenv sync --system --clear --dev && \
    rm --recursive --force /tmp/* /root/.cache/*


FROM base AS run

RUN \
    . /etc/os-release && \
    apt-get update && \
    apt-get --assume-yes upgrade && \
    apt-get install --assume-yes apt-transport-https gnupg curl && \
    echo "deb https://deb.nodesource.com/node_16.x ${VERSION_CODENAME} main" > /etc/apt/sources.list.d/nodesource.list && \
    curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    apt-get update && \
    apt-get install --assume-yes --no-install-recommends nodejs && \
    apt-get clean && \
    rm --recursive --force /var/lib/apt/lists/*

RUN python3 -m compileall -q \
    -x '/usr/local/lib/python3.*/site-packages/pipenv/' -- *

COPY . ./
RUN (cd c2cciutils; npm install) && \
    python3 -m pip install --disable-pip-version-check --no-deps --no-cache-dir --no-deps --editable=. && \
    python3 -m compileall -q /app/c2cciutils
