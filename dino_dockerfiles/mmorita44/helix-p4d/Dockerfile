FROM ubuntu:xenial
MAINTAINER Masato Morita <m.morita44@hotmail.com>

# Add the perforce public key
ADD https://package.perforce.com/perforce.pubkey /tmp/perforce.pubkey

# Define valiables
ARG HELIX_VERSION=2017.1-1534792~xenial

# Set environment variables
ENV SERVER_NAME perforce 
ENV P4PORT 1666
ENV P4USER p4admin
ENV P4PASSWD p4admin@123

# Add the perforce apt key
RUN apt-key add /tmp/perforce.pubkey && \
    echo "deb http://package.perforce.com/apt/ubuntu $(sed -n 's/^DISTRIB_CODENAME=\(.*\)$/\1/p' /etc/lsb-release) release" > /etc/apt/sources.list.d/perforce.list && \
    rm /tmp/*

# Install the perforce server and dependent packages
RUN apt-get update && \
    apt-get install -y net-tools helix-p4d=${HELIX_VERSION}

# Expose default p4d connector port
EXPOSE 1666 

# Set volume mount point for server roots and triggers and configuration
VOLUME /opt/perforce/servers
VOLUME /opt/perforce/triggers
VOLUME /etc/perforce

# Add a startup file
ADD ./run.sh /

# Run the file
CMD ["/run.sh"]
