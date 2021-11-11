# Dockerfile for BIND9

FROM debian:wheezy

MAINTAINER Calum Hunter <calum.h@gmail.com>

# Set Environmental variables
ENV DEBIAN_FRONTEND noninteractive

# Install required packages, then do a clean up
RUN apt-get update && \
	apt-get -y install \
	bind9 \
	bind9utils \
	dnsutils \
	curl \
	nano && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /etc/bind/*

# Setup directories and permissions for bind
RUN mkdir -p /etc/bind/zones/hint && \
	mkdir -p /etc/bind/zones/master && \
	mkdir -p /var/log/bind && chown bind:bind /var/log/bind && \
	mkdir -p /var/bind && chown bind:bind /var/bind && \
	mkdir -p /var/run/bind && chown bind:bind /var/run/bind

# Add our startup script
ADD start.sh /start.sh
RUN chmod 755 /start.sh

# Expose the bind folder as a volumes
VOLUME /etc/bind

# Expose the DNS port
EXPOSE 53

# Run our startup script
CMD ["/start.sh"]


