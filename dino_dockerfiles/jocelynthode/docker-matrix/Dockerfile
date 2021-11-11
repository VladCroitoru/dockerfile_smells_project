FROM debian:stretch-slim

## enable HTTPS repositories
RUN apt-get update -qq \
    && apt-get install -yq apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

## setup repository
RUN echo 'deb https://packages.matrix.org/debian/ stretch main' \
        > /etc/apt/sources.list.d/matrix.list
COPY adds/matrix-org-archive-keyring.gpg /etc/apt/trusted.gpg.d/

## install latest version of matrix
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -qq \
    && apt-get install -yq --no-install-recommends \
        matrix-synapse-py3 \
        ## Suggested deps for email notifications \
        # python-bleach python-jinja2 \
    && rm -rf /var/lib/apt/lists/*
RUN dpkg-query --show -f '${Version}' matrix-synapse-py3 >/synapse.version

## user configuration
ENV MATRIX_UID=991 MATRIX_GID=991
RUN groupadd -r -g $MATRIX_GID matrix \
	&& useradd -r -d /data -M -u $MATRIX_UID -g matrix matrix

## startup configuration
COPY adds/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/opt/venvs/matrix-synapse/bin/python", "-m", "synapse.app.homeserver", "-c", "/data/conf/matrix-server.yaml"]
USER matrix
EXPOSE 8448
VOLUME ["/data"]
