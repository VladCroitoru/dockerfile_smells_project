#
# Dockerfile
#
# Copyright (c) 2015-2017 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
FROM alpine:latest
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

# Install relative packages.
ENV TERM vt100
RUN apk -U add bash openssh socat && rm -rf /var/cache/apk/*

# For sshd in server.
RUN mkdir /var/run/sshd
RUN echo "Protocol 2" >> /etc/ssh/sshd_config && \
		echo "PasswordAuthentication no" >> /etc/ssh/sshd_config && \
		echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config && \
		echo "HostKey /etc/ssh/ssh_host_rsa_key" >> /etc/ssh/sshd_config

# IP address to connect (used in tunnel).
ENV HOST 127.0.0.1

# User of AmbassadorS.
ENV USER tunnel

# Public port number of server.
ENV PORT 10022

# Port number of Socks proxy.
ENV PROXY_PORT 1080

EXPOSE 22
EXPOSE 1080

# Import and set the startup script.
ADD ./bin/entrypoint.sh /root/
ENTRYPOINT ["/root/entrypoint.sh"]
