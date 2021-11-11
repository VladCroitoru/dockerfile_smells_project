FROM ubuntu:xenial
MAINTAINER Masato Morita <m.morita44@hotmail.com>

# Add the perforce public key
ADD https://package.perforce.com/perforce.pubkey /tmp/perforce.pubkey

# Define valiables
ARG HELIX_VERSION=2017.1-1517929~xenial

# Set environment variables
ENV P4PORT perforce:1666
ENV P4USER swarm
ENV P4PASSWD swarm
ENV HOSTNAME localhost
ENV MXHOST localhost

# Add the perforce apt key
RUN apt-key add /tmp/perforce.pubkey && \
    echo "deb http://package.perforce.com/apt/ubuntu $(sed -n 's/^DISTRIB_CODENAME=\(.*\)$/\1/p' /etc/lsb-release) release" > /etc/apt/sources.list.d/perforce.list && \
    rm /tmp/*

# Install the helix swarm packages and dependent package
RUN apt-get update && \
    apt-get install -y wget helix-swarm=$HELIX_VERSION helix-swarm-triggers=$HELIX_VERSION

# Expose HTTP and HTTPS port
EXPOSE 80 443

# Add a startup file
ADD ./run.sh /

# Run the file
CMD ["/run.sh"]
