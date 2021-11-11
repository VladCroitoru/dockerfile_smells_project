# Elastalert Docker image running on Alpine Linux.
# Build image with: docker build -t ivankrizsan/elastalert:latest .
#
# The WORKDIR instructions are deliberately left, as it is recommended to use WORKDIR over the cd command.

FROM elasticsearch:2.3.1

MAINTAINER Jailbirt

#Where elasticsearch is Installed.
WORKDIR /usr/share/elasticsearch

#Would be overriden by docker-compose
VOLUME /usr/share/elasticsearch/data

# Set this environment variable to true to set timezone on container start.
ENV SET_CONTAINER_TIMEZONE false
# Default container timezone as found under the directory /usr/share/zoneinfo/.
ENV CONTAINER_TIMEZONE America/Buenos_Aires
# Launch Elasticsearch
RUN /usr/sbin/service elasticsearch start

# Install plugins, ssl is required but we are not planning to use it.
RUN bin/plugin install mobz/elasticsearch-head
RUN bin/plugin install delete-by-query
