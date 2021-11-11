FROM alpine:edge

MAINTAINER Oleg Kulik "okulik@gorillagroup.com"

RUN apk update && apk add lsyncd inotify-tools \
    && adduser -D -u 1000 www-data

COPY start.sh /

ENV DELAY 2
ENV EXCLUDE_FILE /config/.syncignore

VOLUME ["/var/www", "/data", "/config"]

WORKDIR /data

ENTRYPOINT ["/start.sh"]

CMD ["/usr/bin/lsyncd", "/etc/lsyncd/custom.lua"]
