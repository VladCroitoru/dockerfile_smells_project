################################################################################
# Base image
################################################################################

FROM node:8.1.3
ENV FAUXTON_VERSION=1.1.13

################################################################################
# Build instructions
################################################################################

# Install packages
RUN apt-get update && apt-get install -my \
    supervisor \
    && npm install --no-optional --only=production --quiet --global --no-color fauxton@$FAUXTON_VERSION \
    \
	&& apt-get purge -y --auto-remove \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Add configuration files
COPY docker-entrypoint.sh /
COPY supervisord.conf /etc/supervisor/conf.d/

################################################################################
# Ports
################################################################################

EXPOSE 8000

################################################################################
# Entrypoint
################################################################################

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

