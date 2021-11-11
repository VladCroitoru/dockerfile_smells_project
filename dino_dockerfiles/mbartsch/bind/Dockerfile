FROM alpine:latest
MAINTAINER Marcelo Bartsch <marcelo@bartsch.cl>

RUN apk --no-cache add bind bash
COPY named.conf /etc/bind/named.conf
COPY localhost.zone 127.0.0.zone root.hint /var/named/
RUN chown -R named /var/named && chmod 775 /var/named && chmod a+r /var/named/*
ENTRYPOINT [ "/usr/sbin/named", "-c", "/etc/bind/named.conf", "-g" , "-u", "named" ]

