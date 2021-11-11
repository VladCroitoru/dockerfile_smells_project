FROM python:3-alpine

ARG BUILD_DATE=now
ARG VCS_REF=working-copy
ARG VERSION=latest

LABEL \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.authors="gissehel" \
      org.opencontainers.image.url="https://github.com/gissehel/dikki" \
      org.opencontainers.image.source="https://github.com/gissehel/dikki" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.vendor="gissehel" \
      org.opencontainers.image.ref.name="ghcr.io/gissehel/dikki" \
      org.opencontainers.image.title="dikki" \
      org.opencontainers.image.description="Image for dikki" \
      org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.name="dikki" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.vendor="gissehel" \
      org.label-schema.vcs-url="https://github.com/gissehel/dikki" \
      org.label-schema.schema-version="1.0" \
      maintainer="Gissehel <public-maintainer-docker-dikki@gissehel.org>"

RUN \
    mkdir -p /app/dikkilib
COPY ./dikki.py ./requirements.txt /app/
COPY dikkilib /app/dikkilib
RUN \
    cd /app/ && \
    pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "/app/dikki.py" ]

