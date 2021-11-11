# Pull base image.
FROM ubuntu:14.04

# Disable prompts
ENV DEBIAN_FRONTEND noninteractive

# Reset policy-rc.d
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d
RUN chmod +x /usr/sbin/policy-rc.d

# Install Python
RUN \
  apt-get update && \
    apt-get install -y curl python python-dev python-pip python-virtualenv openssh-server && \
      apt-get install -y python-prettytable python-yaml && \
        rm -rf /var/lib/apt/lists/*

# Set environment variable to Docker
ENV CONTAINER DOCKER

RUN cd /root && curl -sS -k -O https://ops.stackstorm.net/releases/st2/scripts/st2_deploy.sh

RUN bash -c 'chmod +x /root/st2_deploy.sh'

RUN bash -c '/root/st2_deploy.sh stable || exit 2'

ADD . /root/st2/

RUN bash -c 'chmod +x /root/st2/start.sh'

# auth service
EXPOSE 9100
# api server
EXPOSE 9101
# webui
EXPOSE 8080
