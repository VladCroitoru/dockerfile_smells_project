FROM python:alpine
LABEL maintainer="José Antonio Perdiguero López <perdy@perdy.io>"

ENV APP=barrenero-telegram

# Install system dependencies
ENV RUNTIME_PACKAGES sqlite-libs
ENV BUILD_PACKAGES build-base linux-headers
RUN apk --no-cache add $RUNTIME_PACKAGES

# Create project dirs
RUN mkdir -p /srv/apps/$APP/logs
WORKDIR /srv/apps/$APP

# Install pip requirements
COPY Pipfile Pipfile.lock /srv/apps/$APP/
RUN apk --no-cache add $BUILD_PACKAGES && \
    python -m pip install --no-cache-dir --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile && \
    rm -rf $HOME/.cache/pip/* && \
    apk del $BUILD_PACKAGES

# Copy application
COPY . /srv/apps/$APP/

ENTRYPOINT ["./__main__.py"]
