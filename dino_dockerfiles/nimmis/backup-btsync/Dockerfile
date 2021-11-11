FROM nimmis/alpine-glibc

MAINTAINER nimmis <kjell.havneskold@gmail.com>

COPY root/. /

RUN apk update && apk upgrade && \
    cd /root && \
    curl https://download-cdn.getsync.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz | tar xfz - && \
    mv btsync /usr/local/bin && \
    rm -rf /var/cache/apk/*

VOLUME /backup


