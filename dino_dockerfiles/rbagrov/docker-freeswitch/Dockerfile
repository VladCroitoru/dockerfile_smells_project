FROM ubuntu:14.04

#######################################################################################

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r freeswitch && useradd -r -g freeswitch freeswitch

# install basics
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -y install curl git

# install freeswitch
RUN echo 'deb http://files.freeswitch.org/repo/deb/debian/ wheezy main' >>/etc/apt/sources.list.d/freeswitch.list && \
	curl http://files.freeswitch.org/repo/deb/debian/freeswitch_archive_g0.pub | apt-key add - && \
	apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get  -y install freeswitch-meta-all


ENV FREESWITCH_CONF /etc/freeswitch
VOLUME ["/etc/freeswitch"]

ENV FREESWITCH_DATA /var/lib/freeswitch
VOLUME ["/var/lib/freeswitch"]

COPY docker-entrypoint.sh /
COPY docker-command.sh /
RUN chmod +x /docker-entrypoint.sh /docker-command.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

# expose port
EXPOSE 5060
EXPOSE 8021
EXPOSE 16384
EXPOSE 16385
EXPOSE 16386
EXPOSE 16387
EXPOSE 16388
EXPOSE 16389
EXPOSE 16390
EXPOSE 16391
EXPOSE 16392
EXPOSE 16393

CMD ["/docker-command.sh"]
#######################################################################################
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
