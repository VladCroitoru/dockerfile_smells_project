FROM alpine

RUN apk add --update \
     dovecot \
     dovecot-mysql \
     bash \
 && rm -rf /var/cache/apk/*

COPY conf /etc/dovecot

COPY start.sh /start.sh

CMD ["/start.sh"]
