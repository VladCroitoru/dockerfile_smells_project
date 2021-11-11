FROM registry:2

LABEL org.opencontainers.image.source="https://github.com/lorislab/dev-registry"

# Install supervisor and docker for the proxy
RUN apk add --update docker openrc supervisor && \
    rc-update add docker boot && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /etc/supervisor/conf.d

# Switch default docker registry to 5002 port
ENV REGISTRY_HTTP_ADDR=localhost:5002

# Enabled delete images
ENV REGISTRY_STORAGE_DELETE_ENABLED=true

COPY dev-registry /usr/local/bin/dev-registry

# Disable default entrypoint
ENTRYPOINT []

# Add supervisor configuration to run two services
ADD supervisor.conf /etc/supervisor.conf
CMD ["supervisord", "-c", "/etc/supervisor.conf"]
