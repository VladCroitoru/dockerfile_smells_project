FROM alpine:3.2

RUN apk add --update \
    cryptsetup \
    gnupg \
 && rm -fr /var/cache/apk/*

ADD encvol-docker.sh /opt/container/bin/

ENTRYPOINT ["/opt/container/bin/encvol-docker.sh"]
