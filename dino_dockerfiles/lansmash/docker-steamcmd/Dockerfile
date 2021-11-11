FROM ubuntu:16.04

# Ubuntu updates
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV DOCKERBIND_VERSION 1
ENV DATA_DIR=/data

# Install dependencies
RUN apt-get update && apt-get install -y curl lib32gcc1 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#VOLUME ["/srv/steamcmd"]

EXPOSE 27015/udp 27015/tcp 953/tcp
#VOLUME ["/etc/bind"]
#VOLUME ["/var/lib/bind"]

RUN mkdir -p /srv/steamcmd && chmod 777 /srv/steamcmd
RUN cd /srv/steamcmd && \
	curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz

WORKDIR /srv/steamcmd

#COPY entrypoint.sh /sbin/entrypoint.sh
#RUN chmod 755 /sbin/entrypoint.sh
#ENTRYPOINT ["/sbin/entrypoint.sh"]

# This container will be executable
ENTRYPOINT ["./steamcmd.sh"]

