FROM ubuntu:14.04
MAINTAINER  Jonas Finnemann Jensen <jopsen@gmail.com>

ENV NODE_VERSION 0.12.4
ENV NPM_VERSION 2.10.1
ENV DOCKER_VERSION 1.6.1

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9 && \
    echo "deb https://get.docker.io/ubuntu docker main" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    lxc-docker-$DOCKER_VERSION \
    lxc \
    iptables

RUN curl -SL "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" | \
    tar xz -C /usr/local --strip-components=1

# Install the dind-service from this folder
COPY        . /opt/dind-service
WORKDIR     /opt/dind-service
RUN         npm install --production \
         && npm cache clear \
         && chmod +x ./entrypoint.sh \
            ;

# Mount volume at /var/lib/docker for AUFS to work
VOLUME      /var/lib/docker

# Expose proxied docker socket on port 2375, if PORT environment variable is
# overwritten with empty string the socket won't be exposed
ENV         PORT                2375
EXPOSE      2375

# Expose proxied docker socket as unix domain socket in a volume, so it can
# be mounted into another container, if SOCKET_PATH environment variable is
# overwritten with empty string the socket won't be exposed
ENV         SOCKET_PATH         /opt/dind-service/run/docker.sock
VOLUME      /opt/dind-service/run

# Pipe log out by default, set it to 'file' to use /var/log/docker.log
# Also configure proxy DEBUG-level, set it to '*' for more informational logs
ENV         LOG                 pipe
ENV         DEBUG               ''

# Warn people against building from this image, that is not the intend. You
# should use this image to setup a docker daemon you can expose.
ONBUILD     echo "If you build from this image you doing something wrong." \
            exit 1;

# Default entry-point starts docker daemon and validating proxy
ENTRYPOINT  ./entrypoint.sh
