FROM nebo15/alpine-erlang:19.3.1
MAINTAINER Nebo#15 support@nebo15.com

# Configure environment variables and other settings
ENV REFRESHED_AT=2017-04-18 \
    ELIXIR_VERSION=1.4.2

WORKDIR /tmp/elixir-build

# Install Elixir and git
RUN set -xe && \
    ELIXIR_DOWNLOAD_URL="https://github.com/elixir-lang/elixir/archive/v${ELIXIR_VERSION}.tar.gz" && \
    ELIXIR_DOWNLOAD_SHA256="cb4e2ec4d68b3c8b800179b7ae5779e2999aa3375f74bd188d7d6703497f553f" && \
    # Install git
    apk --no-cache --update add git && \
    # Install Elixir build deps
    apk add --no-cache --update --virtual .elixir-build \
      make \
      curl && \
    # Download and validate Elixir checksum
    curl -fSL -o elixir-src.tar.gz "${ELIXIR_DOWNLOAD_URL}" && \
    # echo "${ELIXIR_DOWNLOAD_SHA256} elixir-src.tar.gz" | sha256sum -c - && \
    tar -xzf elixir-src.tar.gz -C /tmp/elixir-build --strip-components=1 && \
    rm elixir-src.tar.gz && \
    # Build Elixir
    make && \
    make install && \
    # Install Hex and Rebar
    mix local.hex --force && \
    mix local.rebar --force && \
    cd /tmp && \
    rm -rf /tmp/elixir-build && \
    # Delete Elixir build deps
    apk del .elixir-build
