FROM debian:latest
ENV UPDATED_AT="2021-10-01T17:46:41"
RUN apt-get update && \
    apt-get -yq install --no-install-recommends curl ca-certificates git && \
    curl -sL https://sentry.io/get-cli/ | bash

