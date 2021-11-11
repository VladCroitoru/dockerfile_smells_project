###############################################
# Ubuntu with added Teamspeak 3 Server. 
# Uses SQLite Database on default.
###############################################

# Using latest Ubuntu image as base
FROM ubuntu:16.04
MAINTAINER Pit Kleyersburg <pitkley@googlemail.com>

## Set some variables for override.
# Download Link of TS3 Server
ENV TEAMSPEAK_VERSION 3.0.13.3
ENV TEAMSPEAK_URL http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2

# Create volume-directory
RUN mkdir /teamspeak3

# Install curl
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bzip2 curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download TS3 file and extract it into /opt.
RUN curl -fSL "${TEAMSPEAK_URL}" -o /tmp/teamspeak3-server.tar.bz2 \
    && (cd /opt && tar -xjf /tmp/teamspeak3-server.tar.bz2) \
    && rm /tmp/teamspeak3-server.tar.bz2

ADD /scripts/ /opt/scripts/

# Add new user and chown on mapped folders
RUN adduser --disabled-password --gecos "" teamspeak \
    && chown -R teamspeak:teamspeak /opt/teamspeak3-server_linux_amd64/ \
    && chown -R teamspeak:teamspeak /opt/scripts/ \
    && chown -R teamspeak:teamspeak /teamspeak3 \
    && chmod -R 774 /opt/scripts/

# Inject a Volume for any TS3-Data that needs to be persisted or to be accessible from the host. (e.g. for Backups)
VOLUME ["/teamspeak3"]

# switch user
USER teamspeak

ENTRYPOINT ["/opt/scripts/docker-ts3.sh"]

# Expose the Standard TS3 port.
EXPOSE 9987/udp
# for files
EXPOSE 30033
# for ServerQuery
EXPOSE 10011
