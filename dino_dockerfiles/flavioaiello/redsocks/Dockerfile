FROM alpine:3.7

COPY files /

RUN set -ex ;\
    apk update ;\
    apk upgrade ;\
    apk add --no-cache redsocks iptables bash ;\
    chmod +x /usr/local/bin/redsocks.sh

ENTRYPOINT ["/usr/local/bin/redsocks.sh"]
