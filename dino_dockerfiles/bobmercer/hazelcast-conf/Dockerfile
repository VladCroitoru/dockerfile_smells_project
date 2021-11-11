FROM debian:jessie

# To be disable
RUN apt-get update && \
	apt-get -y install curl vim libxml2-utils && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /confd
RUN chmod +x /confd

COPY ./conf.d /etc/confd/conf.d
COPY ./templates /etc/confd/templates
COPY ./bin /etc/confd/bin
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh && \
	chmod +x /etc/confd/bin/*.sh

VOLUME /data/confd
VOLUME /opt/rancher/bin
VOLUME /opt/hazelcast

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["--backend", "rancher", "--prefix", "/2015-12-19", "--interval 30"]