FROM alpine:3.6

MAINTAINER Ianus IT GmbH <info@ianus-it.de>

COPY files/start.sh /start.sh

RUN apk add --update dovecot rsyslog &&\
    rm -rf /var/cache/apk/* &&\
    chmod +x /start.sh

CMD ["/start.sh"]
