FROM nvidia/cuda:9.1-base
LABEL maintainer="José Antonio Perdiguero López <perdy@perdy.io>"

ENV APP=barrenero-api
ENV LC_ALL='C.UTF-8' PYTHONIOENCODING='utf-8'

# Install system dependencies
ENV RUNTIME_PACKAGES sqlite git docker python3.6 python3-pip docker-ce
ENV BUILD_PACKAGES build-essential libsqlite3-dev python3.6-dev
RUN apt-get update -m && \
    apt-get install -y --no-install-recommends software-properties-common curl && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y --no-install-recommends $RUNTIME_PACKAGES && \
    apt-get remove --purge -y software-properties-common curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
        /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin

# Create project dirs
RUN mkdir -p /srv/apps/$APP/logs
WORKDIR /srv/apps/$APP

## Install ethminer and python requirements
COPY Pipfile Pipfile.lock /srv/apps/$APP/
RUN apt-get update -m && \
    apt-get install -y --no-install-recommends $BUILD_PACKAGES && \
    python3.6 -m pip install --no-cache-dir --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile && \
    apt-get remove --purge -y $BUILD_PACKAGES && \
    apt-get clean && \
    rm -rf /tmp/* \
        /var/tmp/* \
        /var/lib/apt/lists/* \
        /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin \
        $HOME/.cache/pip/*

# Copy application
COPY . /srv/apps/$APP/

ENTRYPOINT ["./run"]
