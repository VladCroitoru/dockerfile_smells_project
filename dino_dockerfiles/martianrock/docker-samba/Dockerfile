FROM alpine:edge

RUN apk add --update \
    samba-common-tools \
    samba-client \
    samba-server \
    && rm -rf /var/cache/apk/*

EXPOSE 445/tcp

ADD docker-entrypoint.sh /root/docker-entrypoint.sh
RUN chmod +x /root/docker-entrypoint.sh

ENTRYPOINT ["/root/docker-entrypoint.sh"]
CMD []
