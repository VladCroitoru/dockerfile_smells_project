FROM elixir:1.11-alpine as build

# Install deps
RUN set -xe; \
    apk add --update  --no-cache --virtual .build-deps \
        ca-certificates \
        g++ \
        gcc \
        git \
        make \
        musl-dev \
        python3 \
        tzdata;

# Use the standard /usr/local/src destination
RUN mkdir -p /usr/local/src/assembly

COPY . /usr/local/src/assembly/

# ARG is available during the build and not in the final container
# https://vsupalov.com/docker-arg-vs-env/
ARG MIX_ENV=prod
ARG APP_NAME=assembly

# Use `set -xe;` to enable debugging and exit on error
# More verbose but that is often beneficial for builds
RUN set -xe; \
    cd /usr/local/src/assembly/; \
    mix local.hex --force; \
    mix local.rebar --force; \
    mix deps.get; \
    mix deps.compile --all; \
    mix release

FROM alpine:3.9 as release

RUN set -xe; \
    apk add --update  --no-cache --virtual .runtime-deps \
        ca-certificates \
        libmcrypt \
        ncurses-libs \
        tzdata;

# Create a `assembly` group & user
# I've been told before it's generally a good practice to reserve ids < 1000 for the system
RUN set -xe; \
    addgroup -g 1000 -S assembly; \
    adduser -u 1000 -S -h /assembly -s /bin/sh -G assembly assembly;

ARG APP_NAME=assembly

# Copy the release artifact and set `assembly` ownership
COPY --chown=assembly:assembly --from=build /usr/local/src/assembly/_build/prod/rel/${APP_NAME} /assembly

# These are fed in from the build script
ARG VCS_REF
ARG BUILD_DATE
ARG VERSION

# `Maintainer` has been deprecated in favor of Labels / Metadata
# https://docs.docker.com/engine/reference/builder/#maintainer-deprecated
LABEL \
    org.opencontainers.image.created="${BUILD_DATE}" \
    org.opencontainers.image.description="assembly" \
    org.opencontainers.image.revision="${VCS_REF}" \
    org.opencontainers.image.source="https://github.com/system76/assembly" \
    org.opencontainers.image.title="assembly" \
    org.opencontainers.image.vendor="system76" \
    org.opencontainers.image.version="${VERSION}"

ENV \
    PATH="/usr/local/bin:$PATH" \
    VERSION="${VERSION}" \
    APP_REVISION="${VERSION}" \
    MIX_APP="assembly" \
    MIX_ENV="prod" \
    SHELL="/bin/bash"

# Drop down to our unprivileged `assembly` user
USER assembly

WORKDIR /assembly

EXPOSE 50051

ENTRYPOINT ["/assembly/bin/assembly"]

CMD ["start"]
