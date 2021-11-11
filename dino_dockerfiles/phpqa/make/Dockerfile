# Set defaults

ARG BASE_IMAGE="docker:18.09"
ARG TOOL_NAME="make"
ARG REPOSITORY_NAME="phpqa/make"
ARG VERSION="4.2.1"

# Build image

FROM ${BASE_IMAGE}
ARG TOOL_NAME
ARG REPOSITORY_NAME
ARG VERSION
ARG BUILD_DATE
ARG VCS_REF
ARG IMAGE_NAME

# Install Tini - https://github.com/krallin/tini

RUN apk add --no-cache tini

# Install GNU Make - https://pkgs.alpinelinux.org/package/edge/main/x86/make

RUN apk add --no-cache "${TOOL_NAME}=~${VERSION}"

# Add entrypoint script

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Add image labels

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.vendor="phpqa" \
      org.label-schema.name="${REPOSITORY_NAME}" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.url="https://github.com/${REPOSITORY_NAME}" \
      org.label-schema.usage="https://github.com/${REPOSITORY_NAME}/README.md" \
      org.label-schema.vcs-url="https://github.com/${REPOSITORY_NAME}.git" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.docker.cmd="docker run --rm --volume \${PWD}:/app --workdir /app ${IMAGE_NAME}"

# Package container

WORKDIR "/app"
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["make"]
