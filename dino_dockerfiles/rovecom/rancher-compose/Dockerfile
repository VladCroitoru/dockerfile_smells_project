FROM debian:latest

MAINTAINER Erwin Steffens <esteffens@rovecom.nl>

ENV RANCHER_COMPOSE_VERSION 0.12.5

# Install certificates and wget
RUN apt-get -yqq update && \
		apt-get install -yqq --no-install-recommends ca-certificates wget

# Download and install rancher compose
RUN wget -qO- https://github.com/rancher/rancher-compose/releases/download/v${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz | tar xvz -C /tmp && \
		mv /tmp/rancher-compose-v${RANCHER_COMPOSE_VERSION}/rancher-compose /usr/local/bin/rancher-compose && \
		chmod +x /usr/local/bin/rancher-compose

# Install needed packages
RUN apt-get install -y gettext-base

# Cleanup 
RUN apt-get -yqq autoremove && \
		apt-get -yqq clean && \
		rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*

# Setup working dir 
RUN mkdir /app
WORKDIR /app

# Set entrypoint
CMD ["/usr/local/bin/rancher-compose", "--version"]
