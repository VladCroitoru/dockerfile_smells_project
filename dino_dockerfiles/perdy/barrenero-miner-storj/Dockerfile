FROM node:boron-alpine
LABEL maintainer="José Antonio Perdiguero López <perdy@perdy.io>"

ENV APP=barrenero-miner-storj

# Install system dependencies
ENV RUNTIME_PACKAGES python3
ENV BUILD_PACKAGES build-base openssl-dev python git
RUN apk --no-cache add $RUNTIME_PACKAGES

# Create project dirs
RUN mkdir -p /srv/apps/$APP/logs
RUN mkdir -p /srv/apps/$APP/storage
WORKDIR /srv/apps/$APP

# Install Storj and python requirements
COPY Pipfile Pipfile.lock /srv/apps/$APP/
RUN apk --no-cache add $BUILD_PACKAGES && \
    npm install --global storjshare-daemon && \
    npm cache clean --force && \
    python3 -m pip install --no-cache-dir --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile && \
    rm -rf \
        $HOME/.cache/pip/* \
        /tmp/npm* && \
    apk del $BUILD_PACKAGES

# Copy application
COPY . /srv/apps/$APP/

ENTRYPOINT ["./run"]
