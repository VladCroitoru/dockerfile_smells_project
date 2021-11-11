# Pull base image.
FROM debian:latest

MAINTAINER Fabio Napoleoni <f.napoleoni@gmail.com>

# Define rancher compose version
ENV RANCHER_CLI_VERSION v0.6.2

# Download and install rancher compose at specified version
RUN apt-get -yqq update && \
		apt-get install -yqq --no-install-recommends ca-certificates wget && \
		wget -qO- https://github.com/rancher/cli/releases/download/${RANCHER_CLI_VERSION}/rancher-linux-amd64-${RANCHER_CLI_VERSION}.tar.gz | tar xvz -C /tmp && \
		mv /tmp/rancher-${RANCHER_CLI_VERSION}/rancher /usr/local/bin/rancher && \
		chmod +x /usr/local/bin/rancher

# Cleanup image
RUN apt-get -yqq autoremove && \
		apt-get -yqq clean && \
		rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*

# Define working directory.
WORKDIR /workspace
