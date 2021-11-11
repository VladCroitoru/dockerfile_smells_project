###############################################
# Debian with added Teamspeak 3 Server.
# Uses SQLite Database on default.
###############################################

# Using latest debian image as base
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

## Set some variables for override.
# Download Link of TS3 Server
ENV TS3_VERSION 3.13.6
ENV TEAMSPEAK_URL https://files.teamspeak-services.com/releases/server/${TS3_VERSION}/teamspeak3-server_linux_amd64-${TS3_VERSION}.tar.bz2

# Update & install packages for graylog
RUN apt-get update && \
    apt-get install -y bzip2 wget

# path for ts3 directory
WORKDIR /usr/local/src/teamspeak3-server_linux_amd64
ENV TS3_DIR /usr/local/src/teamspeak3-server_linux_amd64/

# Inject a Volume for any TS3-Data that needs to be persisted or to be accessible from the host. (e.g. for Backups)
VOLUME ["/var/lib/backup/teamspeak3","/var/log/ts3"]

# Download TS3 file and extract it into /opt.
RUN cd /tmp && wget $TEAMSPEAK_URL
RUN cd /usr/local/src/ && \
    tar xf /tmp/teamspeak3-server_linux_amd64-$TS3_VERSION.tar.bz2
COPY ts3server.ini ${TS3_DIR}


# Expose the Standard TS3 port.
EXPOSE 9987/udp
# for files
EXPOSE 30033
# for ServerQuery
EXPOSE 10011

#Run TS3
CMD ["/usr/local/src/teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh", "inifile=ts3server.ini"]
