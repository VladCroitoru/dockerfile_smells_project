FROM alpine:3.3

MAINTAINER Sonu K. Meena "sonukr666@gmail.com"

RUN apk add --update unbound curl; \
    rm -rf /var/cache/apk/* ;

COPY unbound.conf /etc/unbound/unbound.conf
COPY root.hints /var/unbound/etc/root.hints
COPY root.key /var/unbound/etc/root.key

RUN mkdir -p /var/unbound/scripts ; mkdir -p /etc/unbound/local.d/
COPY block_ads_server.sh /var/unbound/scripts/block_ads_server.sh
COPY docker-entrypoint.sh /var/unbound/scripts/docker-entrypoint.sh
RUN chmod +x /var/unbound/scripts/*
RUN chown -R unbound:unbound /etc/unbound/* && \
    chown -R unbound:unbound /var/unbound/etc && \
    chown -R unbound:unbound /var/unbound/scripts/*  && \
    chown -R unbound:unbound /etc/unbound/local.d  && \
    chown unbound:unbound /var/unbound/etc/*

EXPOSE 53/udp 53/tcp

VOLUME /etc/unbound

RUN unbound-checkconf

WORKDIR /var/unbound/scripts

ENTRYPOINT ["./docker-entrypoint.sh"]
